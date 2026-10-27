#!/usr/bin/env python3
"""Read-only SF Board validation; optional backed-up exports. Python stdlib only."""
import argparse
import collections
import csv
import datetime
import io
import json
import pathlib
import re
import shutil
import sys

REF_ID = re.compile(r'(?:CHAR|BG|AL|KU)\d+[a-z]?|THUMB\d+[a-z]?')
HEADER = re.compile(r'^Scene (\d+): REF (.+?): /filmlook:')
VO = re.compile(r'VO:\s*("(?:\\.|[^"\\])*")')


def attached(prompt):
    match = HEADER.match(prompt)
    return match.group(2).split(', ') if match else []


def validate(board, directory=None):
    errors, warnings = [], []
    if not isinstance(board, dict):
        return ['Board must be an object.'], warnings
    if not board.get('film') or board.get('kind') != 'phim' or not board.get('updated_at'):
        errors.append('Root needs film, updated_at and kind="phim".')
    scenes = board.get('scenes', [])
    if not isinstance(scenes, list) or not scenes or not isinstance(scenes[0], dict) or scenes[0].get('id') != 'REF':
        return errors + ['scenes[0] must be the REF scene, with sfs and shots.'], warnings
    refs = scenes[0].get('sfs', [])
    if not isinstance(refs, list) or not all(isinstance(r, dict) for r in refs):
        return errors + ['REF sfs must be an array of cards.'], warnings
    refmap = {r.get('id'): r for r in refs}
    if len(refmap) != len(refs):
        errors.append('Duplicate REF IDs.')
    expected = {rid: [] for rid in refmap}
    dependencies = {}
    for r in refs:
        rid = r.get('id')
        if not isinstance(rid, str) or not REF_ID.fullmatch(rid):
            errors.append(f'Invalid REF ID: {rid!r}.')
        for key in ('label', 'desc', 'prompt', 'status', 'notes', 'usedBy', 'refs', 'picked'):
            if key not in r:
                errors.append(f'{rid}: missing {key}.')
        prompt = r.get('prompt', '')
        if not isinstance(prompt, str) or not prompt.strip() or '\n' in prompt or '\r' in prompt:
            errors.append(f'{rid}: reference prompt must be nonempty and single-line.')
        dep = r.get('refs', {})
        if not isinstance(dep, dict) or not isinstance(dep.get('chars'), list):
            errors.append(f'{rid}: refs must contain chars array and bg.'); dep = {'chars': [], 'bg': None}
        links = dep.get('chars', []) + ([dep['bg']] if dep.get('bg') else [])
        dependencies[rid] = links
        for link in links:
            if link not in refmap:
                errors.append(f'{rid}: undefined dependency {link}.')
            else:
                expected[link].append(rid)
        picked = r.get('picked', '')
        if not picked and r.get('status') != 'draft':
            warnings.append(f'{rid}: no picked image; status is not draft.')
        if directory and picked:
            if pathlib.Path(picked).name != picked:
                errors.append(f'{rid}: picked must be a filename, not a path.')
            elif isinstance(rid, str) and REF_ID.fullmatch(rid):
                selected = directory / 'versions' / picked
                asset = directory / 'assets' / (rid + '.png')
                if not selected.is_file() or not asset.is_file():
                    warnings.append(f'{rid}: selected image files are missing; preserve selection and inspect manually.')
                elif selected.read_bytes() != asset.read_bytes():
                    warnings.append(f'{rid}: assets/versions differ; inspect selected media manually.')
    visiting, done = set(), set()
    def visit(rid):
        if rid in visiting:
            errors.append(f'REF dependency cycle at {rid}.'); return
        if rid in done:
            return
        visiting.add(rid)
        for dep in dependencies.get(rid, []):
            if dep in refmap:
                visit(dep)
        visiting.remove(rid); done.add(rid)
    for rid in refmap:
        visit(rid)
    shots, scene_ids = [], []
    for scene in scenes:
        if not isinstance(scene, dict) or not isinstance(scene.get('shots'), list):
            errors.append('Every scene needs a shots array.'); continue
        scene_ids.append(scene.get('id'))
        if scene.get('id') != 'REF':
            shots.extend(scene['shots'])
        elif scene['shots']:
            errors.append('REF scene must not contain video shots.')
    if len(set(scene_ids)) != len(scene_ids):
        errors.append('Duplicate scene IDs.')
    if not shots:
        errors.append('No production clips.')
    for number, shot in enumerate(shots, 1):
        if not isinstance(shot, dict):
            errors.append(f'Clip {number}: must be an object.'); continue
        sid = shot.get('id')
        if sid != f'V-{number:03d}':
            errors.append(f'Clip {number}: expected V-{number:03d}, got {sid}.')
        for key in ('sf', 'dur', 'vstatus', 'ai_request', 'notes', 'text', 'prompt', 'music', 'label', 'goc', 'vpicked'):
            if key not in shot:
                errors.append(f'{sid}: missing {key}.')
        if type(shot.get('dur')) not in (int, float) or shot.get('dur', 0) <= 0:
            errors.append(f'{sid}: dur must be positive numeric seconds.')
        prompt = shot.get('prompt', '')
        if not isinstance(prompt, str) or '\n' in prompt or '\r' in prompt:
            errors.append(f'{sid}: video prompt must be single-line.'); continue
        header = HEADER.match(prompt)
        if not header or int(header.group(1)) != number:
            errors.append(f'{sid}: invalid Scene NNN: REF ...: /filmlook: header.'); continue
        ids = attached(prompt)
        if len(ids) != len(set(ids)):
            errors.append(f'{sid}: duplicate attached refs.')
        if ids[0] != shot.get('sf') or not ids[0].startswith('BG'):
            errors.append(f'{sid}: first attached REF and sf must be the location BG.')
        for rid in ids:
            if rid not in refmap:
                errors.append(f'{sid}: undefined attached REF {rid}.')
            else:
                expected[rid].append(sid)
        if any(rid.startswith('THUMB') for rid in ids):
            errors.append(f'{sid}: THUMB is not a video reference.')
        parts = prompt.split(' | ')[1:]
        numbers = [int(m.group(1)) for part in parts if (m := re.match(r'shot (\d+):', part))]
        if not parts or numbers != list(range(1, len(parts) + 1)):
            errors.append(f'{sid}: invalid | shot N: sequence.')
        if not parts or 'lips closed' not in parts[0] or 'lips closed, hold' not in parts[-1]:
            errors.append(f'{sid}: missing quiet opening/ending edit handles.')
        for token in ('ARRI ALEXA aesthetic', '30fps', 'widescreen 16:9 frame'):
            if token not in prompt:
                errors.append(f'{sid}: missing style token {token}.')
        if prompt.count('/pushin:') > 1:
            errors.append(f'{sid}: more than one push-in.')
        voice = []
        try:
            voice = [json.loads(m) for m in VO.findall(prompt)]
        except json.JSONDecodeError:
            errors.append(f'{sid}: invalid quoted VO string.')
        text = shot.get('text', '')
        if not isinstance(text, str):
            errors.append(f'{sid}: text must be a string.'); text = ''
        lines = text.splitlines()
        if any(': ' not in line for line in lines):
            errors.append(f'{sid}: dialogue text must use ROLE: words lines.')
        expected_voice = [line.split(': ', 1)[-1] for line in lines]
        if voice != expected_voice:
            errors.append(f'{sid}: VO dialogue differs from text or order.')
        for part in parts:
            if len(VO.findall(part)) > 1:
                errors.append(f'{sid}: multiple dialogue turns in one shot.')
        non_dialogue = VO.sub('', prompt)
        if re.search(r'\b\d+(?:\.\d+)?\s*(?:seconds?|secs?|s)\b', non_dialogue, re.I):
            errors.append(f'{sid}: technical seconds in prompt; use dur metadata.')
        if re.search(r'(?:same as|continue from|exact final frame of) (?:the )?(?:previous|last) (?:video|clip)', non_dialogue, re.I):
            errors.append(f'{sid}: previous-clip memory instruction.')
        body_ids = set(re.findall(r'\b(?:CHAR|BG|AL|KU)\d+[a-z]?\b', ' | '.join(parts)))
        if body_ids - set(ids):
            errors.append(f'{sid}: unattached body references: {sorted(body_ids - set(ids))}.')
        note = re.search(r'REF \((\d+)\): (.*?) · ', shot.get('notes', ''))
        if note and (int(note.group(1)) != len(ids) or note.group(2) != ', '.join(ids)):
            errors.append(f'{sid}: notes REF count/list differs from header.')
    for rid, card in refmap.items():
        if card.get('usedBy') != expected[rid]:
            errors.append(f'{rid}: usedBy differs from dependencies and video headers.')
    if directory:
        ledger = directory / 'CONTINUITY-MAP.json'
        if ledger.exists():
            try:
                entries = json.loads(ledger.read_text(encoding='utf-8'))
                if [c['id'] for c in entries] != [s['id'] for s in shots]:
                    errors.append('Continuity ledger clip IDs/order differ from board.')
                for c, s in zip(entries, shots):
                    if c.get('refs') != attached(s['prompt']) or c.get('dur') != s.get('dur'):
                        errors.append(f"{c.get('id')}: ledger refs/dur differ from board.")
                for a, z in zip(entries, entries[1:]):
                    if a['scene'] == z['scene'] and a['ending'] != z['opening']:
                        errors.append(f"{a['id']} -> {z['id']}: ledger state mismatch in continuous scene.")
            except (ValueError, TypeError, KeyError):
                errors.append('Malformed continuity ledger.')
        else:
            warnings.append('No continuity ledger; review actual opening/ending states manually.')
    return errors, warnings


def export(board, directory):
    refs = board['scenes'][0]['sfs']
    rows = [(scene['id'], shot) for scene in board['scenes'][1:] for shot in scene['shots']]
    table = io.StringIO()
    writer = csv.writer(table, delimiter='\t', lineterminator='\n')
    writer.writerow(['CLIP', 'SCENE', 'SECONDS', 'WORDS', 'REFS'])
    for scene, s in rows:
        writer.writerow([s['id'], scene, s['dur'], sum(len(line.split(': ', 1)[-1].split()) for line in s['text'].splitlines()), ', '.join(attached(s['prompt']))])
    output = {'PROMPT_VIDEO.txt': '\n'.join(s['prompt'] for _, s in rows) + '\n', 'BANGTRA.tsv': table.getvalue(), 'REF/prompts.json': json.dumps(refs, ensure_ascii=False, indent=2) + '\n'}
    output.update({'REF/' + r['id'] + '.prompt.txt': r['prompt'] + '\n' for r in refs})
    changed = []
    for name, content in output.items():
        file = directory / name
        if not file.exists() or file.read_text(encoding='utf-8') != content:
            changed.append((file, content))
    stamp = datetime.datetime.now().strftime('%Y-%m-%d/%H%M%S-%f')
    for file, content in changed:
        if file.exists():
            backup = directory / '.snapshots' / stamp / file.relative_to(directory)
            backup.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(file, backup)
        file.parent.mkdir(parents=True, exist_ok=True)
        temporary = file.with_name(file.name + '.part')
        temporary.write_text(content, encoding='utf-8'); temporary.replace(file)
    return len(changed)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=pathlib.Path, help='.project directory or sf-board.json')
    parser.add_argument('--export', action='store_true', help='Export only after validation; back up changed existing exports')
    args = parser.parse_args(argv)
    file = args.project / 'sf-board.json' if args.project.is_dir() else args.project
    try:
        board = json.loads(file.read_text(encoding='utf-8'))
        errors, warnings = validate(board, file.parent)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print(json.dumps({'ok': False, 'errors': [str(exc)]}, ensure_ascii=False)); return 1
    shots = [s for sc in board.get('scenes', [])[1:] for s in sc.get('shots', [])] if isinstance(board, dict) else []
    report = {'ok': not errors, 'errors': errors, 'warnings': warnings, 'clips': len(shots), 'refs': len(board.get('scenes', [{}])[0].get('sfs', [])) if isinstance(board, dict) and board.get('scenes') else 0}
    if not errors:
        report['seconds'] = sum(s['dur'] for s in shots)
        report['camera'] = dict(collections.Counter(tag for s in shots for tag in re.findall(r'/(followshot|pushin):', s['prompt'])))
        if args.export:
            report['export_files_changed'] = export(board, file.parent)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(bool(errors))


if __name__ == '__main__':
    sys.exit(main())

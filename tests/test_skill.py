import copy
import importlib.util
import json
import pathlib
import shutil
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'sf-board-port'

def load(name, file):
    spec = importlib.util.spec_from_file_location(name, file)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module

project = load('project', SKILL / 'scripts' / 'project.py')
installer = load('installer', ROOT / 'install.py')

class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.board = json.loads((SKILL / 'assets/example.project/sf-board.json').read_text(encoding='utf-8'))
    def errors(self):
        return project.validate(self.board)[0]
    def test_working_import_shape_and_handshake(self):
        self.assertEqual(project.validate(self.board, SKILL / 'assets/example.project')[0], [])
    def test_invented_schema_cannot_be_imported(self):
        self.assertTrue(project.validate({'videos': [], 'reference_prompts': []})[0])
    def test_dialogue_rewrite_or_omission_is_detected(self):
        self.board['scenes'][1]['shots'][0]['text'] = 'MAYA: A different line.'
        self.assertTrue(any('VO dialogue differs' in e for e in self.errors()))
    def test_quoted_dialogue_is_not_a_timing_instruction(self):
        s = self.board['scenes'][1]['shots'][0]
        s['text'] = 'MAYA: You have 30 seconds to say "yes".'
        s['prompt'] = s['prompt'].replace('"Here is the record."', json.dumps('You have 30 seconds to say "yes".'))
        self.assertEqual(self.errors(), [])
    def test_technical_timing_is_detected(self):
        self.board['scenes'][1]['shots'][0]['prompt'] += ', hold for 3 seconds'
        self.assertTrue(any('technical seconds' in e for e in self.errors()))
    def test_missing_ref_and_stale_used_by_are_detected(self):
        self.board['scenes'][0]['sfs'].pop(3)
        self.assertTrue(any('undefined attached REF AL1a' in e for e in self.errors()))
        self.setUp(); self.board['scenes'][0]['sfs'][0]['usedBy'] = []
        self.assertTrue(any('usedBy differs' in e for e in self.errors()))
    def test_dependency_cycles_are_detected(self):
        self.board['scenes'][0]['sfs'][0]['refs']['chars'] = ['CHAR2a']
        self.board['scenes'][0]['sfs'][1]['refs']['chars'] = ['CHAR1a']
        self.assertTrue(any('cycle' in e for e in self.errors()))
    def test_missing_edit_handle_and_previous_clip_instruction(self):
        s = self.board['scenes'][1]['shots'][0]
        s['prompt'] = s['prompt'].replace('lips closed, hold', 'same as previous clip')
        self.assertTrue(any('edit handles' in e for e in self.errors()))
        self.assertTrue(any('memory instruction' in e for e in self.errors()))
    def test_malformed_ledger_and_boundary_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            d = pathlib.Path(temp)
            ledger = json.loads((SKILL / 'assets/example.project/CONTINUITY-MAP.json').read_text(encoding='utf-8'))
            ledger[1]['opening']['right'] = 'Elias empty hands'
            (d / 'CONTINUITY-MAP.json').write_text(json.dumps(ledger))
            self.assertTrue(any('state mismatch' in e for e in project.validate(self.board, d)[0]))
    def test_export_roundtrip_and_changed_export_backup(self):
        with tempfile.TemporaryDirectory() as temp:
            d = pathlib.Path(temp)
            self.assertGreater(project.export(self.board, d), 0)
            self.assertEqual(project.export(self.board, d), 0)
            self.assertEqual(json.loads((d / 'REF/prompts.json').read_text(encoding='utf-8')), self.board['scenes'][0]['sfs'])
            self.assertEqual((d / 'PROMPT_VIDEO.txt').read_text(encoding='utf-8').splitlines(), [s['prompt'] for s in self.board['scenes'][1]['shots']])
            (d / 'PROMPT_VIDEO.txt').write_text('previous manual export')
            project.export(self.board, d)
            copies = list((d / '.snapshots').rglob('PROMPT_VIDEO.txt'))
            self.assertEqual(len(copies), 1)
            self.assertEqual(copies[0].read_text(encoding='utf-8'), 'previous manual export')
            self.assertFalse((d / 'assets').exists())

class InstallTests(unittest.TestCase):
    def test_install_is_complete_idempotent_and_preserves_edits_in_backup(self):
        with tempfile.TemporaryDirectory() as temp:
            base = pathlib.Path(temp) / 'skills'
            target, backup, changed = installer.install(SKILL, base)
            self.assertTrue(changed); self.assertIsNone(backup)
            self.assertTrue((target / 'scripts/project.py').is_file())
            self.assertTrue((target / 'references/continuity.md').is_file())
            self.assertFalse(installer.install(SKILL, base)[2])
            (target / 'SKILL.md').write_text('local custom version')
            target, backup, changed = installer.install(SKILL, base)
            self.assertTrue(changed)
            self.assertEqual((backup / 'SKILL.md').read_text(encoding='utf-8'), 'local custom version')
            self.assertFalse(backup.is_relative_to(base))
    def test_ignored_runtime_files_do_not_trigger_reinstall(self):
        with tempfile.TemporaryDirectory() as temp:
            source = pathlib.Path(temp) / 'source'
            shutil.copytree(SKILL, source)
            cache = source / 'scripts' / '__pycache__'; cache.mkdir(exist_ok=True)
            (cache / 'runtime.pyc').write_bytes(b'bytecode')
            (source / '.DS_Store').write_bytes(b'metadata')
            base = pathlib.Path(temp) / 'skills'
            installer.install(source, base)
            self.assertFalse(installer.install(source, base)[2])
    def test_install_does_not_replace_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            base = pathlib.Path(temp) / 'skills'; base.mkdir()
            (base / installer.NAME).symlink_to(SKILL, target_is_directory=True)
            with self.assertRaises(ValueError): installer.install(SKILL, base)

if __name__ == '__main__':
    unittest.main()

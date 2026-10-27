#!/usr/bin/env python3
"""Install the bundled skill without network calls or extra Python packages."""
import argparse
import datetime
import filecmp
import pathlib
import shutil
import tempfile

NAME = 'sf-board-port'


def same_tree(left, right):
    def included(path, base):
        return path.is_file() and '__pycache__' not in path.relative_to(base).parts and path.suffix != '.pyc' and path.name != '.DS_Store'
    a = {p.relative_to(left) for p in left.rglob('*') if included(p, left)}
    b = {p.relative_to(right) for p in right.rglob('*') if included(p, right)}
    return a == b and all(filecmp.cmp(left / p, right / p, shallow=False) for p in a)


def install(source, skills_dir):
    source, skills_dir = pathlib.Path(source), pathlib.Path(skills_dir).expanduser()
    if not (source / 'SKILL.md').is_file():
        raise ValueError('Source does not contain SKILL.md.')
    destination = skills_dir / NAME
    if destination.is_symlink():
        raise ValueError(f'Refusing to replace symlink: {destination}')
    if destination.exists() and not destination.is_dir():
        raise ValueError(f'Destination is not a directory: {destination}')
    if destination.exists() and same_tree(source, destination):
        return destination, None, False
    skills_dir.mkdir(parents=True, exist_ok=True)
    backup = None
    with tempfile.TemporaryDirectory(prefix='.sf-board-install-', dir=skills_dir) as temp:
        staged = pathlib.Path(temp) / NAME
        shutil.copytree(source, staged, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
        if destination.exists():
            stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
            backup = skills_dir.parent / 'skill-backups' / (NAME + '-' + stamp)
            backup.parent.mkdir(parents=True, exist_ok=True)
            destination.rename(backup)
        try:
            staged.rename(destination)
        except OSError:
            if backup and not destination.exists():
                backup.rename(destination)
            raise
    return destination, backup, True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=pathlib.Path, default=pathlib.Path.home() / '.agents' / 'skills', help='Skills parent directory; defaults to ~/.agents/skills')
    args = parser.parse_args()
    source = pathlib.Path(__file__).resolve().parent / 'skills' / NAME
    try:
        destination, backup, changed = install(source, args.dest)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'{exc}\n')
    print(('Installed: ' if changed else 'Already current: ') + str(destination))
    if backup:
        print('Previous version backed up: ' + str(backup))
    print('Invoke $sf-board-port in Codex. If it does not appear, restart Codex.')


if __name__ == '__main__':
    main()

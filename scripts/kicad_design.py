#!/usr/bin/env python3
"""Portable thin client: all engineering calculations and native checks live in kicad-rag."""
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    config = Path(os.environ.get('KICAD_DESIGN_RUNTIME', Path(os.environ.get('CODEX_HOME', Path.home()/'.codex')) / 'kicad-design/runtime.json'))
    if config.exists():
        data = json.loads(config.read_text())
        python = Path(data['python']).expanduser()
        if not python.is_file():
            raise ValueError('Configured Python is missing. Run install.py with the current runtime.')
        return subprocess.run([str(python), '-m', 'kicad_rag.cli', *sys.argv[1:]], check=False).returncode
    try:
        import kicad_rag.cli
    except ImportError as error:
        raise ValueError('Configure the skill with scripts/install.py --python /path/to/kicad-rag/.venv/bin/python') from error
    kicad_rag.cli.main()


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError) as error:
        print(f'Error: {error}', file=sys.stderr)
        raise SystemExit(1) from None

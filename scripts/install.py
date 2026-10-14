#!/usr/bin/env python3
"""Install this skill and bind an already installed kicad-rag runtime. Preserve a dated backup."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

p = argparse.ArgumentParser()
p.add_argument('--python', type=Path, required=True)
p.add_argument('--destination', type=Path, default=Path(os.environ.get('CODEX_HOME', Path.home()/'.codex'))/'skills/kicad-design')
a = p.parse_args()
python = a.python.expanduser().absolute()
subprocess.run([str(python), '-c', 'import kicad_rag.evidence, kicad_rag.native, kicad_rag.board'], check=True)
source = Path(__file__).resolve().parents[1]
destination = a.destination.expanduser().absolute()
if source != destination:
    if destination.exists():
        backup = Path.home()/'.codex/skill-backups'/('kicad-design-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f'))
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(destination, backup)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent, prefix='.kicad-install-') as temp:
        staged = Path(temp)/'kicad-design'
        shutil.copytree(source, staged, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        if destination.exists():
            shutil.rmtree(destination)
        shutil.move(str(staged), destination)
config = Path(os.environ.get('CODEX_HOME', Path.home()/'.codex'))/'kicad-design/runtime.json'
config.parent.mkdir(parents=True, exist_ok=True)
fd, temp = tempfile.mkstemp(dir=config.parent, suffix='.tmp')
with os.fdopen(fd,'w') as stream:
    json.dump({'schema_version':1,'python':str(python)}, stream, indent=2)
os.replace(temp, config)
print(json.dumps({'installed_skill':str(destination),'runtime_config':str(config)},indent=2))

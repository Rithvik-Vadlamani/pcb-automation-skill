# PCB automation skill

A reusable Codex skill for turning electronics requirements into native KiCad schematics and explicitly specified PCB layouts. I wrote the instructions, reference guides, and example specifications to make the design and verification steps repeatable.

The workflow uses datasheet evidence, netlist comparisons, electrical and design rule checks, and rendered review. It keeps design assumptions and unresolved checks with the project so the output can be reviewed.

## Start here

- [SKILL.md](SKILL.md): the main workflow and supported scope.
- [references/](references/): design guidance, evidence handling, and verification procedures.
- [assets/](assets/): small example circuit and board specifications.
- [scripts/](scripts/): runtime launcher and installer.

The skill uses the companion [datasheet assistant](https://github.com/Rithvik-Vadlamani/kicad-datasheet-assistant). Install that package in a virtual environment first, then bind the skill to its Python interpreter:

```sh
python3 scripts/install.py --python /absolute/path/to/assistant/.venv/bin/python
```

The installer backs up an existing skill before installing this copy. KiCad and the required model configuration are separate dependencies. No API credentials or model weights are included.

Generated schematics and boards still need engineering review and hardware testing. Passing ERC or DRC does not establish electrical performance.

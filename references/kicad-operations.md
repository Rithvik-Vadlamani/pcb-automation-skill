# KiCad capabilities and checks

## Discover locally

Resolve `kicad-cli` on PATH; standard macOS installations also provide `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli`. Run `version` and relevant `--help` commands before relying on flags. The creation environment had KiCad 10.0.3; detect the actual version in future sessions.

The CLI performs checks and exports. Authoring requires an appropriate native-file helper, supported API, or UI. Do not assume schematic operations exist because a PCB API exists. Official IPC documentation describes KiCad 9/10 GUI dependencies and version-specific limitations; inspect capabilities before choosing it. Do not install a third-party bridge merely for checks available through the CLI.

For native-file authoring, use documented file formats and verify libraries, instance paths, pins, and coordinates by opening/exporting in KiCad. Test any helper library on a minimal circuit with the installed version before relying on it for a complete project.

## Command examples

Confirm flags with installed command help. Replace executable and project paths and create a task-local reports directory. Run commands separately and inspect output and return status.

```sh
kicad-cli sch erc --format json --severity-all --exit-code-violations --output reports/erc.json project.kicad_sch
kicad-cli sch export netlist --format kicadxml --output reports/netlist.xml project.kicad_sch
kicad-cli sch export svg --output reports/schematic/ project.kicad_sch
kicad-cli pcb drc --format json --severity-all --schematic-parity --refill-zones --exit-code-violations --output reports/drc.json project.kicad_pcb
```

Keep companion schematic/project files available for parity checking. Save refilled zones in the delivered board using UI or a supported save option before final exports; an in-memory DRC refill alone is insufficient for later exports.

Use an available SVG viewer or rendering tool to inspect actual exported images, including all sheets. For requested PDF output, inspect CLI help and render the resulting pages for review.

## Connectivity comparison

Parse the exported netlist into sets of `(component instance, pin number)` endpoints. Compare against intended connections; match identities across hierarchy without relying solely on generated net names. Also check explicit names, power domains, deliberately separate nets, values, footprints, and unused pins. A changed name need not mean changed topology; an unchanged name need not mean correct connectivity.

Keep expected circuit intent independent of generated output. Comparing an output netlist to itself or only rerunning ERC does not validate requirements. For presentation-only edits, preserve a baseline and require unchanged connectivity, identities, values, and footprints unless an intentional correction is in scope.

Distinguish tool failures, rule violations, documented exclusions, connectivity mismatches, and checks that could not run. Missing reports or unsupported flags never count as a pass.

## Primary references

- [KiCad 10 CLI manual](https://docs.kicad.org/10.0/en/cli/cli.html): checks and exports.
- [IPC API for add-on developers](https://dev-docs.kicad.org/en/apis-and-binding/ipc-api/for-addon-developers/): capabilities and version limitations.
- [KiCad file formats](https://dev-docs.kicad.org/en/file-formats/): native readers and writers.
- [Schematic editor](https://docs.kicad.org/10.0/en/eeschema/eeschema.html): wiring, labels, hierarchy, and ERC.
- [PCB editor](https://docs.kicad.org/10.0/en/pcbnew/pcbnew.html): setup, routing, zones, and DRC.

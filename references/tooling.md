# Installation and command contract

The skill is the operating procedure and thin client. The `kicad-rag` Python package owns source extraction, indexing, fact verification, calculation and native-file helpers. Keep one implementation of each numerical equation.

## Set up on another machine

Install KiCad 10 with its symbol and footprint libraries, Python 3.11 or later, and the companion app source distributed with the release:

```bash
python3 -m venv /path/to/kicad-rag/.venv
/path/to/kicad-rag/.venv/bin/python -m pip install -e '/path/to/kicad-rag[dev]'
python3 /path/to/kicad-design/scripts/install.py --python /path/to/kicad-rag/.venv/bin/python
```

The installer validates imports, backs up an installed skill, installs the new files and writes `~/.codex/kicad-design/runtime.json`. `KICAD_DESIGN_RUNTIME` can select another runtime configuration for isolated testing. The wrapper never executes shell strings. Absolute runtime paths belong in the local configuration, not in shared project artifacts. No model service is required for keyword retrieval, native authoring, evidence verification or calculators.

The app discovers KiCad on PATH or in the macOS application bundle. Set `KICAD_SYMBOL_DIR` and `KICAD_FOOTPRINT_DIR` when libraries are elsewhere. `doctor` is read-only and does not download models or call APIs. Check installed command help and version before using a feature. This release was tested with KiCad 10.0.3; other versions require the native regression suite.

## Commands

Replace `kd` below with `python3 /path/to/skill/scripts/kicad_design.py`. Global `--project` goes BEFORE the subcommand. Native authoring commands do not require a RAG project registration.

| Task | Command |
|---|---|
| Initialize evidence project | `kd init evidence-project --name design-name` |
| Register source snapshot | `kd --project evidence-project add source.pdf --id part-reva --parts EXACT-MPN --revision RevA --source-url manufacturer-url` |
| Read and index | `kd --project evidence-project index` |
| Research without generation | `kd --project evidence-project search 'question' --refs U1 --lexical-only --json` |
| Before any schematic exists | `kd --project evidence-project evidence --request request.json --output packet.json --lexical-only` |
| Export actual topology | `kd --project evidence-project sync-kicad circuit.kicad_sch` then `index` |
| Show original text/page | `kd --project evidence-project page document-id 4 --render page4.png` |
| Record a completed review | `kd --project evidence-project accept-fact fact-id --actor reviewer --rationale 'specific completed original-page checks'` |
| Check packet freshness/completeness | `kd --project evidence-project verify-evidence packet.json` |
| Shared calculation | `kd --project evidence-project calculate --evidence packet.json --design design.json --output calculations.json` |
| Source/parameter dependencies | `kd --project evidence-project impact` |
| Inspect schemas | `kd schema evidence-request` or `parameter`, `intent`, `schematic-spec`, `project`, `design` |
| Create a wired schematic | `kd generate-schematic --spec spec.json --intent intent.json --output new-project` |
| Check native schematic | `kd verify-native circuit.kicad_sch --intent intent.json --output reports` |
| Create explicitly routed board | `kd generate-board circuit.kicad_sch --spec board-spec.json --intent intent.json` |
| Refill/save/check complete design | `kd verify-native circuit.kicad_sch --board circuit.kicad_pcb --refill --intent intent.json --output reports` |
| Inspect source and parameter reviews | `kd --project evidence-project gui` |

Exit 0 means the named operation succeeded, not that an entire circuit is approved. Exit 2 means incomplete evidence or failed configured/native checks; exit 1 means an operational/validation error. Read the JSON status and coverage. Never discard a nonzero return code and describe the operation as verified.

## Native authoring boundaries

The schematic writer creates new files with native symbol inheritance, quarter-turn/mirror transforms, visible orthogonal wires, junctions and explicit no-connects. A component may appear in several units: each `(ref, unit)` is unique and the units share symbol/value/footprint/MPN/DNP. All physical pins must appear in independent intent. Shared pins drawn in multiple locations, existing-design rewriting, buses and repeated-file sheet instantiation use native editing.

`generate-hierarchy --spec hierarchy.json --intent intent.json --output new-folder` creates a tree of `SheetDesign` objects. Each contains a `schematic`, named `ports` and optional child `sheets`. A child has name, at, size and design. Parent wires address `SheetName.PortName`; child ports address a physical pin or coordinate. Sheet pins are placed on the connection grid. Use the packaged hierarchy asset or `schema hierarchy-spec` rather than inventing the format. The native export preserves child instance identities and checks the entire physical endpoint graph.

The board writer requires KiCad 10 with `pcbnew` Python bindings. It discovers the bundled macOS interpreter; set `KICAD_PYTHON` for another supported installation. The small worker runs in KiCad's interpreter and applies the native footprint rotation/flip, then returns exact pad positions. The main app stays in its own Python environment. This is a versioned compatibility adapter to the available KiCad 10 API; migration to later bindings needs native regression tests.

Board input has complete placements (`ref`, `at`, final KiCad `angle`, `side` top/bottom), explicit routes, optional zones, `copper_layers` 2/4/6/8 and optional through `vias` (`net`, `at`, `diameter`, `drill`). Internal layers are `In1.Cu`, `In2.Cu`, etc. Logical net aliases resolve only by matching complete independent endpoint groups, including across sheets. Unknown layers, impossible vias and mismatched route endpoints fail. Multiple physical pads with one pad number and blind/buried vias require native routing. This is not an autorouter or an impedance/stackup solver.

The verifier exports actual native files and handles hierarchical netlists with globally annotated references. Source dependency hashes include child sheets and local libraries/project rules. External library/model dependencies need explicit inclusion in the project manifest or snapshots. A manually authored netlist import is a snapshot with no automatic source-schematic freshness proof.

Additional commands: `ocr-copy original.pdf derived.pdf` preserves original bytes and writes lineage, using OCRmyPDF when available or the installed Tesseract + pypdf fallback; `source-diff old.pdf new.pdf --output revision-diff.json` compares extracted text/tables plus bounded rendered-page differences; `simulate reviewed.cir --output simulation-run` runs a bounded self-contained ngspice deck. Use `simulate reviewed.cir --models models.json --output run` for explicit `.include` files. Each manifest entry has project-relative path, SHA-256, source URL and review note. Includes are hash-checked, bounded and flattened; undeclared files, cycles, `.lib` selection, control scripts and plugin loading fail. Native `-n` prevents startup scripts. Execution is not validation of a manufacturer model or its applicability.

For a native release use `release circuit.kicad_sch --intent intent.json --visual-review visual-review.json`, adding `--board circuit.kicad_pcb --physical-review physical-review.json` for a board. A review record follows the `Inspection` model in the app's `release.py`. The release command checks fresh dependencies and recorded inspection verdicts; it cannot independently prove that an inspection was performed.

An optional `configure --shared-extraction-cache /absolute/local/folder` reuses only extraction for identical registered source bytes. Other projects' documents do not become searchable. Choose this location explicitly because it contains source text. Leave it unset for complete per-project storage isolation. Corrupted or mismatched cache entries fail visibly; `index --force` re-extracts from the local original.

`export-manufacturing board.kicad_pcb --output new-folder` requires fresh passing board checks and exports every enabled copper layer for 2/4/6/8-layer boards with mask, silkscreen, outline and separate plated/non-plated drill files. It explicitly uses KiCad Gerber extensions, verifies the expected inventory and records the saved board hash. Its result is `exported_requires_manufacturing_review`, not fabrication approval. `export-assembly board.kicad_pcb --output new-folder` also exports a default-variant BOM and native millimeter placement CSV, excludes DNP, checks reference coverage and reports missing MPNs. Review assembler origin/rotation conventions and component identity. Other variants or fabrication-specific settings use native exports.

## Reading documents before there is a schematic

`search 'question' --parts EXACT-MPN OTHER-MPN --json` uses a provisional exact-part scope. It never labels candidate selection as actual topology. Use separate structured obligations through `evidence` for consequential multi-parameter decisions.

`configure --ocr-mode auto` selectively transcribes pages with little selectable text; `always` is explicit full OCR and `off` preserves digital-only operation. `--ocr-language` and `--ocr-dpi` configure installed language data and 150–400 dpi. Tesseract version, trained-data hashes and settings invalidate transcription caches. Original source identity is retained. Empty or uncertain OCR never becomes an accepted numerical fact.

`extract-parameters --request request.json --output proposals.json` returns source-bound numeric review candidates, not usable facts (exit 2). The GUI imports proposal files and offers **Edit fields** beside the original page. Replace `source_context_unreviewed` with verified conditions and inspect package/category/bound before `accept-fact`; the acceptance command rejects unreviewed condition placeholders.

For optional local embeddings, install `.[local-models]`, predownload a safetensors Sentence Transformer without remote custom code, then configure `--embedding-provider local --embedding-model /absolute/model/folder`. Query/document prefixes remain explicit. Token-window mean pooling prevents silently dropping long chunk tails; it is not a substitute for semantic evaluation. The measured BGE-small experiment underperformed the default keyword/parent path, so do not enable it merely to make the pipeline more complex.

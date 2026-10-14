---
name: kicad-design
description: Design or revise native KiCad schematics and PCBs from requirements, with readable wired circuits, datasheet evidence, independent connectivity checks, and native ERC/DRC. Use for KiCad circuit creation, review, and hardware design changes; preserve schematic-only scope when requested.
---

# KiCad design with traceable evidence

Create editable circuits whose operation a person can follow. Treat electrical reasoning, actual connectivity, readable presentation, and physical layout as separate checks. ERC, DRC, retrieval scores, generated prose, and simulator convergence each establish only their stated scope.

## Start with the user's design

Read the existing project and requirements before choosing a topology. Preserve existing files and authorized scope. A schematic-only request ends with a checked schematic; do not add a board because this skill supports one. Do not require repeated permission for already authorized design work. Ask only for missing operating or mechanical facts that affect a real design decision; continue independent work while awaiting them.

Capture input/output ranges, transient and startup scenarios, current/load, temperature, timing, interfaces, size, connectors, assembly, fabrication and test constraints in `requirements.json`, using [the project contract](references/project-contract.md). Mark assumptions explicitly. Do not silently replace a specified topology, part or package.

Run the bundled wrapper's `doctor` command. Locate it relative to this SKILL.md:

```bash
python3 scripts/kicad_design.py doctor
```

The wrapper uses the configured `kicad-rag` runtime. If missing, follow [installation and tools](references/tooling.md); do not invent a command or assume KiCad's CLI can draw circuits. Read the applicable operation reference before authoring. Native generation targets new files; existing designs and unsupported authoring cases use KiCad's native tools with the same independent verification process.

## Establish evidence before committing design choices

Read [evidence and RAG](references/evidence-rag.md) for datasheet-dependent work. Register manufacturer documents for exact candidate parts, retain original bytes/revisions/source URLs, and index the project. Use provisional candidate manifests before a schematic exists. Only a real KiCad netlist export establishes actual topology.

Write explicit evidence obligations for each important decision: parameter, exact part/package/revision, min/typ/max semantics, units and conditions. Retrieve each prerequisite separately so a long answer about one component cannot hide absent evidence for another. Inspect original PDF pages for tables, pin diagrams, plots, footnotes, ambiguous extraction and all values accepted for engineering use.

Use `extract-parameters` to propose numeric source records when that saves review work. Import proposals in the source viewer, correct their fields, and replace unreviewed condition placeholders before acceptance. Use `parameters.json` records with bound original-page reviews. The `accept-fact` command records a review already performed; never invoke it simply to turn a failing state green. Record yourself as the reviewer when you performed the review, not the user. Quote matches prove location, and numerical matches prove only recognized quantities. Package, column, condition and engineering interpretation still need original-source review. Keep extracted, uncertain, rejected and superseded facts distinct.

Request an `evidence` packet and require `verify-evidence` before using it for checked calculations. Missing, conflicting, stale or inapplicable facts stay unresolved. A legacy `reviewed: true` assertion in `design.json` is not a newly accepted source fact. The `calculate` interface binds accepted evidence to the existing shared calculators; do not create a second implementation of those equations inside the skill.

Read [electrical review](references/electrical-review.md), plus only the applicable [domain guide](references/domain-guides.md). Manufacturer constraints take precedence over generic examples. Never use absolute maximum values as recommended operating limits or typical performance as a guaranteed bound.

## Write independent connectivity intent

Before laying out wires, write `intent.json` from requirements and checked pin functions. Account for every pin, required connection, isolated net and explicit no-connect. Verify numeric symbol pins against actual package pads, including exposed pads, alternate packages and hidden/multi-unit power pins. Store the independent pin-to-pad map for a PCB.

Do not derive the expected intent from the generated netlist or update it merely to make a comparison pass. If engineering evidence changes the intent, record the decision and regenerate dependent checks. Net names alone cannot establish equivalence: compare endpoint groups and separately check intended names and hierarchical scope.

## Draw a circuit people can follow

Read [schematic readability](references/schematic-readability.md) and [circuit patterns](references/circuit-patterns.md). Plan the main power/signal path left to right, with short wired local loops. Place series elements in the path and shunt elements toward their return. Make feedback, bias, protection, decoupling and connector polarity apparent.

Labels name nets and connect distant interfaces; they do not substitute for drawing a local circuit. Never optimize for label count alone. Large ICs and repeated supply rails may need sensible labels and hierarchy. Preserve exact net scope, instance identities and library references.

For a supported new sheet, author `schematic-spec.json` separately from intent and run:

```bash
python3 scripts/kicad_design.py generate-schematic --spec schematic-spec.json --intent intent.json --output new-project
```

Use actual pin coordinates, orthogonal wires, a KiCad connection grid and explicit branch junctions. The helper resolves native symbol inheritance and pin transforms, snapshots used libraries, exports a real netlist, runs ERC and renders sheets. Repeated references use distinct `unit` values with matching physical metadata. Keep all signal and power units present; native export must still account for every physical pin. Generation preserves a failed candidate for inspection and returns a failure status.

For existing/native-authored projects run `verify-native` with an independently written intent. For a new hierarchy use `generate-hierarchy` with real parent sheet pins and matching child ports, as described in [tooling](references/tooling.md). Each file has a unique name and each physical reference/unit a unique instance. Existing hierarchy edits use native KiCad.

After every material change:

- Export through installed KiCad and compare all endpoint groups to intent. Check no-connects, isolation, connector direction, pin numbers and label scope.
- Read all ERC errors, warnings and exclusions. Fix causes; do not change electrical pin types or add false flags/markers to suppress findings.
- Export every sheet and inspect full sheets and component details. Trace the main path and local feedback/return loops. Correct text-wire collisions, hidden branches, ambiguous crossings and excessive label jumps.
- For presentation-only edits, compare connectivity before/after and rerun final ERC/export checks. Save source hashes with the reviews.

A generated SVG is an artifact awaiting inspection, not evidence that visual inspection happened.

## Design the PCB when requested

Read [PCB implementation](references/pcb-verification.md). Establish the actual fabricator's constraints, stackup and mechanical rules first. Derive the board from the checked schematic and preserve associations. Place by current loops, return paths, thermal paths, connector access and signal constraints; schematic coordinates are unrelated to good board placement.

The explicit board writer supports 2/4/6/8 copper layers, KiCad-native rotated/top/bottom placement, through vias and saved zones. Set the actual fabrication rules and dielectric stack in the native project; a copper-layer count alone is not a reviewed stackup. It requires complete placements, verified pad maps, real track paths and optional zone polygons. For arbitrary boards, use native KiCad placement/routing, adding narrowly tested helpers only when necessary. Never represent airwires as completed routing.

Refill and save copper, then run DRC including all track errors, unconnected items and schematic parity. Inspect all violations and exclusions. Independently review pin/pad mapping, polarity, package drawings, mounting and connector mating orientation. Inspect copper and return paths, clearances, thermal paths, silkscreen, outline and drill data. A parity-clean board can still implement a wrong schematic.

Follow [simulation and bench validation](references/simulation.md) when simulation resolves a material uncertainty. Record model origin, pin mapping, parameters and limits. Unbuilt hardware is never bench-tested. Export and review fabrication/assembly outputs only when within scope.

## Deliver a verifiable result

Follow [validation and release](references/validation-release.md). Preserve required local symbol and footprint libraries, native files, requirements, intent, evidence, calculations, decisions and fresh check reports. Record completed visual/physical reviews separately with reviewer and artifact hashes. Final saved artifacts must match reviewed inputs, including project rules and libraries.

Report what was created, why major choices were made, what was actually tested, and remaining uncertainty. Clearly distinguish `pass`, `fail`, `unassessed`, and `not_performed`. Missing tools, crashes, empty reports, stale evidence and partial coverage never become passes. Deliver a useful candidate even when a genuine unresolved issue prevents release, with the issue made explicit.

For efficiency, reuse extraction and embeddings when content/preprocessing is unchanged, inspect only applicable domain references, and rerun affected checks while editing. Run the complete relevant checks once on final saved files. Use [evaluation](references/evaluation.md) when modifying the tools or skill, and add a focused regression for demonstrated failures.

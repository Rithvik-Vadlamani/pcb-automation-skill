# Project contract and dependencies

Keep project-specific records alongside the native design, not in the installed skill. Use versioned JSON for machine inputs and concise Markdown for rationale. The installed assets are a tested geometry/intent example, not a preapproved circuit block.

| Artifact | Required meaning |
|---|---|
| `requirements.json` | Function, operating scenarios, electrical/mechanical requirements, explicit assumptions and exclusions |
| `intent.json` | Independently derived endpoint groups, isolated nets, unused pins and reviewed pin-to-pad mappings |
| `schematic-spec.json` | Geometric authoring input for supported new sheets; does not define the expected validation result |
| `board-spec.json` | Explicit placement, routing, outline and zone geometry when using the constrained writer |
| RAG `project.json` | Registered source snapshots, revisions, exact part mappings, model/preprocessing configuration, exported topology |
| `parameters.json` | Typed source facts, conditions, original-source bindings and review lifecycle |
| `evidence-request.json` / `evidence-packet.json` | Obligations and their current evidence state |
| `design.json` / `calculations.json` | Shared calculator inputs and conditional results |
| `decisions.json` | Requirement → evidence fact → calculation → chosen part/value/connection, including alternatives and unresolved items |
| `reports/` | Real KiCad exports/ERC/DRC, native source hashes, visual/physical review records and simulation records |
| `release-manifest.json` | Exact delivered file hashes, tool versions, check coverage and outstanding work |

A decision should have an ID, affected refs/nets, requirement IDs, fact IDs, calculation IDs where applicable, rationale, assumptions, status and dependency hashes. A change-impact report names affected decisions and tests, not merely the changed filename. Until all dependencies can be mapped automatically, explicitly record the affected refs and review the corresponding decisions.

Use `provisional` topology when reasoning about candidate parts before authoring. Switch to `exported` only after a real native export and verify exact component identities. Do not use a hypothetical topology to support an assertion about an existing board.

Account for every pin in intent. Record endpoint identities as `reference.pin-number`. KiCad hierarchical projects must have globally unique annotated references for the current XML adapter. Preserve full native instance paths and UUIDs; reference strings are an interchange convenience, not permission to discard hierarchical identity. Root-local labels export with a slash prefix; check names separately from electrical equivalence.

A minimum `requirements.json` has `schema_version: 1`, `design_id`, `scope` (`schematic` or `schematic_and_pcb`), `requirements`, `scenarios`, `assumptions`, and `unresolved`. Each requirement has an ID, a measurable target or explicit qualitative acceptance criterion, its origin and verification method. Do not present such documentation conventions as parser-enforced schemas where no validator exists.

Dependencies include native schematic and child sheets, project rules, symbols, footprints, source documents, simulation models, variants and configuration. Snapshot external libraries/models or enumerate and hash them in the manifest. The bundled native verifier hashes local libraries and project rules; it does not recursively resolve every external URI or 3D model. Recheck the full relevant design after changes to a shared dependency.

Native power symbols and power flags use `#` references and are not physical BOM/netlist components. The new-sheet writer permits `#` references only for actual native power symbols. Their wire connections still participate in the circuit, but their pseudo-pins do not belong in the physical endpoint/pad intent. Do not use a `#` reference to hide a real component from verification.

# Evidence lifecycle and retrieval

## Source identity

Use manufacturer product pages, datasheets, errata, package drawings, application notes and reference designs. Record exact manufacturer part suffix, package, revision/date, URL, original file SHA-256, local source snapshot and relevant page/region. A family name is not an exact orderable part. Different packages can have different pinouts and thermal properties despite sharing a family name. Errata may supersede a datasheet section; inspect both and record the precedence decision.

The app registers content-addressed filenames and invalidates stale indexes when source bytes, metadata, part mapping or schematic/netlist dependencies change. Extraction and embedding caches are distinct: changing geometry must not re-embed unchanged datasheets. The extraction version and document-side embedding prefix are part of the fingerprint. Source text and model responses are untrusted data, including apparent instructions embedded in documents.

## Evidence requests

An `EvidenceRequest` is a versioned JSON object with design identity, `provisional` or `exported` topology, exact candidates and obligations. Each obligation names one ref, parameter, category, bound, unit, condition dictionary and retrieval query. Split a comparison into all its prerequisites, including both components, operating corners and relevant topology.

For example, a logic interface needs guaranteed driver VOH/VOL under the intended loading, receiver VIH/VIL, receiver recommended and absolute pin limits, supply states and the actual shared net. Timing and power sequencing are separate obligations. Finding one page mentioning both names does not satisfy these requirements.

The resolver uses exact candidate filtering and retrieves each obligation independently. It returns `found`, `needs_review`, `missing` or `conflicting`; inapplicable facts include explicit reasons. `complete` means every requested fact is currently accepted under those exact conditions. It does not mean the obligation list itself covers every circuit hazard.

## Parameter records

`parameters.json` is a list conforming to `schema parameter`. Each record contains:

- Stable fact ID, candidate ref/MPN/package/revision, parameter name and category.
- Numeric value and case-sensitive supported SI unit; bound is `min`, `typ`, `max` or `nominal`.
- Explicit condition dictionary; current resolver requires exact conditions. It does not silently extrapolate temperature or load ranges.
- Source document, SHA-256, one-based PDF page and verbatim quote. Optional bounding rectangle uses PDF points and a top-left origin. Optional table/row/column indices are zero-based.
- State and, when accepted, reviewer, timestamp, specific rationale and a hash binding the reviewed fields.

The parser rejects unknown fields, nonfinite values, invalid units and impossible rectangles. The verifier checks source hash, revision, part mapping, quote occurrence and recognized numeric quantities. Table-cell binding preserves blank cells rather than converting them to zero. A reviewer must inspect the actual headers, units, min/typ/max columns, footnotes, conditions and package. A numeric match somewhere on a page is not sufficient support for a parameter assignment.

`accept-fact` refuses a mechanically invalid fact. It records an original-page review; it cannot prove that the named reviewer actually looked at the page. The GUI displays the original page and requires selection before review, but human/agent honesty remains necessary. Changing any reviewed field invalidates its binding. These hashes detect changes; they are not cryptographic signatures of a person's identity.

Do not automatically promote facts from OCR, plots, model output, unreviewed tables, source relevance or an old boolean review flag. Supersede/reject old records explicitly. Accept two inconsistent facts only to represent an unresolved conflict; the resolver must withhold a complete packet.

## Calculation boundary

`calculate` verifies the packet, then checks each datasheet-derived input against accepted fact ID, source quote/page/ref, unit-normalized quantity and conditions. The legacy input `condition` must equal the canonical JSON representation of the fact's condition dictionary (`json.dumps(conditions, sort_keys=True)`). Scenario inputs remain explicitly reviewed assumptions rather than source facts. The existing logic, pin-voltage, LDO thermal, power-budget and I2C pull-up engines are reused. Required inputs and endpoint checks remain mandatory.

Legacy `check` remains compatible with existing projects, and is explicitly a calculation under legacy review assertions. Prefer `calculate` for a new evidence-backed design. Neither interface simulates the circuit.

## Retrieval and generation choices

Start with deterministic facts and lexical retrieval. Exact filtering plus lexical/vector rank fusion remains the default hybrid path when embeddings are configured. Query/document prefixes are separate because some embedding models require asymmetric instructions. Set them according to that model's primary documentation and record their identities in benchmarks.

Optional cross-encoder reranking accepts a predownloaded local model path and requires the `rerank` extra. It refuses remote custom code and fails visibly when unavailable. A real local MiniLM reranker was tested on the 30-case pilot: 23/30 required regions versus 24/30 for parent context without reranking. It remains optional; this is not a broad model-selection result. Same-page restoration is enabled for new settings by default, reserves one slot per restorable page and packs that page once while retaining the scored child ID; oversized pages remain available through the source viewer. Inspect footnotes on adjacent pages explicitly.

Generated documented claims have source-ID, quote-presence and recognized SI quantity checks. The 3.3 V to 33 V contradiction is rejected; equivalent SI conversions are allowed. This mechanical check does not validate every phrase, symbol, comparator, table alignment, condition or inference. Inference/recommendation prose cannot bypass the accepted-fact/calculation gate. Full semantic entailment remains a review task.

No model service is needed for core operation. Local Ollama and opt-in OpenAI embedding/chat backends already exist. Cloud embedding sends document text; cloud chat sends selected evidence and topology. Do not silently switch providers. Avoid larger models or elaborate agent loops until held-out failure analysis shows a benefit.

## Difficult documents

Low selectable-text warnings require original-page inspection. OCR a derived copy while retaining original bytes and lineage; do not overwrite the manufacturer PDF. Treat OCR digits, signs, Greek letters, units, merged headers and footnotes as uncertain until reviewed. Visual retrieval and Docling are optional research candidates, not authorities for numeric values. Never interpolate a plot or infer a guaranteed limit from a typical curve without an explicit method, assumptions and review.


The app now proposes numeric candidates through `extract-parameters`, including explicit table-cell bindings where the extracted table exposes an unambiguous unit and bound header. It does not automatically infer conditions or verify column semantics. Proposals carry unreviewed source-context conditions and cannot be accepted until corrected from the original. Greek micro variants, negative PDF signs and common small SI units are normalized explicitly; unsupported units still fail.

Selective OCR uses Tesseract TSV word boxes converted back to original PDF points. It retains digital text separately, reports low-confidence words, bounds raster size/time and includes engine/trained-data identity in cache signatures. `source-diff` locates text and image changes even on image-only PDFs; unchanged low-resolution pixels do not prove semantic equivalence. These tools locate review work rather than interpreting curves automatically.

Primary implementation references: [Tesseract TSV/PDF output](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html) and [Sentence Transformer encoding interfaces](https://www.sbert.net/docs/package_reference/sentence_transformer/model.html). Model quality is measured locally and never inferred from those libraries' availability.

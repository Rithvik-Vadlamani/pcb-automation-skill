# Evaluation and improvement

Run the companion package's software suite and native integration tests. Native tests require KiCad and its libraries and must report skips explicitly on machines without them. They exercise real native exports, saved copper fills and deliberate wiring/pad faults rather than mocked KiCad success messages.

Use the 30-case manufacturer-document pilot to measure exact supporting text regions, complete prerequisite coverage and latency. The pilot is text-reviewed and correlated within three device documents; it is not a representative holdout and does not establish a production accuracy percentage. The evaluator validates gold region existence, withholds labels from the retrieval pipeline, and records actual retrieved IDs/pages and configuration. A plotted-curve location case measures retrieval, not interpretation of the curve.

Compare keyword baseline, configured embeddings, optional reranking and parent restoration on the same corpus and cases. Report failures by package, conditions, timing, thermal and lookup slices. Do not silently change labels after seeing failures. Investigate wrong/missing pages, incomplete condition context and retrieval crowding before changing a model. Report cold/warm timing and number of documents/regions/cases. A mock embedding test verifies plumbing only.

Before claiming reliable automatic numerical acceptance, build a separately reviewed held-out dataset across more device families, manufacturers, revisions and document layouts. Include wrong-family near matches, conflicting revisions, source removal, missing prerequisites, ambiguous tables, units/comparators, false evidence and scanned pages. Measure acceptance precision together with coverage/abstention; refusing every request is not useful accuracy.

The expanded suite now contains 200 cases over 25 original PDFs, 777 pages and four manufacturers: 150 row/section navigation questions, 25 multi-prerequisite queries and 25 synthetic missing-part cases. Device families are separated into development/calibration/holdout. Its anchors were reviewed in text, not independently labeled as engineering answers. Preserve that distinction. Do not claim a model-selection winner or 99% factual reliability without measuring that exact configuration on an appropriate set.

Useful primary inspiration, with bounded roles:

- Anthropic contextual retrieval: https://www.anthropic.com/engineering/contextual-retrieval — motivates chunk context; published gains are not this project's results.
- Docling: https://github.com/docling-project/docling — structured PDF candidates to compare on difficult pages.
- RAGFlow: https://github.com/infiniflow/ragflow — inspectable chunks and retrieval workflows; complexity itself is not reliability.
- Sentence Transformers: https://www.sbert.net/docs/package_reference/cross_encoder/cross_encoder.html — local cross-encoder adapter interface.
- ALCE: https://aclanthology.org/2023.emnlp-main.398/ — citation quality requires more than source existence.
- RAGAs: https://aclanthology.org/2024.eacl-demo.16/ — diagnostic evaluation; model judges need independent calibration.
- Lost in the Middle: https://aclanthology.org/2024.tacl-1.9/ — preserve important evidence under context limits rather than appending everything.

The installed MiniLM experiment used `cross-encoder/ms-marco-MiniLM-L6-v2` at commit `233902d25c440f23af6f7d6e94d2946bac0bee0a`, downloaded as local safetensors without remote custom code. It scored 23/30, including a timing-slice regression; parent context alone scored 24/30. Retain the failure details and keep the reranker disabled by default.


In the v0.3 expanded suite, final keyword/parent retrieval found all required regions in 53/56 development, 40/42 calibration and 74/77 held-out questions; all 25 missing-source probes produced empty document scope. Aggregate complete-region coverage is 167/175 (95.4%). The holdout case-level Wilson 95% interval is approximately 89.2–98.7%; family-cluster uncertainty is reported separately. Do not turn this into a 95.4% circuit-accuracy or 99% automatic-fact claim.

The default was chosen using development/calibration, then frozen for held-out scoring. Real local `BAAI/bge-small-en-v1.5` at commit `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a` scored 47/56 development and 35/42 calibration in the measured hybrid configuration, below keyword/parent retrieval. Keep it available for experiments and disabled by default. Reranker and embedding experiments are different configurations; neither inherits another setup's score.

Run `scripts/download_benchmark.py new-corpus` from the app to obtain hash-pinned original PDFs, then index and run `scripts/evaluate_benchmark.py new-corpus examples/evaluation/expanded-200.jsonl --split holdout --output report.json`. Manufacturer revisions that no longer match the pinned sources require new labels, not silent benchmark replacement. The evaluator validates source hashes/quotes, rejects family split leakage, records code/configuration hashes, reports cold/warm time and withholds all gold fields from production retrieval.

Remaining research claims need a separate independently reviewed numerical/condition/answer dataset, representative naturally scanned documents, and measured model-answer support/abstention. Automatic acceptance remains zero by policy; zero accepted errors on zero automatic acceptances is not 100% precision. Docling, visual embeddings and fine-tuning remain optional experiments, not missing runtime prerequisites.

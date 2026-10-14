# Validation and release

A reviewable design needs independent electrical intent, actual native artifacts and evidence whose inputs are current. The release process is scoped to the user's request.

## Required checks

For a schematic: source/parameter applicability, calculations appropriate to the design, actual native export, all intended endpoint groups, ERC including warnings/exclusions, every rendered sheet and component-detail visual inspection. For a PCB add saved zone fills, all DRC categories and parity, independent pad mapping, physical layout review, and requested manufacturing-file review. Simulation and bench tests are additional evidence only when actually performed.

Use separate records for machine checks and reviewer observations. A visual review should name the reviewer, files/pages inspected, full-sheet and detail views, findings, corrections, final verdict and exact native input hashes. A physical review should also name inspected copper/mask/silk/outline/drill layers and applicable mechanical constraints. The verifier initializes these states as `not_performed`; it must not automatically mark them complete when an image file is generated.

Record each check as pass/fail/unassessed/not_performed with scope, inputs, method/tool version, result and unresolved issues. A missing executable, timeout, crash, malformed JSON, stale source, absent output, empty check set or unsupported feature is never a pass. An ERC/DRC exclusion is evidence to inspect, not a resolved design error by default.

## Final artifact sequence

1. Save final native files, required project rules and local libraries.
2. Resolve or explicitly identify remaining evidence and engineering issues.
3. Run final native schematic and board checks against the independent intent; verify packet/calculation freshness.
4. Render and inspect final sheets/layers. If a correction changes files, rerun relevant checks and update the review hashes.
5. Export requested deliverables, inspect them and hash every delivered file. Keep tool reports and current status readable alongside native files.
6. Summarize actual verification and outstanding work without claiming hardware validation from software checks.

The companion `release` command checks that referenced native input hashes are current and machine checks pass, and requires explicit visual/physical review records before creating a release manifest. This is a bounded workflow check, not an engineering certification. Do not create a review record claiming an inspection you did not perform.

## Regression expectations

Keep the original failure stimulus, independent expected behavior, actual tool result and a focused regression. Useful faults include a deleted wire, a short between intended separate nets, a swapped numeric pad map, stale source/review data, a wrong package/revision, min/typ/max confusion and a 3.3 V to 33 V claim. A test that merely searches the skill text for a sentence does not establish that the behavior works.

Release the skill with installation instructions, versioned companion package, declared tested tool versions, sample inputs, real native artifacts and measured test reports. Retain the prior installed skill and source backup. Do not publish private project artifacts or source documents to a public repository without authorization.

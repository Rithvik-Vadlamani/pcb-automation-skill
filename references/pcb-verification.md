# PCB implementation and physical verification

## Before placement

Start with the checked schematic and reviewed numeric symbol-pin-to-package-pad mapping. Confirm mechanical dimensions, holes, enclosure interfaces, keepouts, connector mating direction, access, layer count, copper weight, finish and assembly process. Obtain design rules from the actual fabricator/assembler. Units and tolerances belong beside dimensions.

Set real clearances, widths, drill/via/annular-ring limits and any net-class overrides before routing. Inspect custom rule exclusions and resolved severities. Unspecified defaults are not evidence that a process can manufacture the board. For controlled impedance, use the fabricator's stackup and calculator/service rather than guessing a trace width.

## Placement and routing review

Fix mechanically constrained components, then arrange active stages and local support by current/signal flow. Bypass capacitors need a short complete current loop through supply and return; proximity alone is insufficient. Keep sensitive feedback and sense connections out of noisy high-current paths. Use Kelvin sense paths when required by the measurement topology. Check exposed-pad connections and thermal-via implications for assembly.

Inspect every signal's return path across reference planes, transitions and connectors. Avoid inadvertent slots or isolated islands that force return currents around long detours. Route switching loops compactly and control switch-node coupling. Review high-current bottlenecks at pads, vias, neckdowns and connector contacts. Review all relevant voltage separation, not just the nominal supply label.

A topological graph path is not a model of current distribution, a physical return path, or a DC conduction path through arbitrary components. DRC cannot prove EMI, thermal or analog performance.

## Native checks

Use KiCad's actual board file. Refill zones and save before exporting final results. Run DRC with `--all-track-errors`, `--schematic-parity`, `--severity-all`, `--refill-zones` and `--save-board` when supported by the installed CLI. Read the generated JSON and inspect violations, unconnected items and parity independently. Zero unconnected items is required for a completed routed fixture; an unrouted placement is an intermediate artifact.

Read legitimate exclusions individually and document the engineering reason. Never blanket-disable violations to obtain a pass. Verify numeric pad mapping independently even if schematic parity passes. Compare net names/scope and endpoint groups, including intentional isolation and no-connect behavior.

After any save that changes copper, geometry, rules, footprints or native metadata, regenerate affected reports. Run final schematic and board checks after footprint library snapshots have been added, because they are part of the dependency set.

## Visual and manufacturing review

Inspect top and bottom copper, mask, silkscreen, outline and holes at board and pad detail scales. Check connector orientation, pin-1/polarity marks, reference visibility, text over pads, clipped outlines, footprints outside the board, courtyard conflicts and assembly access. Use 3D for fit and orientation but inspect actual copper separately.

When requested, export Gerbers, drill maps/files and applicable BOM/position files. Confirm saved board hashes match the exports' input. Inspect the exported files in a manufacturing viewer, count/map drill tools, check plated/non-plated holes, outline continuity, units, layer names and assembly origin/rotation conventions. Do not call outputs fabrication-ready solely because filenames exist. Ordering boards or sending files to a manufacturer is a separate external action and requires the user's authorization.

## Scope of the bundled fixture

The test board exercises native schematic export, numeric pad maps, real tracks, two saved filled copper zones, DRC, unconnected detection and schematic parity. Its rule-clean result applies only to the example and declared software checks. It does not validate the electrical, thermal, RF, high-voltage or production suitability of arbitrary future boards.

Official references: https://docs.kicad.org/10.0/en/pcbnew/pcbnew.html and https://docs.kicad.org/10.0/en/cli/cli.html.

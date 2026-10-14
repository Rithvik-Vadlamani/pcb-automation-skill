# Readable circuit schematics

The reader should be able to trace operation without repeatedly searching for matching labels. These are defaults; preserve conventional topology when it explains a circuit better.

## Placement and wiring

- Place the principal signal or energy path generally left to right. Orient supplies upward and ground downward where practical. Keep actual voltage domains and return nets distinct.
- Keep each functional circuit together: input conditioning, gain stage, regulator, driver, or interface. Show internal wiring even when the sheet uses named sections.
- Place series elements in the visible signal path and shunt elements as branches. Put dividers vertically where helpful; draw amplifier and regulator feedback as visible loops.
- Put bias, pull-up/down, timing, protection, and local decoupling components near the pins they support. Large multi-unit ICs may need a clearly associated power unit/decoupling group; avoid crowding signal circuitry just to avoid a separate group.
- Use a consistent native connection grid and orthogonal wires. Connect to actual transformed pin endpoints after rotation/mirroring; visual proximity is not connectivity.
- Prefer clear T junctions; show junctions at intended electrical joins. Avoid ambiguous four-way crossings and wires passing through symbols or text.
- Allow space for legible reference, value, polarity, pin, and net text. Use a larger sheet or meaningful hierarchy before shrinking a crowded page.

## Labels and hierarchy

- Wire nearby connections inside functional circuits. Labels may name those wires without breaking the visible path.
- Use labels for distant inter-block signals, repeated shared interfaces, and power distribution when continuous wiring would obscure the circuit. Choose local/hierarchical/global scope intentionally; identical local labels on different sheets are not automatically connected.
- Hierarchical designs should expose meaningful ports. Keep the internal circuit visible on its child sheet. Section titles explain function but do not replace the drawing.
- Avoid artificial label-count targets or requiring every net to span a whole sheet. Judge how much cross-referencing the reader needs to understand each circuit.

## Example layout intent

A passive RC low-pass should show the series resistor and capacitor branch:

```text
IN ─── R1 ───┬─── OUT
             │
             C1
             │
            GND
```

This is a placement sketch. Deliver native KiCad symbols, real pins and wires, and verified connectivity. A transistor driver should similarly expose its input resistor, switching device, load branch, and applicable protection path in one understandable circuit.

## Visual acceptance

Inspect every rendered sheet, as a whole sheet and zoomed into each circuit:

- Can the reader follow input to output and supporting circuitry without hunting through labels?
- Are feedback, bias, current paths, and voltage-domain boundaries understandable?
- Are references, values, polarity, connectors, and intentional no-connects unambiguous?
- Are there overlapping fields, accidental-looking junctions, dangling wires, or wires through symbols?
- Does hierarchy reduce complexity while keeping local circuits self-contained?

Confirm issues against the native schematic and netlist. After visual repairs, repeat connectivity checks; attractive wiring can still connect incorrect pins.

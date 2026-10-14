# Readable circuit patterns

Use these as spatial/communication patterns, never as an electrically preapproved block library.

## Signal conditioning

Draw source connector, series resistor/filter stage and destination in left-to-right order. Draw shunt capacitors or clamps vertically to the actual return. Keep the physical branch visible. Put passive references and values beside a vertical branch, not on its wire. Name the signal on a clear wire span rather than on a symbol terminal. The bundled RC fixture demonstrates this arrangement with real connectivity.

## Power conversion and regulation

Show input connector/protection/input capacitance, controller or switching element, energy-storage components, output capacitance and output connector as one visible path. Draw the local return under the stage. Place feedback divider near the sense point and route a visible feedback connection to the correct controller pin when the drawing remains clear. Bootstrap, decoupling and BIAS support should be visible next to their actual pins. Distinguish the schematic's functional return from PCB routing instructions; one long drawn ground line does not prescribe a long physical return.

## Amplifier feedback

Place the input network at the left, amplifier at the center and output at the right. Put the feedback resistor/capacitor in a clearly closed path back to the correct input. Place bias/reference branches toward the appropriate reference rail. Leave enough room for feedback crossings and junctions to be unambiguous. A net label on every op-amp pin obscures operation.

## Microcontroller and interfaces

Group pins by function using an appropriate library symbol or genuinely useful hierarchy. Keep oscillator, reset, programming, supply decoupling and interface protection near the relevant pins/units. Long pin rows do not require long wires across the entire sheet; use short local wiring and named ports to another functional sheet. Show connector pin order and voltage levels explicitly. Do not split a small local network into several label-only boxes.

## Switching drivers and loads

Show gate/base driver, switching device, load connector, current sense and flyback/clamp paths. Make the control reference, power return and any isolation boundary legible. Distinguish power and sense returns by the actual circuit, not decorative colors or misleading net labels.

## Review questions

At whole-sheet scale, can a reader find the input, output, reference/return and major blocks without hunting? At component scale, can they trace a branch or feedback path without a label search? Are every junction and crossing intentional? Can they distinguish connector pin numbers, reference designators and values? Are unused pins explicit and power pins accounted for? Can another engineer reconstruct intended operation from the native schematic without opening a separate netlist?

Use restrained notes for operating assumptions and warnings that matter to the reader. Avoid filling the schematic with implementation logs, tool names, generated evidence JSON or a testing checklist. Keep detailed calculations and source records in companion documentation with concise relevant source notes on the sheet.

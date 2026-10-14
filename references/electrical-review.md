# Electrical review and calculation discipline

Requirements define the operating envelope. Review steady-state minima/maxima and relevant combinations of startup, shutdown, hot-plug, reverse polarity, faults, missing supplies, load transients and temperature. Do not assume every worst-case limit occurs simultaneously; state the corner model and conservatism.

## Part and pin review

Check exact MPN, package drawing, pin numbering/view direction, exposed pad, alternate functions, power pins, reference/enable/mode pins, reserved and NC handling. A pin called NC may require grounding for thermal reasons, or require isolation; read the exact device instructions. Verify the symbol-to-pad map independently. Read errata and reference-layout limitations.

Check operating ratings, absolute limits, transient limits, derating, tolerance, aging and relevant protection. Verify input/output common-mode and differential ranges separately. Apply test conditions attached to guaranteed characteristics. Never assume an operating range guarantees every electrical specification at every point within that range.

## Shared calculator scope

The app implements five deterministic calculations. Read `schema design` and the app's `docs/DESIGN_CHECKS.md` for exact role names and constraints before constructing inputs.

| Calculation | Inputs and meaning | What remains outside it |
|---|---|---|
| Logic compatibility | Guaranteed VOH vs VIH, VIL vs VOL under stated loading, same actual net | Overvoltage, power-off injection, transient ringing, timing and fanout |
| Pin voltage | Applied min/max compared with recommended and absolute input limits | Fast transients, injection current, ESD structures and time-dependent limits |
| LDO thermal | Input/output/load/ground-current corner; dissipation; ambient plus dissipation × thermal resistance | Stability, PCB-dependent thermal behavior, transient temperature, actual measurements |
| Power budget | Available current/power budget vs summed declared demand | Inrush, sequencing, source dynamics and connector heating |
| I2C pull-up | Sink-current lower resistance limit; rise-time upper resistance limit with capacitance and tolerance | Translator behavior, mixed supplies, actual routing, overshoot and measured timing |

Every required input must be present, unit-correct and applicable. Do not insert guessed zeroes or typical values to make a calculator run. Empty configured checks mean nothing was assessed. Add a new calculator only for a recurring, well-specified formula with dimensional review, an independently computed example, boundary tests and source references. Do not evaluate arbitrary generated Python expressions as equations.

## Other recurring calculations

For passives consider voltage/current rating, tolerance, temperature coefficient, actual dissipation, pulse energy and package limits. Ceramic capacitor effective capacitance depends on DC bias, temperature and tolerance; nominal capacitance alone can be inadequate. Inductors need ripple/peak current, saturation, RMS heating and losses. Feedback dividers need tolerance sensitivity, bias-current error and permitted impedance.

For switching power stages review duty range, minimum on/off time, current-limit behavior, peak/RMS currents, compensation/stability, input/output ripple and transient response, switch-node stress, bootstrap/BIAS operating constraints, protection and thermal paths. A power-stage spreadsheet does not validate a layout or control loop. Record the exact equations and manufacturer reference design assumptions.

For analog interfaces review input/output range, rail headroom, source/load impedance, offset/bias error, noise bandwidth, gain/phase margin, sampling kickback and anti-alias requirements. For digital interfaces review DC margins and timing/loading/termination/power-sequence behavior independently.

Use scenario sweeps when a single nominal point hides an important dependency. Keep a decision ledger connecting each chosen value and topology to requirements and accepted evidence. Simulation and bench testing remain separate evidence types.

Primary reference categories: exact manufacturer datasheet and errata first; TI's *Semiconductor and IC Package Thermal Metrics* for thermal interpretation; device application notes for topology-specific calculations. Avoid copying rules of thumb into numeric acceptance gates without their scope and source.

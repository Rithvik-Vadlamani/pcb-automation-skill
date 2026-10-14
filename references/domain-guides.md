# Domain-specific design extensions

Read only the domains needed for the project. These guides are review prompts; numeric requirements come from the selected parts, actual interface specification, environment and fabricator.

| Domain | Schematic concerns | PCB concerns | Additional validation |
|---|---|---|---|
| MCU/embedded | Supply domains, decoupling, reset/boot straps, oscillator, debug access, unused pin behavior | Decoupling loops, oscillator loading/placement, connector polarity, test access | Startup, programming, clock and power-state tests |
| Switching power | Ratings, ripple/peak/RMS current, compensation, bootstrap/BIAS, protection, sequencing | High di/dt loops, switch-node area, Kelvin feedback, thermal pad/vias, return geometry | Load/line transients, loop stability where applicable, thermal/EMI bench tests |
| LDO/linear power | Dropout, reverse current, capacitor stability/ESR, dissipation and enable | Thermal path, decoupling, high-impedance feedback | Thermal and load-step testing |
| Precision analog/sensors | Common-mode/headroom, source impedance, bias, noise, filtering, reference integrity | Kelvin connections, leakage/guarding where justified, separation from switching currents | Offset/gain/noise over temperature and actual load |
| Motor/solenoid drivers | Gate drive, dead time, sense scaling, flyback, current limit, fault states | Commutation loops, shunt Kelvin routing, high-current copper, return and thermal paths | Switching waveform, fault and inductive-energy testing |
| Digital buses | Logic levels, pull-ups, termination, loading, voltage domains, power-off behavior | Return continuity, length/impedance where specification requires it, protection placement | Eye/timing or protocol tests appropriate to rate |
| RF | Matching/reference circuit, biasing, antenna and frequency-specific models | Controlled geometry, stackup, RF return, enclosure/antenna clearance | VNA/spectrum/OTA testing; specialist review as needed |
| High voltage/isolation | Working/transient voltage, isolation components, discharge, fault assumptions | Creepage/clearance tied to the applicable standard, pollution/environment and material group | Appropriate specialist and compliance testing |
| High speed | Channel budget, reference clocks, terminations, connectors and signal models | Fabricator-supported controlled impedance, reference transitions, via stubs, length/skew constraints | SI/PI simulation with valid models and measured correlation |

RF, high voltage and high speed are conditional extensions, not domains certified by the RC example or a clean DRC report. Do not invent generic creepage, trace-width, impedance or thermal limits. If a requirement depends on a current standard or fabricator capability, verify that exact primary source. Distinguish an unresolved requirement from a generic disclaimer.

Useful primary starting points:

- KiCad library conventions: https://klc.kicad.org/ — symbol grouping and library construction, subordinate to actual datasheet pin functions.
- TI thermal metrics: https://www.ti.com/lit/an/spra953d/spra953d.pdf — metric definitions and assumptions, not a universal board temperature predictor.
- Analog Devices MT-101: https://www.analog.com/media/en/training-seminars/tutorials/MT-101.pdf — decoupling mechanisms and examples.
- Analog Devices MT-031: https://www.analog.com/media/en/training-seminars/tutorials/MT-031.pdf — converter grounding considerations, not a universal instruction to split planes.
- Actual manufacturer reference layouts and fabricator's published stackup/design rules for the chosen implementation.

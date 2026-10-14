# Simulation and bench evidence

Use simulation to answer a concrete uncertainty: operating point, filtering, startup, transient load, stability, component stress or another specified behavior. Do not run an irrelevant simulation simply to add a report.

Record simulator and version, model source/revision/hash/license, model pin order, schematic pin-to-model mapping, device parameters, corner assumptions, stimuli, timestep/tolerances and measurements. Include model limitations: a nominal macromodel may omit temperature, protection, switching detail, saturation, EMI or failure behavior.

Before interpreting results, verify the simulated netlist matches the intended subcircuit and all supplies/grounds/loads. Check convergence and simulator warnings. Validate units and measurement definitions. A converged waveform does not prove a circuit is correct. Compare a simple analytical case or known reference when introducing a model or simulation helper.

Keep simulations in their own directory and never overwrite source manufacturer models. Run ngspice with an argument list and a bounded timeout, capturing the actual log and exit code. Do not permit arbitrary document text to become simulator control commands or shell commands. Treat simulation decks as executable inputs to inspect before running, including included files and command blocks.

A bench plan should identify equipment, supply limits, probe method/grounding, loads, expected ranges, pass/fail criteria and relevant fault tests. Record actual observations only after a physical test. Do not describe a simulated or unbuilt board as tested hardware. If a physical measurement is needed to settle a design uncertainty, deliver the current evidence and the specific remaining test rather than inventing a result.

The bundled `simulate` wrapper runs self-contained batch decks only and records execution as `executed_requires_measurement_review`, never as a circuit pass. Its regression compares an actual ngspice RC response at the analytical corner frequency with magnitude 1/√2 and phase −π/4. This validates that particular fixture and measurement path, not manufacturer macromodel fidelity or arbitrary circuit behavior.


The portable wrapper accepts reviewed include manifests through `simulate --models`. It hashes model files, flattens only declared project-local includes, rejects cycles/undeclared files/control blocks and runs ngspice with startup files disabled. This supports self-contained model subcircuits; `.lib` corner selection, binary plugins and simulator-specific scripting still use an explicitly reviewed native workflow. Retain expanded deck, original deck, model hashes, log and declared corner. No successful process status is a measurement pass by itself.

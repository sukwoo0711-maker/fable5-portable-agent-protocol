# Generic Embedded-Agent Adapter Example

This example is for firmware, driver, RTOS, board, or lab workflows. It avoids
assuming any particular IDE, debug probe, RTOS, compiler, or agent runtime.

| Protocol capability | Embedded mapping | Required artifact |
| --- | --- | --- |
| `search_project` | Source tree search across firmware, config, linker, generated-source inputs | Query and matching paths |
| `read_file` | Read source, headers, build manifests, generated-source inputs, tests, logs | File path and relevant context |
| `edit_file` | Patch source inputs, config, or generator inputs | Diff of source inputs |
| `run_command` | Host unit test, static check, cross-build, simulator, or request-human run | Command/method and result |
| `inspect_diff` | Version-control status and diff | Status/diff output |
| `simulator_or_hardware` | Simulator, emulator, probe, board log, trace, or lab request | Target evidence and target identity |
| `request_approval` | Ask before flash, erase, fuse, provisioning, power, production, or shared lab action | Approval record |
| `report_final` | Final report with host vs target evidence separated | Completion gate and limitations |

Embedded-specific rules:

- Host tests do not prove target behavior.
- Generated artifacts should be changed through their source inputs when those
  inputs exist.
- Flashing, erasing, provisioning, or changing shared hardware requires
  approval.
- Final reports must separate `host evidence`, `cross-build evidence`, and
  `target or hardware evidence`.

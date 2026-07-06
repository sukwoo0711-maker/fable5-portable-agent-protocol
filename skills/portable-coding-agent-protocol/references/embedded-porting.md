# Embedded Development Porting

Use this module for firmware, drivers, RTOS work, cross-compilation, hardware
debugging, target boards, lab tools, bootloaders, scripts that touch devices, or
host tools used by embedded developers.

## 1. Identify The Execution Domain

Classify each change as one or more of:

- Host-only tool or test.
- Cross-compiled target code.
- Simulator or emulator path.
- Hardware-in-the-loop path.
- Flash, fuse, calibration, provisioning, or production operation.

Do not treat host success as target success unless the project explicitly uses
host tests as the acceptance gate.

## 2. Capture Toolchain Context

Before changing build-sensitive code, inspect:

- Build system and target selection.
- Compiler, linker, flags, startup files, linker scripts, and memory maps.
- Generated files and source generation inputs.
- Board, MCU, SoC, RTOS, bootloader, and driver boundaries.
- Existing static analysis, unit test, simulator, or hardware test commands.

Use documented project commands instead of inventing generic compiler commands.

## 3. Respect Hardware Safety Gates

Ask before:

- Flashing or erasing a device.
- Changing fuses, option bytes, security state, calibration, serial numbers, or
  provisioning data.
- Running scripts that move hardware, actuate outputs, write production memory,
  or affect connected equipment.
- Connecting to external services, lab infrastructure, or shared benches.

Prefer read-only inspection first: logs, register dumps, build artifacts,
map files, traces, simulator output, or debugger snapshots.

## 4. Preserve Generated And Vendor Boundaries

Do not directly edit generated, vendored, or third-party code unless the project
uses that as the source of truth. Change the generator input, configuration, or
wrapper layer when possible.

Watch for:

- `generated`, `autogen`, `do not edit`, `*.g.*`, `build`, `dist`.
- HAL packs, SDKs, BSPs, vendor drops, and third-party middleware.
- Lock files, generated register maps, protocol headers, and calibration blobs.

## 5. Verify On The Right Layer

Choose verification proportional to risk:

1. Host unit test or static analysis.
2. Cross-compile for the affected target.
3. Link/map inspection for memory or symbol changes.
4. Simulator or emulator run.
5. Hardware run with explicit approval when needed.
6. Log, trace, UART, JTAG/SWD, or debugger evidence.

When hardware is unavailable, disclose the missing target verification and list
the strongest substitute that was run.

## 6. Report Embedded Results

Include:

- Target or board assumed.
- Toolchain/build command used.
- Whether the result is host, simulator, or hardware evidence.
- Any operations intentionally not run because they require approval or lab access.

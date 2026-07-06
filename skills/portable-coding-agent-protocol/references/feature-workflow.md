# Feature Workflow

Use this module when adding or changing behavior.

## 1. Split By Observable Behavior

Break the request into user-visible or caller-visible behavior units:

- Inputs and outputs.
- Success path.
- Empty, boundary, and error paths.
- Persistence, network, hardware, or timing effects.
- Reporting, logging, or UI state if requested.

Implement in an order that leaves the project working after each meaningful
step.

## 2. Match The Existing Shape

Follow the closest existing implementation from entry point to response:

- Routing or command registration.
- Service, handler, controller, or driver boundaries.
- Data models and serialization.
- Error handling and status codes.
- Tests and fixtures.

Do not introduce new framework patterns unless the project already uses them or
the requested feature cannot be implemented safely otherwise.

## 3. Guard Against Scope Creep

Do not add unrequested options, caching, settings, telemetry, retries, UI flows,
permissions, or abstractions. If they look useful, mention them as discovered
follow-ups instead of adding them to the diff.

Use project defaults when a choice is conventional. Ask only when the choice
changes the behavior contract or creates external side effects.

## 4. Define Feature Verification

Verify at least:

- One normal path.
- One boundary or error path when relevant.
- The command, API, UI, hardware, or integration path the user will exercise.

Use tests if the project has them; otherwise run a minimal observable path.

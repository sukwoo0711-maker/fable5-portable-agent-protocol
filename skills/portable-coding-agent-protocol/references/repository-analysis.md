# Repository Analysis

Use this module when the user asks to understand a repository, evaluate an
architecture, plan migration, review operating instructions, or identify likely
implementation points before coding.

## Analysis Mode

When the request is analysis-only, do not apply fixes. The deliverable is a
grounded assessment with file references, confidence labels, and explicit
unknowns.

Analysis should inspect:

- Repository entry points and project instructions.
- Build, test, package, and CI manifests.
- Main source layout and ownership boundaries.
- Existing patterns for the requested topic.
- Recent changes or local diffs when relevant.
- Tests or fixtures that exercise the area.

## Output Shape

Report:

- Answer or recommendation.
- Evidence inspected.
- Assumptions and confidence.
- Risks or missing checks.
- Concrete next implementation step, if requested.

Do not turn analysis into implementation unless the user asked for changes or
the request clearly authorizes a reversible local edit.

## Lower-Model Guard

For lower-capability models, require at least two independent evidence points
before making a broad repository claim. If the repository is large, sample by
module boundary and label conclusions as partial.

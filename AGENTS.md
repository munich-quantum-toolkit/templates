# MQT Templates Agent Guide

## Scope and Validation

- Template sources are in `templates/`; rendering logic is in
  `src/mqt/templates/`; rendering tests are in `tests/`.
- Update template sources rather than generated files in `docs/` or `.github/`.
  The repository's templating workflow regenerates those consumers.
- Install the package with `uv sync`.
- Run tests with `uv run pytest`.
- Run changed-file checks with `uv run prek run --files <paths>`; run
  `uv run prek run --all-files` before handoff when practical.
- Follow `docs/ai_usage.md` as the current contribution-level disclosure and
  attribution policy. Do not duplicate its requirements in this operational
  guide.

## Template Changes

- Keep rendered policy text consistent across `templates/AGENTS.md`,
  `templates/ai_usage.md`, `templates/docs_contributing.md`, and
  `templates/pull_request_template.md` when changing AI contribution rules.
- Keep rendering tests focused on representative end-to-end behavior. Verify
  which files are rendered and that formatting and lint checks leave them
  unchanged. Do not add assertions that merely repeat template content or
  implementation logic.
- Write changelog entries from this repository's perspective: describe how the
  templates or rendered output changed. For example, when changing guidance,
  write `Document Python 3.11+`, not `Require Python 3.11+`.
- Preserve the generated-file headers in template output.

## Release Preparation

This repository uses manual static versioning; it does not use `setuptools_scm`
or another automatic versioning tool. A release-preparation PR must:

- Set `[project].version` in `pyproject.toml` to the release version.
- Run `uv lock` and include the matching `mqt-templates` version update in
  `uv.lock`.
- Move the relevant entries from `CHANGELOG.md`'s `Unreleased` section into a
  dated `## [x.y.z]` section. Each entry must link to its PR and every
  contributor, for example `([#123]) ([**@username**])`; define those links at
  the bottom of the file.
- Add or finalize the corresponding `UPGRADING.md` section and update the
  changelog and upgrade-guide version links.
- Use the release title `🔖 Prepare release of \`vX.Y.Z\`` and verify the
  Release Drafter draft proposes the same version after the PR is merged.
- Do not create or publish the Git tag or GitHub release unless the human has
  explicitly authorized that external action.

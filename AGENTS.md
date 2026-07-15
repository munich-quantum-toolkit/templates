# MQT Templates Agent Guide

## Scope and Validation

- Template sources are in `templates/`; rendering logic is in
  `src/mqt/templates/`; rendering tests are in `tests/`.
- Update template sources rather than generated files in `docs/` or `.github/`.
  The repository's templating workflow regenerates those consumers.
- Set up the test environment with `uv sync --group test`.
- Run tests with `uv run --group test python -m pytest`.
- Run changed-file checks with `uv run prek run --files <paths>`; run
  `uv run prek run --all-files` before handoff when practical.
- Follow `docs/ai_usage.md` and include
  `Assisted-by: [Model Name] via [Tool Name]` in every AI-assisted commit.

## Template Changes

- Keep rendered policy text consistent across `templates/AGENTS.md`,
  `templates/ai_usage.md`, `templates/docs_contributing.md`, and
  `templates/pull_request_template.md` when changing AI contribution rules.
- Add or update rendering tests for every template behavior change, including
  synchronization flags and project-type variants.
- Preserve the generated-file headers in template output. Do not hand-edit the
  generated consumers in this repository.

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

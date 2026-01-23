# Upgrade Guide

This document describes breaking changes and how to upgrade. For a complete list of changes, including minor and patch releases, please refer to the [changelog](CHANGELOG.md).

## [Unreleased]

While not a breaking change, with this release, the action will only create a pull request once it runs on `main`.
On all other branches, the action outputs `git diff` to the terminal.

## [1.1.3]

This release includes two non-breaking changes:

- A `has-changelog-and-upgrade-guide` flag has been added to make the templates more generic.
  If this flag is disabled, respective sections in templates such as `pull_request_template.md` are omitted.
- `other` has been added as a `project_type`.
  For this project type, the contribution and installation guides cannot be synchronized.

## [1.1.0]

With this release, the templating action has new required inputs:

- The `name` is the stylized name of the package (e.g., "Core" or "DDSIM").
- The `project_type` specifies whether the project has C++ components.
  The options are `c++-python` or `pure-python`.

The release adds support for templating several new files.
By default, the templating is enabled for all the added files.
This behavior can be controlled using the following flags:

- `synchronize-contribution-xguide`: Whether to synchronize `.github/CONTRIBUTING.md` and `docs/contributing.md`
- `synchronize-documentation-utilities`: Whether to synchronize documentation utilities such as `docs/_templates/page.html` and `docs/_static/custom.css`
- `synchronize-installation-guide`: Whether to synchronize `docs/installing.md`
- `synchronize-release-drafter-template`: Whether to synchronize `.github/release-drafter.yml`
- `synchronize-renovate-config`: Whether to synchronize `.github/renovate.json5`
- `synchronize-support-resources`: Whether to synchronize `.github/SUPPORT.md` and `docs/support.md`

The categories of the Release Drafter can be configured using `release-drafter-categories`.
If not provided, the default categories are used.

See below for an exemplary action configuration:

```yaml
jobs:
  render-template:
    name: Render template
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      # ...
      - uses: munich-quantum-toolkit/templates@v1.1.0
        with:
          token: <...>
          name: Core
          organization: munich-quantum-toolkit
          project-type: c++-python
          repository: core
          # If desired, the default Release Drafter categories can be overwritten
          release-drafter-categories: <...>
          # If desired, templating a file can be disabled
          synchronize-renovate-config: false
```

<!-- Version links -->

[unreleased]: https://github.com/munich-quantum-toolkit/templates/compare/v1.1.3...HEAD
[1.1.3]: https://github.com/munich-quantum-toolkit/templates/compare/v1.1.0...v1.1.3
[1.1.0]: https://github.com/munich-quantum-toolkit/templates/compare/v1.0.0...HEAD

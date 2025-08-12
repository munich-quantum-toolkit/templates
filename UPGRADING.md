# Upgrade Guide

This document describes breaking changes and how to upgrade. For a complete list of changes, including minor and patch releases, please refer to the [changelog](CHANGELOG.md).

## [Unreleased]

With this release, the templating Action has new required inputs:

- The `name` is the stylized name of the package (e.g., "Core" or "DDSIM").
- The `project_type` specifies whether the project has C++ components.
  The choices are `cpp` or `python`.

<!-- Version links -->

[unreleased]: https://github.com/munich-quantum-toolkit/templates/compare/v1.0.0...HEAD

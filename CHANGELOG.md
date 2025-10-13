<!-- Entries in each category are sorted by merge time, with the latest PRs appearing first. -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on a mixture of [Keep a Changelog] and [Common Changelog].
This project adheres to [Semantic Versioning], with the exception that minor releases may include breaking changes.

## [Unreleased]

## [1.1.9] - 2025-10-13

### Fixed

- 🐛 Fix working directory of action ([#102]) ([**@denialhaag**])

## [1.1.8] - 2025-10-13

### Fixed

- 🐛 Fix call of templating script in action ([#100]) ([**@denialhaag**])

## [1.1.7] - 2025-10-11

### Added

- ✅ Add tests checking that templates render correctly ([#67]) ([**@denialhaag**])

### Changed

- 👷 Use `pep440` versioning for all `pre-commit` dependencies ([#90]) ([**@denialhaag**])
- 📝 Mention `macos-15-intel` runner in contribution guide ([#79]) ([**@denialhaag**])

## [1.1.6] - 2025-09-08

### Changed

- 🎨 Use `pinGitHubActionDigestsToSemver` helper in Renovate configuration ([#66]) ([**@denialhaag**])
- 🎨 Improve wording in installation guide ([#66]) ([**@denialhaag**])

## [1.1.5] - 2025-09-02

### Changed

- 🎨 Improve Renovate configuration ([#59]) ([**@denialhaag**])

## [1.1.4] - 2025-09-02

### Fixed

- 🐛 Allow `name` to contain whitespace character ([#58]) ([**@denialhaag**])

### Changed

- 🎨 Improve wording in issue templates ([#57]) ([**@denialhaag**])

## [1.1.3] - 2025-09-02

_If you are upgrading: please see [`UPGRADING.md`](UPGRADING.md#113)._

### Added

- 🎨 Add `has_changelog_and_upgrade_guide` flag to make templates more generic ([#55]) ([**@denialhaag**])
- 🎨 Add `other` as possible `project_type` ([#54]) ([**@denialhaag**])

### Changed

- 🎨 Add `hpca` key to `lit_header.bib` ([#53]) ([**@denialhaag**])

## [1.1.2] - 2025-09-01

### Fixed

- 🐛 Fix whitespace in installation guide ([#51]) ([**@denialhaag**])

## [1.1.1] - 2025-09-01

### Fixed

- 🐛 Fix whitespaces in rendered templates ([#50]) ([**@denialhaag**])

## [1.1.0] - 2025-08-28

_If you are upgrading: please see [`UPGRADING.md`](UPGRADING.md#110)._

### Added

- ✨ Synchronize documentation utilities such as `page.html` and `custom.css` ([#45]) ([**@denialhaag**])
- ✨ Synchronize contribution guide ([#31]) ([**@denialhaag**], [**@burgholzer**])
- ✨ Synchronize installation guide ([#31]) ([**@denialhaag**], [**@burgholzer**])
- ✨ Synchronize Renovate config ([#25]) ([**@denialhaag**])
- ✨ Synchronize Release Drafter template ([#24]) ([**@denialhaag**])
- ✨ Synchronize support resources ([#23]) ([**@denialhaag**])
- ✨ Synchronize issue templates ([#21]) ([**@denialhaag**])

### Changed

- 🚚 Rename `support.md` to `SUPPORT.md` ([#31]) ([**@denialhaag**])

### Fixed

- 🐛 Fix emojis in Renovate config ([#32]) ([**@denialhaag**])

## [1.0.0] - 2025-07-09

### Added

- 👷 Add initial version of action ([#1]) ([**@denialhaag**])

### Removed

- 🔥 Drop support for custom changes ([#13]) ([**@denialhaag**])

<!-- Version links -->

[unreleased]: https://github.com/munich-quantum-toolkit/templates/compare/v1.1.9...HEAD
[1.1.9]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.9
[1.1.8]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.8
[1.1.7]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.7
[1.1.6]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.6
[1.1.5]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.5
[1.1.4]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.4
[1.1.3]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.3
[1.1.2]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.2
[1.1.1]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.1
[1.1.0]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.1.0
[1.0.0]: https://github.com/munich-quantum-toolkit/templates/releases/tag/v1.0.0

<!-- PR links -->

[#102]: https://github.com/munich-quantum-toolkit/templates/pull/102
[#100]: https://github.com/munich-quantum-toolkit/templates/pull/100
[#90]: https://github.com/munich-quantum-toolkit/templates/pull/90
[#79]: https://github.com/munich-quantum-toolkit/templates/pull/79
[#67]: https://github.com/munich-quantum-toolkit/templates/pull/67
[#66]: https://github.com/munich-quantum-toolkit/templates/pull/66
[#59]: https://github.com/munich-quantum-toolkit/templates/pull/59
[#58]: https://github.com/munich-quantum-toolkit/templates/pull/58
[#57]: https://github.com/munich-quantum-toolkit/templates/pull/57
[#55]: https://github.com/munich-quantum-toolkit/templates/pull/55
[#54]: https://github.com/munich-quantum-toolkit/templates/pull/54
[#53]: https://github.com/munich-quantum-toolkit/templates/pull/53
[#51]: https://github.com/munich-quantum-toolkit/templates/pull/51
[#50]: https://github.com/munich-quantum-toolkit/templates/pull/50
[#45]: https://github.com/munich-quantum-toolkit/templates/pull/45
[#32]: https://github.com/munich-quantum-toolkit/templates/pull/32
[#31]: https://github.com/munich-quantum-toolkit/templates/pull/31
[#25]: https://github.com/munich-quantum-toolkit/templates/pull/25
[#24]: https://github.com/munich-quantum-toolkit/templates/pull/24
[#23]: https://github.com/munich-quantum-toolkit/templates/pull/23
[#21]: https://github.com/munich-quantum-toolkit/templates/pull/21
[#13]: https://github.com/munich-quantum-toolkit/templates/pull/13
[#1]: https://github.com/munich-quantum-toolkit/templates/pull/1

<!-- Contributor -->

[**@burgholzer**]: https://github.com/burgholzer
[**@denialhaag**]: https://github.com/denialhaag

<!-- General links -->

[Keep a Changelog]: https://keepachangelog.com/en/1.1.0/
[Common Changelog]: https://common-changelog.org
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
[GitHub Release Notes]: https://github.com/munich-quantum-toolkit/templates/releases

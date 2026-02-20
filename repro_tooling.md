<!--- This file has been generated from an external template. Please do not modify it directly. -->
<!--- Changes should be contributed to https://github.com/munich-quantum-toolkit/templates. -->

# Tooling

This page summarizes the main tools, software, and standards used in MQT Test.
It serves as a quick reference for new contributors and users who want to understand the project's ecosystem.

## Python

<!-- prettier-ignore -->
| Tool           | Description                                                                              | Links / Notes                                                                                                                                                                       |
| -------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **uv**         | Fast Python package and project manager (install, venv, dependencies).                   | [Documentation](https://docs.astral.sh/uv/). Recommended over {code}`pip` for installs and development.                                                                  |
| **nox**        | Task automation for tests, lint, docs, and other sessions defined in {code}`noxfile.py`. | [Documentation](https://nox.thea.codes/en/stable/). Run sessions with {code}`nox -s <session>`.                                                                          |
| **pre-commit** | Runs hooks (formatting, linting) before each commit.                                     | [Documentation](https://pre-commit.com/). Recommended: install and run via [prek](https://prek.j178.dev) ({code}`prek install`, {code}`prek run`); alternative: {code}`pre-commit`. |
| **ruff**       | Linter and formatter for Python, written in Rust.                                        | [Documentation](https://docs.astral.sh/ruff/). Used in pre-commit and CI.                                                                                                |
| **ty**         | Static type checker for Python (Astral).                                                 | [Documentation](https://docs.astral.sh/ty/).                                                                                                                             |
| **pytest**     | Testing framework for Python.                                                            | [Documentation](https://docs.pytest.org/). Run via {code}`nox -s tests` or {code}`pytest`.                                                                               |

<!-- prettier-ignore -->
| Tool         | Description                                          | Links / Notes                                                                                                                             |
| ------------ | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **nanobind** | C++/Python bindings (exposes C++ library to Python). | [Documentation](https://nanobind.readthedocs.io/). Bindings live in {code}`bindings`; stubs are auto-generated (see {doc}`contributing`). |

## Build and documentation

<!-- prettier-ignore -->
| Tool       | Description                                | Links / Notes                                                                               |
| ---------- | ------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **CMake**  | Build configuration (configure + build).   | [Documentation](https://cmake.org/documentation/). Requires 3.24 or newer.                  |
| **Sphinx** | Documentation generator.                   | [Documentation](https://www.sphinx-doc.org/). Docs source in {code}`docs/`.                 |
| **MyST**   | Markdown flavor for Sphinx (used in docs). | [Documentation](https://myst-parser.readthedocs.io/). Enables rich Markdown in doc sources. |

## C++

<!-- prettier-ignore -->
| Tool             | Description                          | Links / Notes                                                                                                 |
| ---------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **clang-format** | Code formatter (LLVM style).         | [Documentation](https://clang.llvm.org/docs/ClangFormat.html). Config: {code}`.clang-format` in project root. |
| **clang-tidy**   | Static analysis and linting for C++. | [Documentation](https://clang.llvm.org/extra/clang-tidy/). Config: {code}`.clang-tidy` in project root.       |
| **Doxygen**      | C++ API documentation (comments).    | [Documentation](https://www.doxygen.nl/). Rendered in Sphinx via [breathe](https://breathe.readthedocs.io/).  |
| **GoogleTest**   | C++ unit testing.                    | [Primer](https://google.github.io/googletest/primer.html). Tests in {code}`test/`; run via CTest.             |

## CI and quality

<!-- prettier-ignore -->
| Tool               | Description                                 | Links / Notes                                                                                                                     |
| ------------------ | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **GitHub Actions** | CI workflows (build, test, lint, coverage). | Workflows in {code}`.github/workflows/`; see [Actions](https://github.com/munich-quantum-toolkit/test/actions).               |
| **Codecov**        | Code coverage reporting.                    | [Codecov for this repo](https://codecov.io/gh/munich-quantum-toolkit/test).                                               |
| **CodeRabbit**     | Automated code review on PRs.               | [CodeRabbit app](https://github.com/apps/coderabbit). See the section _Working with CodeRabbit_ in the {doc}`contributing` guide. |
| **pre-commit.ci**  | Runs pre-commit in CI and can auto-fix.     | [pre-commit.ci](https://pre-commit.ci).                                                                                           |

## Standards and conventions

- **Commit messages**: Prefer [gitmoji](https://gitmoji.dev) for context.
- **Changelog / versioning**: Projects may follow [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/). When present, see the project's changelog and upgrade guide in the documentation.
- **Python style**: Google-style docstrings; type hints for public APIs.
- **C++ style**: [LLVM Coding Standard](https://llvm.org/docs/CodingStandards.html); enforced via clang-format and clang-tidy.

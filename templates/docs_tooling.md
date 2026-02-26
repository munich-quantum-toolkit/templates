<!--- This file has been generated from an external template. Please do not modify it directly. -->
<!--- Changes should be contributed to https://github.com/munich-quantum-toolkit/templates. -->

# Tooling

This page summarizes the main tools, software, and standards used in MQT {{name}}.
It serves as a quick reference for new contributors and users who want to understand the project's ecosystem.

## Python

| Tool       | Description                                                                              | Links / Notes                                                                                                                                          |
| ---------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **uv**     | Fast Python package and project manager (install, venv, dependencies).                   | [Documentation](https://docs.astral.sh/uv/). Recommended over {code}`pip` for installs and development.                                                |
| **nox**    | Task automation for tests, lint, docs, and other sessions defined in {code}`noxfile.py`. | [Documentation](https://nox.thea.codes/en/stable/). Run sessions with {code}`nox -s <session>`.                                                        |
| **prek**   | Runs hooks (formatting, linting) before each commit.                                     | [Documentation](https://prek.j178.dev). Install and run via {code}`prek install`, {code}`prek run` (staged files), or {code}`prek run -a` (all files). |
| **ruff**   | Linter and formatter for Python, written in Rust.                                        | [Documentation](https://docs.astral.sh/ruff/). Used in prek and CI.                                                                                    |
| **ty**     | Static type checker for Python (Astral).                                                 | [Documentation](https://docs.astral.sh/ty/).                                                                                                           |
| **pytest** | Testing framework for Python.                                                            | [Documentation](https://docs.pytest.org/). Run via {code}`nox -s tests` or {code}`pytest`.                                                             |

{%- if project_type in ["c++-python", "c++-mlir-python"] %}

## C++/Python Bindings

| Tool         | Description                                          | Links / Notes                                                                                                                             |
| ------------ | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **nanobind** | C++/Python bindings (exposes C++ library to Python). | [Documentation](https://nanobind.readthedocs.io/). Bindings live in {code}`bindings`; stubs are auto-generated (see {doc}`contributing`). |

{%- endif %}

## Build and documentation

| Tool       | Description                                | Links / Notes                                                                               |
| ---------- | ------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **Sphinx** | Documentation generator.                   | [Documentation](https://www.sphinx-doc.org/). Docs source in {code}`docs/`.                 |
| **MyST**   | Markdown flavor for Sphinx (used in docs). | [Documentation](https://myst-parser.readthedocs.io/). Enables rich Markdown in doc sources. |

{%- if project_type in ["c++-python", "c++-mlir-python"] %}

## C++

| Tool             | Description                          | Links / Notes                                                                                                 |
| ---------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **clang-format** | Code formatter (LLVM style).         | [Documentation](https://clang.llvm.org/docs/ClangFormat.html). Config: {code}`.clang-format` in project root. |
| **clang-tidy**   | Static analysis and linting for C++. | [Documentation](https://clang.llvm.org/extra/clang-tidy/). Config: {code}`.clang-tidy` in project root.       |
| **Doxygen**      | C++ API documentation (comments).    | [Documentation](https://www.doxygen.nl/). Rendered in Sphinx via [breathe](https://breathe.readthedocs.io/).  |
| **GoogleTest**   | C++ unit testing.                    | [Primer](https://google.github.io/googletest/primer.html). Tests in {code}`test/`; run via CTest.             |

{%- if project_type == "c++-mlir-python" %}
| **LLVM/MLIR** | Compiler framework providing MLIR dialects and infrastructure. | Obtained via [setup-mlir](https://github.com/munich-quantum-toolkit/setup-mlir). Required for all MLIR-based builds. |
{%- endif %}
{%- endif %}

## CI and Quality

| Tool               | Description                                 | Links / Notes                                                                                                                     |
| ------------------ | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **GitHub Actions** | CI workflows (build, test, lint, coverage). | Workflows in {code}`.github/workflows/`; see [Actions](https://github.com/{{organization}}/{{repository}}/actions).               |
| **Codecov**        | Code coverage reporting.                    | [Codecov for this repo](https://codecov.io/gh/{{organization}}/{{repository}}).                                                   |
| **CodeRabbit**     | Automated code review on PRs.               | [CodeRabbit app](https://github.com/apps/coderabbit). See the section _Working with CodeRabbit_ in the {doc}`contributing` guide. |
| **pre-commit.ci**  | Runs pre-commit in CI and can auto-fix.     | [pre-commit.ci](https://pre-commit.ci).                                                                                           |

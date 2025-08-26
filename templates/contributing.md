<!--- This file has been generated from an external template. Please do not modify it directly. -->
<!--- Changes should be contributed to https://github.com/munich-quantum-toolkit/templates. -->

# Contributing

Thank you for your interest in contributing to MQT {{name}}!
This document lays out development guidelines but also acts as a development guide.

We use GitHub to [host code](https://github.com/{{organization}}/{{repository}}), to [track issues and feature requests][issues], as well as accept [pull requests](https://github.com/{{organization}}/{{repository}}/pulls).
See <https://docs.github.com/en/get-started/quickstart> for a general introduction to working with GitHub and contributing to projects.

## Types of Contributions

You can contribute in several ways:

- 🐛 Report Bugs:
  Report bugs at <https://github.com/{{organization}}/{{repository}}/issues> using the _🐛 Bug report_ issue template.
  Please make sure to fill out all relevant information in the respective issue form.

- 🐛 Fix Bugs:
  Look through the [GitHub Issues][issues] for bugs.
  Anything tagged with "bug" is open to whoever wants to try and fix it.

- ✨ Propose New Features:
  Propose new features at <https://github.com/{{organization}}/{{repository}}/issues> using the _✨ Feature request_ issue template.
  Please make sure to fill out all relevant information in the respective issue form.

- ✨ Implement New Features:
  Look through the [GitHub Issues][issues] for features.
  Anything tagged with "feature" or "enhancement" is open to whoever wants to implement it.
  We highly appreciate external contributions to the project.

- 📝 Write Documentation:
  MQT {{name}} could always use some more documentation, and we appreciate any help with that.

## Guidelines

This section lays out some guidelines for contributing to MQT {{name}}.
It is important that we all adhere to them to ensure that the project can grow sustainably.

### Core Guidelines

- ["Commit early and push often"](https://www.worklytics.co/blog/commit-early-push-often).
- Write meaningful commit messages, preferably using [gitmoji](https://gitmoji.dev) for additional context.
- Focus on a single feature or bug at a time and only touch relevant files.
  Split multiple features into separate contributions.
- Add tests for new features to ensure they work as intended.
- Document new features appropriately.
  For user-facing changes, add an entry to the changelog.
  In case of breaking changes, please also update the upgrade guide.
- Add tests for bug fixes to demonstrate that the bug has been resolved.
- Document your code thoroughly and ensure it is readable.
- Keep your code clean by removing debug statements, leftover comments, and unrelated code.
- Check your code for style and linting errors before committing.
- Follow the project's coding standards and conventions.
- Be open to feedback and willing to make necessary changes based on code reviews.

### Pull Request Workflow

- Create PRs early.
  It is ok to create work-in-progress PRs.
  You may mark these as draft PRs on GitHub.
- Describe your PR with a descriptive title, reference any related issues by including the issue number in the PR description, and add a comprehensive description of the changes.
  Follow the provided PR template and do not delete any sections, except for the issue reference if your PR is not related to an issue.
- Whenever a PR is created or updated, several workflows on all supported platforms and versions of Python are executed.
  These workflows ensure that the project still builds, all tests pass, the code is properly formatted, and no new linting errors are introduced.
  Your PR must pass all these continuous integration (CI) checks before it can be merged.
- Once your PR is ready, change it from a draft PR to a regular PR and request a review from one of the project maintainers.
  Only request a review once you are done with your changes and the PR is ready to be reviewed.
  If you are unsure whether your PR is ready, ask in the PR comments.
  If you are a first-time contributor, request a review from one of the maintainers by mentioning them in a comment on the PR.
- If your PR gets a "Changes requested" review, address the feedback and update your PR by pushing to the same branch.
  Do not close the PR and open a new one.
  Respond to review comments on the PR (e.g., with "Done. 👍" or "Done in @<commit>.") to let the reviewer know that you have addressed the feedback
  Note that reviewers do not get a notification if you just react to the review comment with an emoji.
  Write a comment to notify the reviewer.
  Do not resolve the review comments yourself.
  The reviewer will mark the comments as resolved once they are satisfied with the changes.
- Be sure to rerequest a review once you have made changes after a code review so that maintainers know that the requests have been addressed.
- Please do not squash commits before merging; we usually squash them to keep the history clean.
  We only merge without squashing if the commit history is clean and meaningful.
  Avoid rebasing or force-pushing your PR branch before merging, as it complicates reviews.
  You can rebase or clean up commits after addressing all review comments if desired.

## Get Started 🎉

Ready to contribute?
We value contributions from people with all levels of experience.
In particular, if this is your first PR, not everything has to be perfect.
We will guide you through the process.

## Installation

Check out our [installation guide for developers](https://mqt.readthedocs.io/projects/{{repository}}/en/latest/installation.html) for instructions on how to set up your development environment.

{%- if project_type == "c++-python" %}

## Working on the C++ Library

Building the project requires a C++ compiler supporting _C++20_ and CMake with a minimum version of _3.24_.
As of August 2025, our CI pipeline on GitHub continuously tests the library under a wide matrix of systems and compilers:

- `ubuntu-24.04`: `Release` and `Debug` builds using `gcc`
- `ubuntu-24.04-arm`: `Release` build using `gcc`
- `macos-14`: `Release` and `Debug` builds using `AppleClang`
- `macos-13`: `Release` build using `AppleClang`
- `windows-2022`: `Release` and `Debug` builds using `msvc`
- `windows-11-arm`: `Release` build using `msvc`

To access the latest build logs, visit the [GitHub Actions page](https://github.com/{{organization}}/{{repository}}/actions/workflows/ci.yml).

Additionally, we regularly run extensive tests with an even wider matrix of compilers and operating systems.
We are not aware of any issues with other compilers or operating systems.
If you encounter any problems, please [open an issue][issues] and let us know.

### Configure and Build

> [!TIP]
> We recommend using an IDE like [CLion][clion] or [Visual Studio Code][vscode] for development.
> Both IDEs have excellent support for CMake projects and provide a convenient way to run CMake and build the project.
> If you prefer to work on the command line, the following instructions will guide you through the process.

Our projects use _CMake_ as the main build configuration tool.
Building a project using CMake is a two-stage process.
First, CMake needs to be _configured_ by calling:

```console
$ cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
```

This tells CMake to:

- search the current directory `.` (passed via `-S`) for a `CMakeLists.txt` file,
- process it into a directory `build` (passed via `-B`), and
- configure a `Release` build (passed via `-DCMAKE_BUILD_TYPE`) as opposed to, e.g., a _Debug_ build.

After configuring CMake, the project can be built by calling:

```console
$ cmake --build build --config Release
```

This tries to build the project in the `build` directory (passed via `--build`).
Some operating systems and development environments explicitly require a configuration to be set, which is why the `--config` flag is also passed to the build command.
The flag `--parallel <NUMBER_OF_THREADS>` may be added to trigger a parallel build.

Building the project this way generates:

- the main project libraries in the `build/src` directory and
- some test executables in the `build/test` directory.

> [!NOTE]
> This project uses CMake's [`FetchContent`](https://cmake.org/cmake/help/latest/module/FetchContent.html) module to download and build its dependencies.
> Because of this, the first time you configure the project, you'll need an active internet connection to fetch the required libraries.
>
> However, there are several ways to bypass these downloads:
>
> - **Use system-installed dependencies**:
>   If the dependencies are already installed on your system and Find-modules exist for them, `FetchContent` will use those versions instead of downloading them.
> - **Provide a local copy**:
>   If you have local copies of the dependencies (from a previous build or another project), you can point `FetchContent` to them by passing the [`-DFETCHCONTENT_SOURCE_DIR_<uppercaseName>`](https://cmake.org/cmake/help/latest/module/FetchContent.html#variable:FETCHCONTENT_SOURCE_DIR_%3CuppercaseName%3E) flag to your CMake configure step.
>   The `<uppercaseName>` should be replaced with the name of the dependency as specified in the project's CMake files.
> - **Use project-specific options**:
>   Some projects provide specific CMake options to use a system-wide dependency instead of downloading it.
>   Check the project's documentation or CMake files for these types of flags.

### Running the C++ Tests and Code Coverage

We use the [GoogleTest](https://google.github.io/googletest/primer.html) framework for unit testing of the C++ library.
All tests are contained in the `test` directory, which is further divided into subdirectories for different parts of the library.
You are expected to write tests for any new features you implement and ensure that all tests pass.
Our CI pipeline on GitHub will also run the tests and check for any failures.
It will also collect code coverage information and upload it to [Codecov](https://codecov.io/gh/{{organization}}/{{repository}}).
Our goal is to have new contributions at least maintain the current code coverage level, while striving for covering as much of the code as possible.
Try to write meaningful tests that actually test the correctness of the code and not just exercise the code paths.

Most IDEs like [CLion][clion] or [Visual Studio Code][vscode] provide a convenient way to run the tests directly from the IDE.
If you prefer to run the tests from the command line, you can use CMake's test runner [CTest](https://cmake.org/cmake/help/latest/manual/ctest.1.html).
To run the tests, call:

```console
$ ctest -C Release --test-dir build
```

from the main project directory after building the project as described above.

> [!TIP]
> If you want to disable configuring and building the C++ tests, you can pass `-DBUILD_MQT_{{name.upper()}}_TESTS=OFF` to the CMake configure step.

### C++ Code Formatting and Linting

This project mostly follows the [LLVM Coding Standard](https://llvm.org/docs/CodingStandards.html), which is a set of guidelines for writing C++ code.
To ensure the quality of the code and that it conforms to these guidelines, we use:

- [`clang-tidy`](https://clang.llvm.org/extra/clang-tidy/), a static analysis tool that checks for common mistakes in C++ code, and
- [`clang-format`](https://clang.llvm.org/docs/ClangFormat.html), a tool that automatically formats C++ code according to a given style guide.

Common IDEs like [CLion][clion] or [Visual Studio Code][vscode] have plugins that can automatically run `clang-tidy` on the code and automatically format it with `clang-format`.

- If you are using CLion, you can configure the project to use the `.clang-tidy` and `.clang-format` files in the project root directory.
- If you are using Visual Studio Code, you can install the [clangd extension](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd).

They will automatically execute `clang-tidy` on your code and highlight any issues.
In many cases, they also provide quick-fixes for these issues.
Furthermore, they provide a command to automatically format your code according to the given style.

> [!NOTE]
> After configuring CMake, you can run `clang-tidy` on a file by calling the following command:
>
> ```console
> $ clang-tidy <FILE> -- -I <PATH_TO_INCLUDE_DIRECTORY>
> ```
>
> Here, `<FILE>` is the file you want to analyze and `<PATH_TO_INCLUDE_DIRECTORY>` is the path to the `include` directory of the project.

Our `pre-commit` configuration also includes `clang-format`.
If you have installed `pre-commit`, it will automatically run `clang-format` on your code before each commit.
If you do not have `pre-commit` set up, the [pre-commit.ci](https://pre-commit.ci) bot will run `clang-format` on your code and automatically format it according to the style guide.

> [!TIP]
> Remember to pull the changes back into your local repository after the bot has formatted your code to avoid merge conflicts.

Our CI pipeline will also run `clang-tidy` over the changes in your PR and report any issues it finds.
Due to technical limitations, the workflow can only post PR comments if the changes are not coming from a fork.
If you are working on a fork, you can still see the `clang-tidy` results either in the GitHub Actions logs, on the workflow summary page, or in the "Files changed" tab of the PR.

### C++ Documentation

Historically, the C++ part of the code base has not been sufficiently documented.
Given the substantial size of the code base, we have set ourselves the goal to improve the documentation over time.
We expect any new additions to the code base to be documented using [Doxygen](https://www.doxygen.nl/index.html) comments.
When touching existing code, we encourage you to add Doxygen comments to the code you touch or refactor.

For some tips on how to write good Doxygen comments, see the [Doxygen Manual](https://www.doxygen.nl/manual/docblocks.html).

The C++ API documentation is integrated into the overall documentation that we host on ReadTheDocs using the [breathe](https://breathe.readthedocs.io/en/latest/) extension for Sphinx.
See the [Working on the Documentation](#working-on-the-documentation) section for more information on how to build the documentation.

{%- endif %}

{%- if project_type == "c++-python" %}

## Working on the Python Package

We use [`pybind11`](https://pybind11.readthedocs.io/en/stable) to expose large parts of the C++ core library to Python.
This allows us to keep the performance-critical parts of the code in C++ while providing a convenient interface for Python users.
All code related to C++-Python bindings is contained in the `bindings` directory.

> [!TIP]
> If you just want to build the Python bindings themselves, you can pass `-DBUILD_MQT_{{name.upper()}}_BINDINGS=ON` to the CMake configure step.
> CMake will then try to find Python and the necessary dependencies (`pybind11`) on your system and configure the respective targets.
> In [CLion][clion], you can enable an option to pass the current Python interpreter to CMake.
> Go to `Preferences` -> `Build, Execution, Deployment` -> `CMake` -> `Python Integration` and check the box `Pass Python Interpreter to CMake`.
> Alternatively, you can pass `-DPython_ROOT_DIR=<PATH_TO_PYTHON>` to the configure step to point CMake to a specific Python installation.

The Python package itself lives in the `python/mqt/{{repository}}` directory.

{%- elif project_type == "pure-python" %}

## Working on the Package

The package lives in the `src/mqt/{{repository}}` directory.

We recommend using [`nox`][nox] for development.
`nox` is a Python automation tool that allows you to define tasks in a `noxfile.py` file and then run them with a single command.
If you have not installed it yet, see our [installation guide](https://mqt.readthedocs.io/projects/{{repository}}/en/latest/installation.html).

We define four convenient `nox` sessions in our `noxfile.py`:

- `tests` to run the Python tests
- `minimums` to run the Python tests with the minimum dependencies
- `lint` to run the Python code formatting and linting
- `docs` to build the documentation

These are explained in more detail in the following sections.

{%- if project_type == "c++-python" %}

## Running the Python Tests

{%- elif project_type == "pure-python" %}

## Running the Tests

{%- endif %}

The Python code is tested by unit tests using the [`pytest`](https://docs.pytest.org/en/latest/) framework.
{%- if project_type == "c++-python" %}
The corresponding test files can be found in the `test/python` directory.
{%- elif project_type == "pure-python" %}
The corresponding test files can be found in the `tests` directory.
{%- endif %}
A `nox` session is provided to conveniently run the Python tests.

```console
$ nox -s tests
```

The above command will automatically build the project and run the tests on all supported Python versions.
For each Python version, it will create a virtual environment (in the `.nox` directory) and install the project into it.
We take extra care to install the project without build isolation so that rebuilds are typically very fast.

If you only want to run the tests on a specific Python version, you can pass the desired Python version to the `nox` command.

```console
$ nox -s tests-3.12
```

> [!NOTE]
> If you do not want to use `nox`, you can also run the tests directly using `pytest`.
> This requires that you have the project and its test dependencies installed in your virtual environment (e.g., by running `uv sync`).
>
> ```console
> (.venv) $ pytest
> ```

We provide an additional nox session `minimums` that makes use of `uv`'s `--resolution=lowest-direct` flag to install the lowest possible versions of the direct dependencies.
This ensures that the project can still be built and the tests pass with the minimum required versions of the dependencies.

```console
$ nox -s minimums
```

{%- if project_type == "c++-python" %}

## Python Code Formatting and Linting

{%- elif project_type == "pure-python" %}

## Code Formatting and Linting

{%- endif %}

The Python code is formatted and linted using a collection of [`pre-commit`][pre-commit] hooks.
This collection includes:

- [ruff][ruff], an extremely fast Python linter and formatter written in Rust, and
- [mypy][mypy], a static type checker for Python code.

The hooks can be installed by running running the following command in the root directory:

```console
$ pre-commit install
```

This will install the hooks in the `.git/hooks` directory of the repository.
The hooks will be executed whenever you commit changes.

You can also run `nox` session `lint` to run the hooks manually.

```console
$ nox -s lint
```

> [!NOTE]
> If you do not want to use `nox`, you can also run the hooks manually by using `pre-commit`.
>
> ```console
> $ pre-commit run --all-files
> ```

{%- if project_type == "c++-python" %}

## Python Documentation

{%- elif project_type == "pure-python" %}

## Documentation

{%- endif %}

The Python code is documented using [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings).
Every public function, class, and module should have a docstring that explains what it does and how to use it.
`ruff` will check for missing docstrings and will explicitly warn you if you forget to add one.

We heavily rely on [type hints](https://docs.python.org/3/library/typing.html) to document the expected types of function arguments and return values.
{%- if project_type == "c++-python" %}
For the compiled parts of the code base, we provide type hints in the form of stub files in the `python/mqt/{{repository}}` directory.
{%- endif %}

The Python API documentation is integrated into the overall documentation that we host on ReadTheDocs using the
[`sphinx-autoapi`](https://sphinx-autoapi.readthedocs.io/en/latest/) extension for Sphinx.

## Working on the Documentation

The documentation is written in [MyST](https://myst-parser.readthedocs.io/en/latest/index.html) (a flavor of Markdown) and built using [Sphinx](https://www.sphinx-doc.org/en/master/).
The documentation source files can be found in the `docs/` directory.

On top of the API documentation, we provide a set of tutorials and examples that demonstrate how to use the library.
These are written in Markdown using [myst-nb](https://myst-nb.readthedocs.io/en/latest/), which allows executing Python code blocks in the documentation.
The code blocks are executed during the documentation build process, and the output is included in the documentation.
This allows us to provide up-to-date examples and tutorials that are guaranteed to work with the latest version of the library.

You can build the documentation using the `nox` session `docs`.

```console
$ nox -s docs
```

This will install all dependencies for building the documentation in an isolated environment, build the Python package, and then build the documentation.
Finally, it will host the documentation on a local web server for you to view.

> [!NOTE]
> If you don't want to use `nox`, you can also build the documentation directly using `sphinx-build`.
> This requires that you have the project and its documentation dependencies installed in your virtual environment (e.g., by running `uv sync`).
>
> ```console
> (.venv) $ sphinx-build -b html docs/ docs/_build
> ```
>
> The docs can then be found in the `docs/_build` directory.

## Tips for Development

If something goes wrong, the CI pipeline will notify you.
Here are some tips for finding the cause of certain failures:

{%- if project_type == "c++-python" %}

- If any of the `CI / 🇨‌ Test` checks fail, this indicates build errors or test failures in the C++ part of the code base.
  Look through the respective logs on GitHub for any error or failure messages.
- If any of the `CI / 🐍 Test` checks fail, this indicates build errors or test failures in the Python part of the code base.
  Look through the respective logs on GitHub for any error or failure messages.

{%- elif project_type == "pure-python" %}

- If any of the `CI / 🐍 Test` checks fail, this indicates build errors or test failures.
  Look through the respective logs on GitHub for any error or failure messages.

{%- endif %}

- If any of the `codecov/\*` checks fail, this means that your changes are not appropriately covered by tests or that the overall project coverage decreased too much.
  Ensure that you include tests for all your changes in the PR.
  {%- if project_type == "c++-python" %}
- If `cpp-linter` comments on your PR with a list of warnings, these have been raised by `clang-tidy` when checking the C++ part of your changes for warnings or style guideline violations.
  The individual messages frequently provide helpful suggestions on how to fix the warnings.
  If you don't see any messages, but the `🇨‌ Lint / 🚨 Lint` check is red, click on the `Details` link to see the full log of the check and a step summary.
  {%- endif %}
- If the `pre-commit.ci` check fails, some of the `pre-commit` checks failed and could not be fixed automatically by the _pre-commit.ci_ bot.
  The individual log messages frequently provide helpful suggestions on how to fix the warnings.
- If the `docs/readthedocs.org:\*` check fails, the documentation could not be built properly.
  Inspect the corresponding log file for any errors.

## Maintaining the Changelog and Upgrade Guide

MQT {{name}} adheres to [Semantic Versioning], with the exception that minor releases may include breaking changes.
To inform users about changes to the project, we maintain a [changelog](https://github.com/{{organization}}/{{repository}}/blob/main/CHANGELOG.md) and an [upgrade guide](https://github.com/{{organization}}/{{repository}}/blob/main/UPGRADING.md).

If your PR includes noteworthy changes, please update the changelog.
The format is based on a mixture of [Keep a Changelog] and [Common Changelog].
There are the following categories:

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

When updating the changelog, follow these guidelines:

- Add a changelog entry for every user-facing change in your PR.
- Write entries in the imperative mood (e.g., "Add support for X" or "Fix bug in Y").
- A single PR may result in multiple changelog entries.
- Entries in each category are sorted by merge time, with the latest PR appearing first.
- Each entry links to the PR and all contributing authors.
  The links are defined at the bottom of the file.
  If this is your first contribution to this project, do not forget to add a link to your GitHub profile.

If your PR introduces major or breaking changes, or if you think additional context would help users, please also add a section to the upgrade guide.
The upgrade guide is intended to provide a general overview of significant changes in a more descriptive and prose-oriented form than the changelog.
Use it to explain how users may need to adapt their usage of MQT {{name}}, highlight new workflows, or clarify the impact of important updates.
Feel free to write in a style that is helpful and accessible for users seeking to understand the broader implications of recent changes.

## Releasing a New Version

When it is time to release a new version of MQT {{name}}, create a PR that prepares the release.
This PR should:

- add new version titles in both the changelog and the upgrade guide,
- add the release date to the changelog entry for the new version,
- update the version links at the bottom of both files,
- review and streamline all changelog and upgrade guide entries for clarity and consistency,
- ensure that all links (to PRs, authors, etc.) are defined and correct,
- double-check that the changelog comprehensively covers all changes since the last release and that nothing is missing,
- review the upgrade guide to ensure it covers all major or breaking changes and provides helpful context, and
- if the upgrade guide contains a section relevant to the release, add a reference to it in the changelog.

Before merging the PR perparing the release, check the GitHub release draft generated by the Release Drafter for unlabelled PRs.
Unlabelled PRs would appear at the top of the release draft below the main heading.
If you missed updating labels before merging, you can still update them and re-run the Release Drafter afterward.
Furthermore, check whether the version number in the release draft is correct.
The version number in the release draft is dictated by the presence of certain labels on the PRs involved in a release.
By default, a patch release will be created.
If any PR has the `minor` or `major` label, a minor or major release will be created, respectively.

> [!NOTE]
> Sometimes, Dependabot or Renovate will tag a PR updating a dependency with a `minor` or `major` label because the dependency update itself is a minor or major release.
> This does not mean that the dependency update itself is a breaking change for MQT {{name}}.
> If you are sure that the dependency update does not introduce any breaking changes for MQT {{name}}, you can remove the `minor` or `major` label from the PR.
> This will ensure that the respective PR does not influence the type of an upcoming release.

Once everything is in order and the release draft looks good, you can merge the PR preparing the release.
Afterward, navigate to the [Releases page](https://github.com/{{organization}}/{{repository}}/releases) on GitHub, edit the created draft, and publish the release.

<!--- Links --->

[clion]: https://www.jetbrains.com/clion/
[mypy]: https://mypy-lang.org/
[nox]: https://nox.thea.codes/en/stable/
[issues]: https://github.com/{{organization}}/{{repository}}/issues
[pipx]: https://pypa.github.io/pipx/
[pre-commit]: https://pre-commit.com/
[ruff]: https://docs.astral.sh/ruff/
[uv]: https://docs.astral.sh/uv/
[vscode]: https://code.visualstudio.com/
[Keep a Changelog]: https://keepachangelog.com/en/1.1.0/
[Common Changelog]: https://common-changelog.org
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html

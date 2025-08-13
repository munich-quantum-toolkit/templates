# Development Guide

Ready to contribute to the project?
This guide will get you started.

## Initial Setup

1. Get the code

   ::::{tab-set}
   :::{tab-item} External Contribution
   If you do not have write access to the [{{organization}}/{{repository}}](https://github.com/{{organization}}/{{repository}}) repository, fork the repository on GitHub (see <https://docs.github.com/en/get-started/quickstart/fork-a-repo>) and clone your fork locally.

   ```console
   $ git clone git@github.com:your_name_here/{{repository}}.git
   ```

   :::
   :::{tab-item} Internal Contribution
   If you do have write access to the [{{organization}}/{{repository}}](https://github.com/{{organization}}/{{repository}}) repository, clone the repository locally.

   ```console
   $ git clone git@github.com/{{organization}}/{{repository}}.git
   ```

   :::
   ::::

2. Change into the project directory

   ```console
   $ cd {{repository}}
   ```

3. Create a branch for local development

   ```console
   $ git checkout -b name-of-your-bugfix-or-feature
   ```

   Now you can make your changes locally.

4. {% if project_type == "c++-python" -%}
   If you plan to [work on the Python package](#working-on-the-python-package), we highly recommend using [{code}`uv`][uv].
   {% elif project_type == "pure-python" -%}
   We highly recommend using [{code}`uv`][uv].
   {% endif -%}
   It is an extremely fast Python package and project manager written in Rust and developed by [Astral](https://astral.sh/) (the same team behind [{code}`ruff`][ruff]).
   It can act as a drop-in replacement for {code}`pip` and {code}`virtualenv`, and it provides a more modern and faster alternative to the traditional Python package management tools.
   It automatically handles the creation of virtual environments and the installation of packages, and it is much faster than {code}`pip`.
   Additionally, it can even set up Python for you if it is not installed yet.

   If you do not have {code}`uv` installed yet, you can install it via

   ::::{tab-set}
   :::{tab-item} macOS and Linux

   ```console
   $ curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   :::
   :::{tab-item} Windows

   ```console
   $ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   :::
   ::::

   Check out their excellent [documentation][uv] for more information.

5. We also highly recommend installing and setting up [{code}`pre-commit`][pre-commit] to automatically run a set of checks before each commit.

   ::::{tab-set}
   :::{tab-item} {code}`uv` _(recommended)_
   :sync: uv
   The easiest way to install {code}`pre-commit` is via [{code}`uv`][uv].

   ```console
   $ uv tool install pre-commit
   ```

   :::
   :::{tab-item} {code}`brew`
   :sync: brew
   If you use macOS and Homebrew, you can install {code}`pre-commit` with

   ```console
   $ brew install pre-commit
   ```

   :::
   :::{tab-item} {code}`pipx`
   :sync: pipx
   If you prefer to use [{code}`pipx`][pipx], you can install {code}`pre-commit` with

   ```console
   $ pipx install pre-commit
   ```

   :::
   :::{tab-item} {code}`pip`
   :sync: pip
   If you prefer to use regular {code}`pip` (preferably in a virtual environment), you can install {code}`pre-commit` with

   ```console
   $ pip install pre-commit
   ```

   :::
   ::::

   Afterward, you can install the {code}`pre-commit` hooks with

   ```console
   $ pre-commit install
   ```

{%- if project_type == "c++-python" %}

## Working on the C++ Library

Building the project requires a C++ compiler supporting _C++20_ and CMake with a minimum version of _3.24_.
As of July 2025, our CI pipeline on GitHub continuously tests the library under a wide matrix of systems and compilers:

- `ubuntu-24.04`: `Release` and `Debug` builds using `gcc`
- `ubuntu-24.04-arm`: `Release` build using `gcc`
- `macos-14`: `Release` and `Debug` builds using `AppleClang`
- `macos-13`: `Release` build using `AppleClang`
- `windows-2022`: `Release` and `Debug` builds using `msvc`
- `windows-11-arm`: `Release` build using `msvc`

To access the latest build logs, visit the [GitHub Actions page](https://github.com/{{organization}}/{{repository}}/actions/workflows/ci.yml).

Additionally, we regularly run extensive tests with an even wider matrix of compilers and operating systems.
We are not aware of any issues with other compilers or operating systems.
If you encounter any problems, please [open an issue](https://github.com/{{organization}}/{{repository}}/issues) and let us know.

### Configure and Build

:::{tip}
We recommend using an IDE like [CLion][clion] or [Visual Studio Code][vscode] for development.
Both IDEs have excellent support for CMake projects and provide a convenient way to run CMake and build the project.
If you prefer to work on the command line, the following instructions will guide you through the process.
:::

Our projects use _CMake_ as the main build configuration tool.
Building a project using CMake is a two-stage process.
First, CMake needs to be _configured_ by calling

```console
$ cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
```

This tells CMake to

- search the current directory {code}`.` (passed via {code}`-S`) for a {code}`CMakeLists.txt` file,
- process it into a directory {code}`build` (passed via {code}`-B`), and
- configure a {code}`Release` build (passed via {code}`-DCMAKE_BUILD_TYPE`) as opposed to, e.g., a _Debug_ build.

After configuring CMake, the project can be built by calling

```console
$ cmake --build build --config Release
```

This tries to build the project in the {code}`build` directory (passed via {code}`--build`).
Some operating systems and development environments explicitly require a configuration to be set, which is why the {code}`--config` flag is also passed to the build command.
The flag {code}`--parallel <NUMBER_OF_THREADS>` may be added to trigger a parallel build.

Building the project this way generates

- the main project libraries in the {code}`build/src` directory and
- some test executables in the {code}`build/test` directory.

:::{note}
This project uses CMake's [`FetchContent`](https://cmake.org/cmake/help/latest/module/FetchContent.html) module to download and build its dependencies.
Because of this, the first time you configure the project, you'll need an active internet connection to fetch the required libraries.

However, there are several ways to bypass these downloads:

- Use system-installed dependencies:
  If the dependencies are already installed on your system and Find-modules exist for them, `FetchContent` will use those versions instead of downloading them.
- Provide a local copy:
  If you have local copies of the dependencies (from a previous build or another project), you can point `FetchContent` to them by passing the [`-DFETCHCONTENT_SOURCE_DIR_<uppercaseName>`](https://cmake.org/cmake/help/latest/module/FetchContent.html#variable:FETCHCONTENT_SOURCE_DIR_%3CuppercaseName%3E) flag to your CMake configure step.
  The `<uppercaseName>` should be replaced with the name of the dependency as specified in the project's CMake files.
- Use project-specific options:
  Some projects provide specific CMake options to use a system-wide dependency instead of downloading it.
  Check the project's documentation or CMake files for these types of flags.

:::

### Running the C++ Tests and Code Coverage

We use the [GoogleTest](https://google.github.io/googletest/primer.html) framework for unit testing of the C++ library.
All tests are contained in the {code}`test` directory, which is further divided into subdirectories for different parts of the library.
You are expected to write tests for any new features you implement and ensure that all tests pass.
Our CI pipeline on GitHub will also run the tests and check for any failures.
It will also collect code coverage information and upload it to [Codecov](https://codecov.io/gh/{{organization}}/{{repository}}).
Our goal is to have new contributions at least maintain the current code coverage level, while striving for covering as much of the code as possible.
Try to write meaningful tests that actually test the correctness of the code and not just exercise the code paths.

Most IDEs like [CLion][clion] or [Visual Studio Code][vscode] provide a convenient way to run the tests directly from the IDE.
If you prefer to run the tests from the command line, you can use CMake's test runner [CTest](https://cmake.org/cmake/help/latest/manual/ctest.1.html).
To run the tests, call

```console
$ ctest -C Release --test-dir build
```

from the main project directory after building the project as described above.

:::{tip}
If you want to disable configuring and building the C++ tests, you can pass `-DBUILD_MQT_{{name.upper()}}_TESTS=OFF` to the CMake configure step.
:::

### C++ Code Formatting and Linting

This project mostly follows the [LLVM Coding Standard](https://llvm.org/docs/CodingStandards.html), which is a set of guidelines for writing C++ code.
To ensure the quality of the code and that it conforms to these guidelines, we use

- [`clang-tidy`](https://clang.llvm.org/extra/clang-tidy/), a static analysis tool that checks for common mistakes in C++ code, and
- [`clang-format`](https://clang.llvm.org/docs/ClangFormat.html), a tool that automatically formats C++ code according to a given style guide.

Common IDEs like [CLion][clion] or [Visual Studio Code][vscode] have plugins that can automatically run `clang-tidy` on the code and automatically format it with clang-format.

- If you are using CLion, you can configure the project to use the {code}`.clang-tidy` and {code}`.clang-format` files in the project root directory.
- If you are using Visual Studio Code, you can install the [clangd extension](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd).

They will automatically execute `clang-tidy` on your code and highlight any issues.
In many cases, they also provide quick-fixes for these issues.
Furthermore, they provide a command to automatically format your code according to the given style.

:::{note}
After configuring CMake, you can run `clang-tidy` on a file by calling

```console
$ clang-tidy <FILE> -- -I <PATH_TO_INCLUDE_DIRECTORY>
```

where {code}`<FILE>` is the file you want to analyze and {code}`<PATH_TO_INCLUDE_DIRECTORY>` is the path to the {code}`include` directory of the project.
:::

Our {code}`pre-commit` configuration also includes {code}`clang-format`.
If you have installed {code}`pre-commit`, it will automatically run clang-format on your code before each commit.
If you do not have {code}`pre-commit` setup, the [pre-commit.ci](https://pre-commit.ci) bot will run {code}`clang-format` on your code and automatically format it according to the style guide.

:::{tip}
Remember to pull the changes back into your local repository after the bot has formatted your code to avoid merge conflicts.
:::

Our CI pipeline will also run {code}`clang-tidy` over the changes in your pull request and report any issues it finds.
Due to technical limitations, the workflow can only post pull request comments if the changes are not coming from a fork.
If you are working on a fork, you can still see the {code}`clang-tidy` results either in the GitHub Actions logs, on the workflow summary page, or in the "Files changed" tab of the pull request.

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

We use [{code}`pybind11`](https://pybind11.readthedocs.io/en/stable) to expose large parts of the C++ core library to Python.
This allows us to keep the performance-critical parts of the code in C++ while providing a convenient interface for Python users.
All code related to C++-Python bindings is contained in the {code}`bindings` directory.

:::{tip}
If you just want to build the Python bindings themselves, you can pass `-DBUILD_MQT_{{name.upper()}}_BINDINGS=ON` to the CMake configure step.
CMake will then try to find Python and the necessary dependencies ({code}`pybind11`) on your system and configure the respective targets.
In [CLion][clion], you can enable an option to pass the current Python interpreter to CMake.
Go to `Preferences` -> `Build, Execution, Deployment` -> `CMake` -> `Python Integration` and check the box `Pass Python Interpreter to CMake`.
Alternatively, you can pass `-DPython_ROOT_DIR=<PATH_TO_PYTHON>` to the configure step to point CMake to a specific Python installation.
:::

The Python package itself lives in the {code}`python/mqt/{{repository}}` directory.

{%- elif project_type == "pure-python" %}

## Working on the Package

The package lives in the {code}`src/mqt/{{repository}}` directory.

{%- endif %}

::::::{tab-set}
:sync-group: installer

:::::{tab-item} {code}`uv` _(recommended)_
:sync: uv
Getting the project up and running locally using {code}`uv` is as simple as running

```console
$ uv sync
```

This will

- download a suitable version of Python for you (if you don't have it installed yet),
- create a virtual environment,
- install all the project's dependencies into the virtual environment with known-good versions, and
- build and install the project itself into the virtual environment.

:::::

:::::{tab-item} {code}`pip`
:sync: pip
The whole process is a lot more tedious and manual if you use {code}`pip`.
Once you have Python installed, you can first create a virtual environment using
::::{tab-set}
:::{tab-item} macOS and Linux

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
```

:::
:::{tab-item} Windows

```console
$ python3 -m venv .venv
$ .venv\Scripts\activate.bat
```

:::
::::
Then, you can install the project via

```console
(.venv) $ pip install -ve.
```

:::::
::::::

{%- if project_type == "c++-python" %}

:::{tip}
While the above commands install the project in editable mode (so that changes to the Python code are immediately reflected in the installed package), any changes to the C++ code will require a rebuild of the Python package.
:::

The commands above build a wheel for the project in an isolated environment and then install it into the virtual environment.
Due to the build isolation, the corresponding C++ build directory cannot be reused for subsequent builds.
This can make rapid iteration on the Python package cumbersome.
However, one can work around this by pre-installing the build dependencies in the virtual environment and then building the package without build isolation.

Since the overall process can be quite involved, we recommend using [{code}`nox`][nox] to automate the build process.

{%- elif project_type == "pure-python" %}

We also recommend using [{code}`nox`][nox].

{%- endif %}
{code}`nox` is a Python automation tool that allows you to define tasks in a `noxfile.py` file and then run them with a single command.

::::{tab-set}
:::{tab-item} {code}`uv` _(recommended)_
:sync: uv
The easiest way to install {code}`nox` is via [{code}`uv`][uv].

```console
$ uv tool install nox
```

:::
:::{tab-item} {code}`brew`
:sync: brew
If you use macOS and Homebrew, you can install {code}`nox` with

```console
$ brew install nox
```

:::
:::{tab-item} {code}`pipx`
:sync: pipx
If you prefer to use [{code}`pipx`][pipx], you can install {code}`nox` with

```console
$ pipx install nox
```

:::
:::{tab-item} {code}`pip`
:sync: pip
If you prefer to use regular {code}`pip` (preferably in a virtual environment), you can install {code}`nox` with

```console
$ pip install nox
```

:::
::::

We define four convenient {code}`nox` sessions in {code}`noxfile.py`:

- {code}`tests` to run the Python tests
- {code}`minimums` to run the Python tests with the minimum dependencies
- {code}`lint` to run the Python code formatting and linting
- {code}`docs` to build the documentation

These are explained in more detail in the following sections.

{%- if project_type == "c++-python" %}

## Running the Python Tests

{%- elif project_type == "pure-python" %}

## Running the Tests

{%- endif %}

The Python code is tested by unit tests using the [{code}`pytest`](https://docs.pytest.org/en/latest/) framework.
{%- if project_type == "c++-python" %}
The corresponding test files can be found in the {code}`test/python` directory.
{%- elif project_type == "pure-python" %}
The corresponding test files can be found in the {code}`tests` directory.
{%- endif %}
A {code}`nox` session is provided to conveniently run the Python tests.

```console
$ nox -s tests
```

The above command will automatically build the project and run the tests on all supported Python versions.
For each Python version, it will create a virtual environment (in the {code}`.nox` directory) and install the project into it.
We take extra care to install the project without build isolation so that rebuilds are typically very fast.

If you only want to run the tests on a specific Python version, you can pass the desired Python version to the {code}`nox` command.

```console
$ nox -s tests-3.12
```

:::{note}
If you do not want to use {code}`nox`, you can also run the tests directly using {code}`pytest`.

```console
(.venv) $ pytest
```

This requires that you have the project installed in the virtual environment and the test dependency group installed.
:::

We provide an additional nox session {code}`minimums` that makes use of {code}`uv`'s {code}`--resolution=lowest-direct` flag to install the lowest possible versions of the direct dependencies.
This ensures that the project can still be built and the tests pass with the minimum required versions of the dependencies.

```console
$ nox -s minimums
```

{%- if project_type == "c++-python" %}

## Python Code Formatting and Linting

{%- elif project_type == "pure-python" %}

## Code Formatting and Linting

{%- endif %}

The Python code is formatted and linted using a collection of [{code}`pre-commit`][pre-commit] hooks.
This collection includes

- [ruff][ruff], an extremely fast Python linter and formatter written in Rust, and
- [mypy][mypy], a static type checker for Python code.

There are two ways of using these hooks:

- You can install the hooks manually by running

  ```console
  $ pre-commit install
  ```

  in the project root directory.
  This will install the hooks in the {code}`.git/hooks` directory of the repository.
  The hooks will then be executed automatically when committing changes.

- You can use the {code}`nox` session {code}`lint` to run the hooks manually.

  ```console
  $ nox -s lint
  ```

  :::{note}
  If you do not want to use {code}`nox`, you can also run the hooks directly using {code}`pre-commit`.

  ```console
  $ pre-commit run --all-files
  ```

  :::

{%- if project_type == "c++-python" %}

## Python Documentation

{%- elif project_type == "pure-python" %}

## Documentation

{%- endif %}

The Python code is documented using [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings).
Every public function, class, and module should have a docstring that explains what it does and how to use it.
{code}`ruff` will check for missing docstrings and will explicitly warn you if you forget to add one.

We heavily rely on [type hints](https://docs.python.org/3/library/typing.html) to document the expected types of function arguments and return values.
{%- if project_type == "c++-python" %}
For the compiled parts of the code base, we provide type hints in the form of stub files in the {code}`python/mqt/{{repository}}` directory.
{%- endif %}

The Python API documentation is integrated into the overall documentation that we host on ReadTheDocs using the
[{code}`sphinx-autoapi`](https://sphinx-autoapi.readthedocs.io/en/latest/) extension for Sphinx.

## Working on the Documentation

The documentation is written in [MyST](https://myst-parser.readthedocs.io/en/latest/index.html) (a flavour of Markdown) and built using [Sphinx](https://www.sphinx-doc.org/en/master/).
The documentation source files can be found in the {code}`docs/` directory.

On top of the API documentation, we provide a set of tutorials and examples that demonstrate how to use the library.
These are written in Markdown using [myst-nb](https://myst-nb.readthedocs.io/en/latest/), which allows to execute Python code blocks in the documentation.
The code blocks are executed during the documentation build process, and the output is included in the documentation.
This allows us to provide up-to-date examples and tutorials that are guaranteed to work with the latest version of the library.

You can build the documentation using the {code}`nox` session {code}`docs`.

```console
$ nox -s docs
```

This will install all dependencies for building the documentation in an isolated environment, build the Python package, and then build the documentation.
Finally, it will host the documentation on a local web server for you to view.

:::{note}
If you don't want to use {code}`nox`, you can also build the documentation directly using {code}`sphinx-build`.

```console
(.venv) $ sphinx-build -b html docs/ docs/_build
```

The docs can then be found in the {code}`docs/_build` directory.
:::

## Maintaining the Changelog and Upgrade Guide

MQT {{name}} adheres to [Semantic Versioning], with the exception that minor releases may include breaking changes.
To inform users about changes to the project, we maintain a {doc}`changelog <CHANGELOG>` and an {doc}`upgrade guide <UPGRADING>`.

If your pull request includes noteworthy changes, please update the changelog.
The format is based on a mixture of [Keep a Changelog] and [Common Changelog].
There are the following categories:

- {code}`Added` for new features.
- {code}`Changed` for changes in existing functionality.
- {code}`Deprecated` for soon-to-be removed features.
- {code}`Removed` for now removed features.
- {code}`Fixed` for any bug fixes.
- {code}`Security` in case of vulnerabilities.

When updating the changelog, follow these guidelines:

- Add a changelog entry for every user-facing change in your pull request.
- Write entries in the imperative mood (e.g., "Add support for X" or "Fix bug in Y").
- A single pull request may result in multiple changelog entries.
- Entries in each category are sorted by merge time, with the latest pull requests appearing first.
- Each entry links to the pull request and all contributing authors.
  The links are defined at the bottom of the file.
  If this is your first contribution to this project, do not forget to add a link to your GitHub profile.

If your pull request introduces major or breaking changes, or if you think additional context would help users, please also add a section to the upgrade guide.
The upgrade guide is intended to provide a general overview of significant changes in a more descriptive and prose-oriented form than the changelog.
Use it to explain how users may need to adapt their usage of MQT {{name}}, highlight new workflows, or clarify the impact of important updates.
Feel free to write in a style that is helpful and accessible for users seeking to understand the broader implications of recent changes.

## Releasing a New Version

When it is time to release a new version of MQT {{name}}, create a pull request that prepares the release.
This pull request should:

- add new version titles in both the changelog and the upgrade guide,
- add the release date to the changelog entry for the new version,
- update the version links at the bottom of both files,
- review and streamline all changelog and upgrade guide entries for clarity and consistency,
- ensure that all links (to pull requests, authors, etc.) are defined and correct,
- double-check that the changelog comprehensively covers all changes since the last release and that nothing is missing,
- review the upgrade guide to ensure it covers all major or breaking changes and provides helpful context, and
- if the upgrade guide contains a section relevant to the release, add a reference to it in the changelog.

Before merging the release preparation pull request, check the GitHub release draft generated by the Release Drafter for unlabelled pull requests.
Unlabelled pull requests would appear at the top of the release draft below the main heading.
If you missed updating labels before merging, you can still update them and re-run the Release Drafter afterward.
Furthermore, check whether the version number in the release draft is correct.
The version number in the release draft is dictated by the presence of certain labels on the pull requests involved in a release.
By default, a patch release will be created.
If any pull request has the {code}`minor` or {code}`major` label, a major or minor release will be created, respectively.

:::{note}
Sometimes, dependabot or renovate will tag a dependency update pull request with a {code}`minor` or {code}`major` label because the dependency update itself is a minor or major release.
This does not mean that the dependency update itself is a breaking change for MQT {{name}}.
If you are sure that the dependency update does not introduce any breaking changes for MQT {{name}}, you can remove the {code}`minor` or {code}`major` label from the pull request.
This will ensure that the respective pull request does not influence the type of release.
:::

Once everything is in order and the release draft looks good, you can proceed to publish the new version.

<!-- Links -->

[clion]: https://www.jetbrains.com/clion/
[mypy]: https://mypy-lang.org/
[nox]: https://nox.thea.codes/en/stable/
[pipx]: https://pypa.github.io/pipx/
[pre-commit]: https://pre-commit.com/
[ruff]: https://docs.astral.sh/ruff/
[uv]: https://docs.astral.sh/uv/
[vscode]: https://code.visualstudio.com/
[Keep a Changelog]: https://keepachangelog.com/en/1.1.0/
[Common Changelog]: https://common-changelog.org
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html

# Using the MQT templates

## Synchronize repository files

Use the [templating action](../action.yml) in your repository's GitHub Actions
workflow. Provide the repository name, organization, display name, and project
type. The action opens a synchronization pull request when it runs on the
configured base branch. On other branches, it prints the diff.

For a working example, see the
[Templates repository workflow](../.github/workflows/templating.yml). Set the
corresponding `synchronize-*` input to `false` for files your repository
maintains locally.

## Configure Renovate

The synchronized `.github/renovate.json5` includes the
[CMake preset](../renovate/cmake.json). Annotate release pins in
`cmake/ExternalDependencies.cmake`:

```cmake
# renovate: datasource=github-tags depName=google/googletest
set(GTEST_REV
    "063de7e9578f82b369302001269680b4b1553359" # tag=v1.18.0
)
# renovate: datasource=github-releases depName=nlohmann/json
set(JSON_TAG v3.12.0)
```

For commit pins, Renovate updates the tag and SHA together. Release versions can
include a `v` prefix; strip it in CMake when passing the version to
`find_package()`. Remove the annotation to keep a development commit pinned.

CMake updates open individual PRs for review. Archive checksums need manual
updates.

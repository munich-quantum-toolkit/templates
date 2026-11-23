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

The action synchronizes `.github/renovate.json5` by default. It includes the
shared CMake preset and enables the regex manager. Repositories with their own
Renovate configuration can extend
`github>munich-quantum-toolkit/templates:cmake` directly. If they set
`enabledManagers`, add `custom.regex` to that list.

The preset reference follows the Templates repository's default branch. To use a
specific Templates release, append `#<tag>` once that tag contains
[`cmake.json`](../cmake.json).

### Track a release by commit SHA

In `cmake/ExternalDependencies.cmake`, add the annotation above the `set()`
declaration and write the release tag after the quoted commit SHA. Use the SHA
in the Git checkout or archive URL. Renovate updates the tag and SHA together.

```cmake
# renovate: datasource=github-tags depName=google/googletest
set(GTEST_REV
    "52eb8108c5bdec04579160ae17225d66034bd723" # tag=v1.17.0
)
```

### Track a release by version

Use `github-releases` for a numeric GitHub release version. The variable can
supply the Git tag or form part of a release asset URL.

```cmake
# renovate: datasource=github-releases depName=aws/aws-sdk-cpp
set(AWSSDK_VERSION 1.11.935)
```

If CMake adds a prefix such as `v` to the tag, set a Renovate `extractVersion`
rule for that dependency to extract the numeric version. Keep the minimum
supported installed-package version separate from the fetched version where they
serve different purposes.

### Pin a development commit

Remove the Renovate annotation and release tag when pinning a development
commit. Restore both when switching back to a release. The preset only matches
annotated declarations in `cmake/ExternalDependencies.cmake`.

### Review dependency updates

The synchronized configuration opens individual CMake update pull requests for
review and schedules regular dependency updates on weekends. Checksummed release
archives need a rule that updates the checksum alongside the version.

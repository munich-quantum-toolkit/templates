## Description

Please include a summary of the change and, if applicable, which issue is fixed.
Please also include relevant motivation and context.
List any dependencies that are required for this change.
Leave validation commands, test counts, and pass/fail summaries to CI.

<!---
Replace `(issue)` with the issue number fixed by this pull request.
If this PR does not fix an issue, please remove the line.
-->
Fixes #(issue)

## Checklist

<!---
This checklist serves as a reminder of a couple of things that ensure your pull request will be merged swiftly.
-->

- [ ] The pull request only contains commits that are focused and relevant to this change.
- [ ] I have added or updated tests where needed to cover features and bug fixes.
- [ ] I have updated the documentation to reflect these changes.
{%- if has_changelog_and_upgrade_guide %}
- [ ] I have added entries to the changelog for any noteworthy additions, changes, fixes, or removals.
- [ ] I have added migration instructions to the upgrade guide (if needed).
{%- endif %}
- [ ] The changes follow the project's style guidelines and introduce no new warnings.
- [ ] The changes pass the relevant CI checks.
- [ ] I have reviewed my own code changes.

**If PR contains AI-assisted content:**

- [ ] Any agent that created, edited, or submitted GitHub content was explicitly authorized for that scope, as required by our [AI Usage Guidelines](https://github.com/{{organization}}/{{repository}}/blob/main/docs/ai_usage.md).
- [ ] Every agent-authored or agent-edited public text body begins with the visible disclosure `🤖 *AI text below* 🤖` (titles are exempt).
- [ ] I have disclosed AI assistance in the PR description.
- [ ] I confirm that I have personally reviewed and understood all AI-generated content, and accept full responsibility for it.

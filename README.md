<p align="center">
  <a href="https://mqt.readthedocs.io">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/munich-quantum-toolkit/.github/refs/heads/main/docs/_static/logo-mqt-dark.svg" width="60%">
      <img src="https://raw.githubusercontent.com/munich-quantum-toolkit/.github/refs/heads/main/docs/_static/logo-mqt-light.svg" width="60%" alt="MQT Logo">
    </picture>
  </a>
</p>

# Templates for the Munich Quantum Toolkit (MQT)

This repository contains a collection of templates and a GitHub action to synchronize them across the repositories of the [_Munich Quantum Toolkit (MQT)_](https://mqt.readthedocs.io).

If you have any questions, feel free to create a [discussion](https://github.com/munich-quantum-toolkit/templates/discussions) or an [issue](https://github.com/munich-quantum-toolkit/templates/issues) on [GitHub](https://github.com/munich-quantum-toolkit/templates).

## Contributors and Supporters

The _[Munich Quantum Toolkit (MQT)](https://mqt.readthedocs.io)_ is developed by the [Chair for Design Automation](https://www.cda.cit.tum.de/) at the [Technical University of Munich](https://www.tum.de/) and supported by the [Munich Quantum Software Company (MQSC)](https://munichquantum.software).
Among others, it is part of the [Munich Quantum Software Stack (MQSS)](https://www.munich-quantum-valley.de/research/research-areas/mqss) ecosystem, which is being developed as part of the [Munich Quantum Valley (MQV)](https://www.munich-quantum-valley.de) initiative.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/munich-quantum-toolkit/.github/refs/heads/main/docs/_static/mqt-logo-banner-dark.svg" width="90%">
    <img src="https://raw.githubusercontent.com/munich-quantum-toolkit/.github/refs/heads/main/docs/_static/mqt-logo-banner-light.svg" width="90%" alt="MQT Partner Logos">
  </picture>
</p>

Thank you to all the contributors who have helped make the MQT Templates a reality and keep them up-to-date!

<p align="center">
<a href="https://github.com/munich-quantum-toolkit/templates/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=munich-quantum-toolkit/templates" />
</a>
</p>

## Getting Started

This repository includes a GitHub action that can be used to synchronize the [templates](./templates/) to other MQT repositories.
For an example on how to use the action, refer to this repository's [`templating.yml`](./.github/workflows/templating.yml).

The action uses [`Jinja`](https://jinja.palletsprojects.com/en/stable/) to render the templates.
The rendered templates are placed into the [`.templates`](./.templates/) directory that is created by this action.
Afterward, `git file-merge` is used to consolidate changes to the rendered templates with custom changes to the templated files.
The action then creates a PR that updates the files in the [`.templates`](./.templates/) directory as well as the templated files.

---

## Acknowledgements

The Munich Quantum Toolkit has been supported by the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation program (grant agreement No. 101001318), the Bavarian State Ministry for Science and Arts through the Distinguished Professorship Program, as well as the Munich Quantum Valley, which is supported by the Bavarian state government with funds from the Hightech Agenda Bayern Plus.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/munich-quantum-toolkit/.github/refs/heads/main/docs/_static/mqt-funding-footer-dark.svg" width="90%">
    <img src="https://raw.githubusercontent.com/munich-quantum-toolkit/.github/refs/heads/main/docs/_static/mqt-funding-footer-light.svg" width="90%" alt="MQT Funding Footer">
  </picture>
</p>

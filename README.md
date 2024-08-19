# Biomedical MT Agents [![DOI](https://zenodo.org/badge/844520374.svg)](https://zenodo.org/doi/10.5281/zenodo.13342142)


This repository contains code for Biomedical Machine Translation (MT) agents. The agents and tasks implemented here are designed to facilitate the translation of biomedical texts using advanced language models.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

To get started with this project, you will need to have Python 3.8 or higher installed. The project dependencies are managed using [Poetry](https://python-poetry.org/).

## Project Structure

- main.py: The entry point for the project. Loads environment variables and initializes the translation crew.
- translation_tasks.py: Defines tasks for biomedical text translation.
- translation_agents.py: Contains agent definitions used to perform translations.
- crew.py: Manages the crew of agents working on translation tasks.
- pyproject.toml: Defines the project dependencies and build configurations.

## How To Cite

```
@software{castaldo_biomedical_mt_agents_2024,
  author       = {Castaldo, Antonio},
  title        = {Biomedical {MT} {Agents}},
  year         = {2024},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  url          = {https://github.com/YourGitHubUsername/Biomedical-MT-Agents},
  doi          = {10.5281/zenodo.13342142},
  note         = {Submission to WMT24}
}
```

## LICENSE

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

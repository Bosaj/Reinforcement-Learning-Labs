# Reinforcement Learning Labs

Labs and homework from the **Machine Learning 2 — Reinforcement Learning** course at ENIAD Berkane: tabular Q-learning, SARSA, and PPO applied to classic Gymnasium environments.

[![CI](https://github.com/Bosaj/Reinforcement-Learning-Labs/actions/workflows/ci.yml/badge.svg)](https://github.com/Bosaj/Reinforcement-Learning-Labs/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange.svg)](https://jupyter.org/)

## Overview

This repository collects the practical work (`TP1`–`TP4`) and homework exercises produced for the Reinforcement Learning module of the Machine Learning 2 course (Prof. Mohamed Khalifa Boutahir), each notebook implementing and evaluating a specific RL algorithm on a Gymnasium environment, with recorded video demonstrations and result plots.

## Contents

| Lab | Environment | Algorithm | Notebook |
| --- | --- | --- | --- |
| HomeWork | Custom grid world (treasure/trap) | Random policy + tabular Q-learning (with terminal animation) | [`HomeWork/HomeWork.py`](HomeWork/HomeWork.py), [`HomeWork/HomeWorkAnimation.py`](HomeWork/HomeWorkAnimation.py) |
| TP1 | `CartPole-v1` | Introduction to RL / Q-table basics | [`TP1/TP1.ipynb`](TP1/TP1.ipynb) |
| TP2 | `FrozenLake-v1` | Q-learning | [`TP2/TP2.ipynb`](TP2/TP2.ipynb) |
| TP3 | Custom traffic-light simulation | Q-learning vs. SARSA comparison | [`TP3/TP3.ipynb`](TP3/TP3.ipynb), [`TP3/traffic_env.py`](TP3/traffic_env.py) |
| TP4 | `Taxi-v3` | PPO (Proximal Policy Optimization) | [`TP4/TP4.ipynb`](TP4/TP4.ipynb) |

Each `TPx` folder also includes a demo video (`.mp4`) and result screenshot (`.png`) of the trained agent.

## Tech Stack

- **Python 3.10+**
- [Gymnasium](https://gymnasium.farama.org/) — RL environments (`CartPole-v1`, `FrozenLake-v1`, `Taxi-v3`)
- **NumPy** — Q-table storage and numerical operations
- **Matplotlib** — training curves and result plots
- **pandas** — data handling in TP3
- Jupyter Notebook

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/Bosaj/Reinforcement-Learning-Labs.git
cd Reinforcement-Learning-Labs

# 2. Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
pip install jupyter

# 4. Launch Jupyter and open any TPx/TPx.ipynb notebook
jupyter notebook
```

The `HomeWork` scripts are plain Python and can be run directly, e.g. `python HomeWork/HomeWork.py`.

## Testing / CI

A GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push/PR to `main`:

- Installs dependencies from `requirements.txt`
- Validates that every `.ipynb` file is structurally well-formed (via `nbformat`)
- Lints the `.py` scripts with `flake8` (non-blocking, style feedback only)

This does not execute full agent training (no GPU / long-running training in CI) — it guards against broken notebooks and import errors.

## Project Structure

```
Reinforcement-Learning-Labs/
├── HomeWork/           # Introductory grid-world exercises
├── TP1/                # CartPole-v1
├── TP2/                # FrozenLake-v1
├── TP3/                # Q-learning vs SARSA (traffic simulation)
├── TP4/                # Taxi-v3 (PPO)
├── requirements.txt
└── .github/workflows/ci.yml
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Distributed under the MIT License — see [LICENSE.txt](LICENSE.txt).

## Author

**Oussama EL HADJI** — [github.com/Bosaj](https://github.com/Bosaj)
Final-year student, École Nationale de l'Intelligence Artificielle et du Digital (ENIAD), Berkane.

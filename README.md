<div align="center">

# 🔥 PrometheusDS

### Self-Evolving AI Agents for End-to-End Data Science

**Built by Shyaam Prasadh — AI Research Manager at Entain and part of Entain's Enterprise AI & Data Science ecosystem.**

*An open-source agentic framework exploring how AI agents can plan, execute, evaluate, repair, and continuously improve real-world data science workflows.*

</div>

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/sprasadhpy/PrometheusDS?style=for-the-badge)](https://github.com/sprasadhpy/PrometheusDS)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange?style=for-the-badge)](https://github.com/sprasadhpy/PrometheusDS)
[![License](https://img.shields.io/github/license/sprasadhpy/PrometheusDS?style=for-the-badge)](LICENSE)

</div>

---

## What if a Data Science System Could Improve Itself?

Traditional data science pipelines are static.

A data scientist writes code, runs experiments, investigates failures, adjusts transformations, retrains models, evaluates results, and repeats the process.

**PrometheusDS explores a different approach.**

The goal is to build a team of collaborative AI agents capable of:

> **Plan → Execute → Evaluate → Reflect → Repair → Improve**

PrometheusDS is an open-source research and engineering project for building **self-evolving data science agents**.

Instead of treating an LLM as a chatbot that simply generates code, PrometheusDS explores agents that can reason about a data science problem, generate executable workflows, safely run code, evaluate their own outputs, recover from failures, and iteratively improve the pipeline.

---

## Why PrometheusDS?

Modern data science is not a single task.

A production-grade workflow may require:

- understanding raw datasets;
- identifying data-quality problems;
- cleaning and transforming data;
- conducting exploratory analysis;
- generating and selecting features;
- training multiple candidate models;
- evaluating performance;
- diagnosing failures;
- revising earlier decisions;
- producing reusable code and reports.

PrometheusDS approaches this as a **multi-agent system**.

Each specialist agent focuses on a part of the data science lifecycle, while supervisor, evaluation, and reflection mechanisms coordinate the overall workflow.

The long-term vision is simple:

> **Build an AI Data Science Squad that does not just execute tasks — it learns from execution outcomes and improves its own workflows.**

---

## The PrometheusDS Agent Squad

PrometheusDS is being designed around a team of specialist agents.

| Agent | Responsibility |
|---|---|
| **Supervisor Agent** | Understands the objective and coordinates specialist agents |
| **Planning Agent** | Converts business and analytical objectives into an execution plan |
| **Data Loader Agent** | Loads, inspects, profiles, and validates datasets |
| **Data Cleaning Agent** | Plans and executes auditable data-quality transformations |
| **EDA Agent** | Investigates distributions, relationships, anomalies, and patterns |
| **Data Wrangling Agent** | Filters, joins, aggregates, and restructures datasets |
| **Feature Engineering Agent** | Creates and evaluates candidate predictive features |
| **Modelling Agent** | Trains and compares candidate machine-learning models |
| **Evaluation Agent** | Evaluates statistical and predictive performance |
| **Reflection Agent** | Critiques results and identifies opportunities for improvement |
| **Repair Agent** | Diagnoses failed generated code and attempts corrective action |
| **Reporting Agent** | Converts analytical outputs into structured reports and insights |

---

## The Self-Evolving Loop

The core research direction behind PrometheusDS is an iterative agent loop:

```text
                    ┌─────────────────────┐
                    │     User Goal       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Supervisor Agent   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Planning Agent    │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌────────────────────────────────┐
              │     Specialist Agent Squad     │
              │                                │
              │  Cleaning │ EDA │ Features     │
              │  Modeling │ SQL │ Evaluation   │
              └───────────────┬────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Sandboxed Execution │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Validation & Metrics│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Reflection Agent    │
                    └──────────┬──────────┘
                               │
                    Improve    │    Repair
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             Better Strategy       Code Repair Agent
                    │                     │
                    └──────────┬──────────┘
                               │
                               ▼
                         Next Iteration
```

---

## AI Pipeline Studio

AI Pipeline Studio is the visual experimentation environment for PrometheusDS.

It brings human-controlled data science workflows and agentic execution into one workspace.

The goal is to allow users to combine:

- manual analytical steps;
- AI-generated transformations;
- specialist agents;
- visual pipeline construction;
- dataset lineage;
- reproducible Python code;
- model experimentation;
- evaluation and comparison;
- MLflow-based experiment tracking.

### Current capabilities

- Visual pipeline editor
- Dataset inspection
- Table exploration
- Interactive charts
- Exploratory Data Analysis
- AI-assisted code generation
- Feature engineering workflows
- Model training
- Predictions
- MLflow integration
- Multi-dataset workflows
- Dataset merge operations
- Project persistence and rehydration

### Run the Studio locally:

```bash
streamlit run apps/ai-pipeline-studio-app/app.py
```

---

## Quick Start

### Requirements

- Python 3.10+
- An LLM endpoint supported by the configured LangChain integration
- OpenAI-compatible APIs or supported local models

### Clone PrometheusDS

```bash
git clone https://github.com/sprasadhpy/PrometheusDS.git
cd PrometheusDS
```

### Install

```bash
pip install -e .
```

### Launch AI Pipeline Studio

```bash
streamlit run apps/ai-pipeline-studio-app/app.py
```

---

## Example: Data Cleaning Agent

The Data Cleaning Agent demonstrates the core PrometheusDS philosophy.

Rather than applying a fixed collection of transformations, the workflow can:

- inspect and summarize the dataset;
- recommend cleaning actions;
- optionally request human approval;
- generate reusable Python cleaning code;
- execute the generated function in a controlled environment;
- validate the resulting dataset;
- detect execution failures;
- repair failed code;
- retry execution;
- return the cleaned dataset, code, and workflow summary.

```python
from Prometheus_DS.agents import DataCleaningAgent

agent = DataCleaningAgent(
    model=llm,
    human_in_the_loop=False,
)

result = agent.run(
    data=df,
    instructions="""
    Analyse the dataset and create an appropriate cleaning strategy.
    Preserve potentially meaningful observations.
    Explain significant transformations.
    Produce reusable cleaning code.
    """
)

result.cleaned_data        # Cleaned pandas DataFrame
result.cleaning_plan       # Recommended steps
result.generated_code      # Reusable Python function
result.execution_report    # Attempt history and improvement summary
result.attempts            # Detailed list of all execution attempts
```

---

## Repository Overview

```
PrometheusDS/
│
├── Prometheus_DS/
│   ├── agents/
│   ├── ds_agents/
│   ├── ml_agents/
│   ├── multiagents/
│   ├── templates/
│   ├── tools/
│   └── utils/
│
├── apps/
│   ├── ai-pipeline-studio-app/
│   ├── exploratory-copilot-app/
│   ├── pandas-data-analyst-app/
│   └── sql-database-agent-app/
│
├── examples/
│   ├── data_cleaning_agent.ipynb
│   ├── data_visualization_agent.ipynb
│   ├── feature_engineering_agent.ipynb
│   ├── data_wrangling_agent.ipynb
│   ├── ml_agents/
│   └── multiagents/
│
├── tests/
└── README.md
```

---

## Research Direction

PrometheusDS is an active exploration of several questions:

### Can agents critique their own analytical decisions?

A successful run is not necessarily a good run.

PrometheusDS aims to distinguish between:

- code execution success;
- statistical validity;
- predictive performance;
- data leakage;
- overfitting;
- unstable features;
- inappropriate transformations;
- weak analytical reasoning.

### Can a data science agent learn from execution feedback?

Future iterations will explore structured memory of:

- successful transformations;
- failed approaches;
- dataset characteristics;
- model performance;
- error patterns;
- human feedback;
- reusable strategies.

### Can specialist agents collaborate like an AI Data Science Squad?

The broader goal is not to create one giant agent.

The goal is to create a coordinated system of specialist agents with explicit responsibilities, execution boundaries, evaluation mechanisms, and shared context.

---

## Roadmap

- [x] Data Cleaning Agent
- [x] Data Wrangling Agent
- [x] Data Visualization Agent
- [x] EDA Agent
- [x] Feature Engineering Agent
- [x] SQL Agent
- [x] MLflow integration
- [x] H2O modelling workflows
- [x] Supervisor-based multi-agent orchestration
- [x] AI Pipeline Studio
- [ ] Cross-agent memory
- [ ] Reflection-driven pipeline improvement
- [ ] Automated experiment critique
- [ ] Data leakage detection agent
- [ ] Model failure diagnosis
- [ ] Agent performance benchmarks
- [ ] Dataset-specific strategy memory
- [ ] Automated pipeline optimisation
- [ ] Human feedback learning loop
- [ ] Self-evolving agent policies

---

## About the Creator

PrometheusDS is led by **Shyaam Prasadh**, an AI Research Manager working with the AI and Data Science ecosystem at Entain.

His work focuses on applied AI systems, agentic AI, large language models, machine learning, and the engineering required to move AI systems from experimentation towards real-world use.

PrometheusDS is an independent open-source project exploring a broader question:

> *What happens when AI agents move beyond generating data science code and begin evaluating, repairing, and improving the entire analytical workflow?*

---

## Contributing

PrometheusDS is under active development.

Contributions are welcome in areas including:

- AI agents;
- data science automation;
- agent evaluation;
- LangGraph workflows;
- safe code execution;
- AutoML;
- MLOps;
- agent memory;
- reflection and self-improvement;
- human-in-the-loop systems.

If this direction interests you, open an issue, propose an experiment, or contribute an agent.

---

## Support the Project

If you find PrometheusDS useful or interesting:

- ⭐ Star the repository
- 🍴 Fork it and experiment
- 🧪 Try the agents on real datasets
- 🐛 Report failures and edge cases
- 🤝 Contribute new agents and evaluation methods

The aim is to build an open experimentation ground for the next generation of agentic data science systems.

---

<div align="center">

### 🔥 PrometheusDS

**Plan. Execute. Evaluate. Reflect. Repair. Improve.**

*Building towards self-evolving AI Data Science Agents.*

</div>

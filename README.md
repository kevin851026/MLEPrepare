# MLEPrepare

Companion coding workspace for my Notion MLE notes.

- **Notion**: concept recap and study notes.
- **GitHub**: small runnable examples for the topics I am actively studying.

## Structure

```text
MLEPrepare/
├── ml_foundations/
│   └── 01_classic_ml_concepts/
│       └── linear_regression.py
├── pyproject.toml
└── README.md
```

The numbered folders mirror the Notion hierarchy. Python directories and files use
lowercase snake case.

## Current topic

- Linear Regression

## Setup

Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/), then run:

```bash
uv sync
uv run python ml_foundations/01_classic_ml_concepts/linear_regression.py
```

Use `uv add <package>` to add another dependency.

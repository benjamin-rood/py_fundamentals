# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python Foundations is an 8-week curriculum teaching Python literacy to beginners (targeting healthcare professionals) for AI-assisted development. The goal is code *reading and reviewing* competency, not writing large programs from scratch. The curriculum follows Ryan Carson's 2026 hierarchy: understand LLMs → security hygiene → "one level below" (Git, testing, how code works).

## Repository Structure

The repo has two main content directories, split by learning phase:

- **`python_learning_notebooks/`** — Jupyter notebooks for Weeks 0–4 (Google Colab). Covers fundamentals: objects/references, control flow, functions, data structures. Each notebook is numbered by week and lesson (e.g., `01_2_references.ipynb`).
- **`python_learning_replit/`** — Markdown lesson guides and Python files for Weeks 5–7 (Replit). Covers scripts, imports, pytest, Git, error handling, AI code review, and Claude Code usage. Contains working example code (`bmi.py`) and tests (`test_bmi.py`).
- **`curriculum_v7.md`** — Master curriculum outline (also duplicated in `python_learning_notebooks/`).

## Commands

```bash
# Run tests (from python_learning_replit/)
cd python_learning_replit && pytest -v

# Run a single test
pytest -v python_learning_replit/test_bmi.py::test_normal_bmi
```

## Key Conventions

- The BMI calculator (`bmi.py` / `test_bmi.py`) is the running example throughout the curriculum. Changes to it should maintain its role as a teaching aid.
- Notebooks are designed to be opened via Google Colab links from GitHub — they should remain self-contained with inline markdown explanations.
- The curriculum philosophy is "no analogies — only actual mechanisms." Content should explain how Python works (objects, references, `id()`) rather than using metaphors.
- Lesson numbering follows `WW_L_topic` format (week_lesson_topic).

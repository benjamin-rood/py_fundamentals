# Python Foundations for AI-Assisted Development

An 8-week course that teaches you enough Python to read, understand, and review AI-generated code. Everything runs in your browser — no installation required.

## What You Need Before Starting

- A **Google account** (Gmail). You'll use this to open and save lesson notebooks.
- A web browser (Chrome works best with Google Colab).

That's it. No software to install.

## How This Course Works

The course has two phases, each using a different browser-based tool:

- **Weeks 0–4** use [Google Colab](https://colab.research.google.com/) — an online notebook environment where you run Python one cell at a time and see results immediately.
- **Weeks 5–7** use [Replit](https://replit.com/) — a browser-based coding environment with a file system, terminal, and package management.

You'll transition from Colab to Replit at Week 5 when the lessons move from learning concepts to building with real files, imports, and tests.

## What is Google Colab?

Google Colab is a free tool from Google that lets you write and run Python code in your browser. Python runs on Google's computers, not yours. Your work can be saved to your Google Drive.

If you've never used Colab before, read Google's own introduction: [Welcome to Colab](https://colab.research.google.com/notebooks/intro.ipynb).

## Getting Started (Weeks 0–4)

### Step 1: Open your first lesson

Click the link for **Lesson 0.1** below. It will open the notebook directly in Google Colab.

### Step 2: Save a copy to your Google Drive

When the notebook opens, go to **File > Save a copy in Drive** before doing anything else. The original notebook is read-only — it belongs to the course repository and cannot be modified. Your copy in Google Drive is where your work is saved. If you skip this step, everything you type or run will be lost when you close the tab.

### Step 3: Work through the notebook

Read the explanations, run each code cell (click the play button or press **Shift+Enter**), and experiment. The notebooks are self-contained — everything you need is in the cells and markdown text.

## Lesson Notebooks (Weeks 0–4)

> **Before you start:** When you open a notebook in Colab, go to **File > Save a copy in Drive** immediately. The links below open read-only originals — any work you do in the original will be lost when you close the tab. Your saved copy in Google Drive is where your actual work lives.

Click any link below to open the lesson in Google Colab.

### Week 0: Getting Started

| Lesson | Topic | Open in Colab |
|--------|-------|---------------|
| 0.1 | Opening Your First Notebook | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/00_1_first_notebook.ipynb) |
| 0.2 | Variables and Cells | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/00_2_variables_and_cells.ipynb) |
| 0.3 | Python Tutor | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/00_3_python_tutor.ipynb) |

### Week 1: How Python Works

| Lesson | Topic | Open in Colab |
|--------|-------|---------------|
| 1.1 | Objects | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/01_1_objects.ipynb) |
| 1.2 | References | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/01_2_references.ipynb) |
| 1.3 | Strings | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/01_3_strings.ipynb) |

### Week 2: Control Flow

| Lesson | Topic | Open in Colab |
|--------|-------|---------------|
| 2.1 | Conditionals | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/02_1_conditionals.ipynb) |
| 2.2 | Loops | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/02_2_loops.ipynb) |

### Week 3: Functions

| Lesson | Topic | Open in Colab |
|--------|-------|---------------|
| 3.1 | Functions | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/03_1_functions.ipynb) |
| 3.2 | Scope | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/03_2_scope.ipynb) |

### Week 4: Data Structures

| Lesson | Topic | Open in Colab |
|--------|-------|---------------|
| 4.1 | Lists | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/04_1_lists.ipynb) |
| 4.2 | Dictionaries | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/04_2_dicts.ipynb) |
| 4.3 | Mutability | [Open](https://colab.research.google.com/github/benjamin-rood/py_fundamentals/blob/main/python_learning_notebooks/04_3_mutability.ipynb) |

## Lesson Guides (Weeks 5–7)

At Week 5 you move to [Replit](https://replit.com/). Create a free account, then follow the lesson guides below. Each guide is a markdown file you can read directly on GitHub.

| Lesson | Topic |
|--------|-------|
| [5.1](python_learning_replit/05_1_setting_up_replit.md) | Setting Up Replit |
| [5.2](python_learning_replit/05_2_imports_and_modules.md) | Imports and Modules |
| [5.3](python_learning_replit/05_3_testing_with_pytest.md) | Testing with pytest |
| [5.4](python_learning_replit/05_4_git_hands_on.md) | Git Hands-On |
| [6.3](python_learning_replit/06_3_reading_ai_generated_code.md) | Reading AI-Generated Code |
| [7.2](python_learning_replit/07_2_working_with_claude_code.md) | Working with Claude Code |
| [7.3](python_learning_replit/07_3_whats_next.md) | What's Next |

The BMI calculator ([`bmi.py`](python_learning_replit/bmi.py) and [`test_bmi.py`](python_learning_replit/test_bmi.py)) is the running example used throughout these lessons.

## Supplementary Resources

All optional. Read or watch *after* the corresponding lesson if a concept didn't land. The curriculum is designed to stand alone — these are for reinforcement only.

### Free

| When | Resource | Why |
|------|----------|-----|
| Week 1 | [Launch School: "Variables as Pointers"](https://launchschool.com/books/ruby/read/more_stuff#variables_as_pointers) | Covers the same object/reference model as Week 1 |
| Week 1 | [Ned Batchelder — "Facts and Myths about Python Names and Values" (PyCon talk)](https://www.youtube.com/watch?v=_AEJHKGk9ns) — first 12 minutes only | Authoritative treatment with no analogies |
| Week 5 | [pytest docs: "Get Started"](https://docs.pytest.org/en/stable/getting-started.html) | Short, practical pytest introduction |
| After Week 7 | [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) | Natural next step: files, automation, real scripts |
| After Week 7 | [Ryan Carson's 2026 coding guide](https://theneuron.ai/explainer-articles/how-to-learn-to-code-2026-ryan-carson-guide/) | The playbook this curriculum prepares you for |
| After Week 7 | [Claude Code docs](https://docs.claude.com) | Reference for continued Claude Code use |

### Real Python (paid, ~$20/month)

Articles from [realpython.com](https://realpython.com/) for deeper coverage. Read after the lesson notebook for that week.

| Week | Article | Why |
|------|---------|-----|
| 1 | "Variables in Python: Usage and Best Practices" | References, `id()`, identity vs equality |
| 2 | "Python for Loops: The Pythonic Way" | Loop mechanics |
| 3 | "Pass by Reference in Python: Best Practices" | Pass-by-assignment with `id()` |
| 4 | "Python's list Data Type: A Deep Dive" | Lists reference |
| 4 | "Dictionaries in Python" | Dicts reference |
| 4 | "Python's Mutable vs Immutable Types" | `id()`, aliasing, copying |

## Full Curriculum Outline

The complete week-by-week curriculum with learning objectives is in [`curriculum_v7.md`](curriculum_v7.md).

## Troubleshooting

**The Colab link shows "File not found"** — The repository may be private. Ask your instructor for access, or check that you're signed into GitHub.

**I lost my changes in Colab** — You need to save a copy to your Drive first (File > Save a copy in Drive). The original notebook is read-only.

**Shift+Enter doesn't run the cell** — Make sure you've clicked into the cell first. The cell border should turn blue or green.

## Development

To verify all notebook code cells execute without errors:

```bash
python3 test_notebooks.py          # standalone
pytest test_notebooks.py -v        # via pytest
```

No Jupyter installation required — notebooks are parsed as JSON and code cells are executed directly. Cells that intentionally demonstrate errors (e.g. `10 / 0`) are tagged with `"raises-exception"` in their metadata and are expected to fail.

## License

[MIT](LICENSE) — Benjamin Rood, 2026

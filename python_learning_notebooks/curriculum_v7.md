# Python Foundations for AI-Assisted Development
## Complete Lesson Outline: Weeks 0–7 (Version 7)

---

## Course Overview

**Target Audience:** Healthcare professional (nurse practitioner) with no programming experience

**Goal:** Build enough code literacy and development concepts to work effectively with AI coding agents — then transition to Ryan Carson's "just-in-time learning" approach for everything else.

**Philosophy:**
- No analogies — only actual mechanisms
- 100% browser-based — no local installation ever. Colab for learning, Replit for building.
- Lean and fast — teach only what AI coding agents can't substitute for
- The student should be *using AI to build things* within 8 weeks, not 15
- Foundation for reading, understanding, and reviewing AI-generated code — not for writing large programs from scratch

**What Changed (v6 → v7):**
This curriculum was restructured around Ryan Carson's hierarchy for coding in 2026:
1. Understand how LLMs work
2. Security hygiene
3. Know "one level below" — Git, testing, how code works
4. Don't worry about: specific languages, frameworks, libraries, networking, deployment

The old curriculum spent 15 weeks building toward Claude Code at the very end. This version gets there in 8 weeks by cutting deep dives that AI agents handle for you (advanced list operations, standard library tours, multi-week projects) and eliminating the local installation barrier entirely. The object/reference model stays — it's essential for debugging. But we no longer need to teach someone to be a self-sufficient Python programmer. We need to teach them to be an effective AI collaborator.

**Total Duration:** 8 weeks (3–4 hours per week), approximately 25–30 hours

**Pacing Note:** Each week targets 3–4 hours. The week numbers are guides, not deadlines. If a week feels heavy, let it spill.

**Tools by Phase:**
- **Weeks 0–4:** Google Colab in browser (primary), Python Tutor (visualization). No installation required.
- **Week 5:** Replit (browser-based IDE with terminal, file system, and package management — no installation)
- **Week 6–7:** Replit + Claude Code

**Why Colab then Replit (not one or the other):**
- Colab notebooks are the best tool for *learning* — run one cell at a time, see results immediately, markdown explanations inline, zero friction
- Replit is the best tool for *building* — real file system, terminal, packages, deployment, version control. Carson's #1 recommendation for beginners.
- The transition happens at Week 5, when the student needs files, imports, and testing — things notebooks can't do well

**Course Delivery:**
- Weeks 0–4: Lesson notebooks hosted on GitHub, opened via Colab links
- Weeks 5–7: Replit projects (student creates free Replit account)
- Python Tutor links embedded where visualization helps

**Supplementary Reading:**
- **Real Python** (realpython.com) remains the primary supplementary resource for anyone who wants deeper coverage. Read *after* lesson notebooks, not before.
- Supplementary reading is now truly optional. The curriculum is designed to stand alone in 8 weeks. Extra reading is for reinforcement if a concept doesn't land.
- See Appendix C for the condensed reading guide.

**Where This Curriculum Ends — Where Carson's Guide Begins:**
After Week 7, the student has: basic Python literacy, understanding of how code works, testing instincts, Git awareness, and hands-on experience with Claude Code. They're ready to follow Carson's playbook: think of something fun to build, build it with Claude Code in Replit, deploy it. Everything else is just-in-time learning — ask the AI when you need to know something.

---

# WEEK 0: Getting Started

**No installation required. Everything runs in the browser.**

## Lesson 0.1: Opening Your First Notebook

**Duration:** 30 minutes

**Notebook provided:** `00_1_first_notebook.ipynb`

**Learning Objectives:**
- Open a Colab notebook from a link
- Run a code cell
- Understand what just happened

**Content (in notebook markdown cells):**

**What is Google Colab?**
- A website where you can write and run Python code
- Python runs on Google's computers, not yours
- Your work saves to your Google Drive
- You need a Google account (Gmail)

**What is Python?**
- A program that reads and executes code you write
- You write instructions; Python carries them out
- Colab gives you access to Python through your browser

**What is a notebook?**
- A document with "cells" — blocks of code or text
- Code cells: contain Python code you can run
- Text cells: contain explanations (like this one)
- You run a code cell by clicking the play button ▶ or pressing Shift+Enter
- The output appears directly below the cell

**First exercise (in code cells):**
```python
# Cell 1 — Click the play button or press Shift+Enter
2 + 3
```
Output: `5`

```python
# Cell 2 — Try these
10 - 2
```

```python
# Cell 3
6 * 7
```

```python
# Cell 4
15 / 3
```

- Explanation: each cell sent code to Python, Python evaluated it, and the result appeared below
- The last expression in a cell is automatically displayed

**Saving:**
- Colab auto-saves to your Google Drive
- You can also File → Save (or Ctrl+S / Cmd+S)
- Close the tab, come back later — your work is still there

---

## Lesson 0.2: Variables, Types, and Cells

**Duration:** 1.5 hours

**Notebook provided:** `00_2_variables_and_cells.ipynb`

**Learning Objectives:**
- Create variables
- Know the basic types: int, float, str, bool
- Understand that cells share state
- Know the critical rule about execution order
- Use `print()` to display multiple values

**Content (in notebook):**

**Variables:**
```python
# Cell 1 — Create a variable
x = 10
```
(No output — assignment doesn't display anything)

```python
# Cell 2 — Use the variable
x
```
Output: `10`

```python
# Cell 3 — Variables created in earlier cells are available
x + 5
```
Output: `15`

```python
# Cell 4 — Strings
name = "John"
name
```

```python
# Cell 5 — Using print() to show multiple things
x = 10
y = 20
print(x)
print(y)
print(x + y)
```

**The type() function:**
```python
type(5)         # int
type("hello")   # str
type(3.14)      # float
type(True)      # bool
```

**⚠️ THE CRITICAL RULE: Execution Order**

Cells run in the order YOU click them, not the order they appear on screen. This can cause confusion.

**Rule: When confused, use Runtime → Restart and run all**
This runs every cell from top to bottom, starting completely fresh.
Develop this habit. Use it often.

**Exercises:**
- Create variables of different types
- Use `type()` on each
- Deliberately cause the execution-order problem, then fix it with "Restart and run all"
- Use `print()` to display multiple values in one cell

---

## Lesson 0.3: Python Tutor

**Duration:** 30 minutes

**Notebook provided:** `00_3_python_tutor.ipynb`

**Learning Objectives:**
- Access pythontutor.com
- Understand what it visualizes
- Know when to use it alongside notebooks

**Content:** Same as v6. Python Tutor shows objects in memory, variables pointing to objects, execution order. Workflow: try in notebook → if confused → paste into Python Tutor → step through → return to notebook.

---

# WEEK 1: How Python Actually Works — Objects and References

**Supplementary Reading (optional, after completing notebooks):**
- **Real Python:** "Variables in Python: Usage and Best Practices" — Teaches variables as references, uses `id()`.
- **Launch School (free):** "Variables as Pointers" chapter — Almost identical to this week's content.
- **Ned Batchelder (free):** "Facts and Myths about Python Names and Values" PyCon talk — Watch first 12 minutes only.

## Lesson 1.1: Python Creates Objects

**Duration:** 1 hour

**Notebook provided:** `01_1_objects.ipynb`

**Learning Objectives:**
- Understand that Python stores data as objects in memory
- Use `id()` to see object addresses
- Know that `type()` returns the type of object

**Key Concepts:**
- When you write `x = 5`, Python creates an integer object containing 5
- This object is stored at a memory address
- The name `x` refers to that memory address
- `id()` returns the memory address

**Notebook exercises:** Create objects, check `id()` and `type()`, observe small integer caching.

---

## Lesson 1.2: Variables Are References, Not Containers

**Duration:** 1 hour

**Notebook provided:** `01_2_references.ipynb`

**Learning Objectives:**
- Understand variables are names that reference objects
- Distinguish identity (`is`) from equality (`==`)
- Know that reassignment creates a new reference, not a new copy

**Key Concepts:**
- `y = x` makes y refer to the same object as x
- `is` checks identity (same object), `==` checks equality (same value)
- Integers are immutable — `x = x + 1` creates a NEW object
- Reassignment changes what the variable points to; other variables are unaffected

**Why this matters for AI-generated code:** When AI writes code that passes data between functions, you need to know whether the function got the same object or a copy. This is the single most common source of subtle bugs in Python.

**Notebook exercises:** Aliasing demo, `id()` checks, immutability of integers and strings, f-string formatting basics.

---

## Lesson 1.3: Strings and Formatting

**Duration:** 1 hour

**Notebook provided:** `01_3_strings.ipynb`

**Learning Objectives:**
- Know that strings are immutable
- Use f-strings for formatting
- Use common string methods

**Key Concepts:**
- `.upper()`, `.replace()` etc. return NEW strings (check with `id()`)
- f-strings: `f"Hello, {name}"`
- Number formatting: `f"{bmi:.1f}"`
- `.split()`, `.join()`, `.strip()`, `len()`

---

# WEEK 2: Control Flow

**Supplementary Reading (optional):**
- **Real Python:** "Python for Loops: The Pythonic Way" and "Python while Loops"

## Lesson 2.1: Booleans and Conditionals

**Duration:** 1.5 hours

**Notebook provided:** `02_1_conditionals.ipynb`

**Learning Objectives:**
- Use comparison operators
- Write if/elif/else chains
- Understand indentation

**Key Concepts:**
- `bool` type: `True`, `False`
- Comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`
- `if`/`elif`/`else` — conditions evaluated top to bottom, first True wins
- `and`, `or`, `not`
- Truthy/falsy (brief): `0`, `""`, `None`, `[]` are falsy

**Exercises:** BMI categorization, temperature checks, intentional indentation errors.

---

## Lesson 2.2: Loops

**Duration:** 1.5 hours

**Notebook provided:** `02_2_loops.ipynb`

**Learning Objectives:**
- Use `for` loops with `range()`
- Iterate over lists (preview — lists formally taught Week 4)
- Use `while` loops
- Know `break` and `continue`

**Key Concepts:**
- `for i in range(n)` iterates n times
- `for item in some_list:` iterates over elements
- `while condition:` repeats while True
- `break` exits, `continue` skips to next

**Exercises:** Print numbers, sum 1–100, countdown, simple number guessing game with `input()`.

---

# WEEK 3: Functions

**Supplementary Reading (optional):**
- **Real Python:** "Pass by Reference in Python: Best Practices"

## Lesson 3.1: Defining and Calling Functions

**Duration:** 1.5 hours

**Notebook provided:** `03_1_functions.ipynb`

**Learning Objectives:**
- Write function definitions
- Call functions and use return values
- Understand return vs print
- Know that functions without `return` return `None`

**Key Concepts:**
- `def function_name(parameters):` defines a function
- `return` sends value back; no `return` → `None`
- Parameters = names in definition; arguments = values passed in
- Docstrings: `"""What this function does."""`

**Exercises:**
- Write `calculate_bmi()`, test with multiple inputs
- Show difference: function that returns vs function that only prints
- Write functions with docstrings

---

## Lesson 3.2: Scope and Parameter Passing

**Duration:** 1.5 hours

**Notebook provided:** `03_2_scope.ipynb`

**Learning Objectives:**
- Know that local variables exist only inside the function
- Parameters receive references, not copies
- Reassigning a parameter does NOT affect the caller

**Key Concepts:**
- Each call creates a frame; frame destroyed on return
- Local variables are invisible outside the function
- Same `id()` for parameter and argument (pass-by-assignment)
- Immutable args: can't modify, only reassign → caller unaffected
- Mutable args (preview): modifications affect caller

**Note:** "We'll see mutable objects (lists, dicts) in Week 4. For now, just know: integers and strings can't be modified in place, so functions can't accidentally change the caller's data."

**Exercises with Python Tutor links for visualizing stack frames.**

---

# WEEK 4: Data Structures

**This week covers lists and dictionaries — the two data structures you'll encounter most in AI-generated code.**

**Supplementary Reading (optional):**
- **Real Python:** "Python's list Data Type: A Deep Dive" and "Dictionaries in Python"

## Lesson 4.1: Lists

**Duration:** 1.5 hours

**Notebook provided:** `04_1_lists.ipynb`

**Learning Objectives:**
- Create lists and access elements
- Know that lists are mutable — and what that means
- Use common list operations
- Iterate over lists with `for`

**Key Concepts:**
- Ordered sequences, zero-indexed
- `list[-1]` is last element, `list[1:3]` is a slice
- Lists are mutable: `.append()`, `.remove()`, `.pop()`, element assignment
- Mutating methods return `None` (the `x = list.sort()` trap)
- `id()` stays same after mutation — same object, changed contents
- Aliasing: `list2 = list1` → same object. Fix with `.copy()`
- List comprehensions: `[expr for item in items]` and `[expr for item in items if condition]`

**Why this matters for AI-generated code:** AI frequently generates list comprehensions. You need to be able to read them. AI also frequently creates accidental aliasing bugs — knowing the `id()` check saves hours of confusion.

**Exercises:** Create, modify, iterate. Demonstrate aliasing. Convert a loop to a comprehension. BMI calculation from lists of weights and heights.

---

## Lesson 4.2: Dictionaries and Nested Data

**Duration:** 1.5 hours

**Notebook provided:** `04_2_dicts.ipynb`

**Learning Objectives:**
- Create dictionaries and access values
- Use `.get()` for safe access
- Iterate with `.keys()`, `.values()`, `.items()`
- Work with lists of dicts (the "records" pattern)

**Key Concepts:**
- Key-value pairs: `{"name": "Alice", "bmi": 22.1}`
- Keys must be immutable; dicts are mutable
- `.get(key, default)` avoids KeyError
- `for key, value in dict.items():` iterates over pairs
- Lists of dicts: `patients[0]["name"]` — the most common data shape in real applications

**Why this matters:** Almost every API, database, and AI-generated data handler uses dicts or lists of dicts. This is the shape of real-world data.

**Exercises:** Build patient records as list of dicts, iterate and filter, BMI calculations on patient data.

---

## Lesson 4.3: Mutable vs Immutable — The Mental Model

**Duration:** 45 minutes

**Notebook provided:** `04_3_mutability.ipynb`

**Learning Objectives:**
- Classify built-in types as mutable or immutable
- Know why it matters for functions
- Know how to avoid accidental mutation

**Key Concepts:**
- Immutable: `int`, `float`, `str`, `bool`, `tuple`
- Mutable: `list`, `dict`, `set`
- Aliasing is safe with immutable, dangerous with mutable
- Copy inside function if you don't want to modify the original
- Tuple: immutable sequence (brief intro)

**This is the consolidation lesson** — ties together objects, references, mutability, and functions into one mental model.

---

# WEEK 5: Scripts, Imports, Testing, and Git

**This is the transition week. The student moves from Colab notebooks to Replit — a browser-based development environment with a real file system, terminal, and package manager. No local installation required.**

## Lesson 5.1: Setting Up Replit

**Duration:** 45 minutes

**Learning Objectives:**
- Create a Replit account
- Create a Python project (called a "Repl")
- Understand files, the editor, and the terminal
- Run a Python script

**Content:**

**Why Replit?**
- A website where you write code in files and run them — like having a full computer in your browser
- Has a file system (folders and .py files), an editor, and a terminal
- Can install packages, run tests, deploy apps
- Ryan Carson's #1 recommendation for beginners: "Replit takes care of all the complexity"
- You'll still use Colab for quick experiments — it doesn't go away

**Setup:**
1. Go to replit.com, create free account
2. Create new Repl → Python template
3. You'll see: file panel (left), editor (center), terminal/output (right)

**Key differences from notebooks:**

| Colab Notebook | Replit Script (.py) |
|----------------|---------------------|
| Last expression auto-displayed | Must use `print()` |
| Cells run individually | File runs top to bottom |
| State persists between cell runs | State resets each run |
| Good for exploration | Good for reusable programs |
| Can't import between files | Can import between files |
| Can't run pytest | Can run pytest |

**First script — create `hello.py`:**
```python
name = "John"
age = 45
print(f"Hello, {name}! You are {age} years old.")
```
Click Run (or type `python hello.py` in terminal).

**Exercises:**
- Create `hello.py`, run it
- Create `bmi_calc.py` with `calculate_bmi()` function, call it, print result
- Deliberately forget `print()` — observe no output

---

## Lesson 5.2: Imports and Modules

**Duration:** 45 minutes

**Learning Objectives:**
- Understand that modules are .py files
- Import from your own scripts
- Know `if __name__ == "__main__":`

**Key Concepts:**
- `import module` → use as `module.function()`
- `from module import function` → use directly
- `if __name__ == "__main__":` — code that only runs when executed directly, not when imported
- Standard library exists (math, random, datetime) — but agents pick libraries for you, so don't memorize

**Exercises in Replit:**
- Create `bmi.py` with functions and main guard
- Create `main.py` that imports from `bmi.py`
- Observe: code in imported module runs on import (why `if __name__` matters)

---

## Lesson 5.3: Testing with pytest

**Duration:** 1.5 hours

**Learning Objectives:**
- Understand why testing matters
- Write test functions with pytest
- Run tests in Replit's terminal
- Know the Red → Green → Refactor cycle

**Key Concepts:**
- Tests verify your code works correctly
- `assert condition, "message"` — crashes if false
- pytest: test functions start with `test_`, test files start with `test_`
- `pytest.raises()` for expected errors
- Run: `pytest -v` in terminal

**Why testing matters for AI-generated code:** AI coding agents generate code that *looks* right but may have bugs, miss edge cases, or handle errors poorly. Writing tests is how you verify that generated code actually works. Carson explicitly calls out TDD as a foundational concept.

**Red → Green → Refactor (brief):**
1. Write a test that fails (Red)
2. Write code to make it pass (Green)
3. Improve the code (Refactor) — tests still pass

**In Replit:**
1. In terminal: `pip install pytest`
2. Create `test_bmi.py`:
```python
from bmi import calculate_bmi, categorize_bmi

def test_normal_bmi():
    result = calculate_bmi(70, 1.75)
    assert 22.0 < result < 23.0

def test_categorize_normal():
    assert categorize_bmi(22.0) == "normal"

def test_categorize_obese():
    assert categorize_bmi(35.0) == "obese"

def test_zero_height():
    """Should handle zero height gracefully."""
    # What should happen here? Think before coding.
```
3. Run: `pytest -v`

**Exercises:**
- Write tests for `calculate_bmi()`: normal, edge cases, invalid input
- TDD mini-exercise: write `test_categorize_bmi()` first, then implement `categorize_bmi()`
- Observe a test failing, then fix the code

---

## Lesson 5.4: Git — Version Control Hands-On

**Duration:** 1.5 hours

**Learning Objectives:**
- Know what version control is and why it exists
- Use core Git commands: `init`, `status`, `add`, `commit`, `log`, `diff`
- Create and switch branches
- Understand what AI agents are doing when they say "I'll commit this" or "I'll create a branch"

**Content:**

**What is Git?**
- A tool that tracks every change to your code over time
- Every set of changes is a "commit" — a snapshot you can return to
- You can go back to any previous commit, see exactly what changed, and undo mistakes

**What is GitHub?**
- A website that stores your Git history in the cloud
- Lets you share code, collaborate, and back up your work
- AI coding agents (Claude Code in particular) use GitHub constantly

**Hands-on: Your first repository (in Replit's terminal):**

Replit Repls come with Git pre-installed. Open the Shell tab and follow along.

```bash
# Step 1: See what Git knows about your project
git status
```
Replit may have already initialized Git. If you see "not a git repository", run `git init`.

```bash
# Step 2: Tell Git who you are (one-time setup)
git config user.name "Your Name"
git config user.email "you@example.com"
```

```bash
# Step 3: See what files exist but aren't tracked yet
git status
```
You'll see your .py files listed in red under "Untracked files." Git sees them but isn't tracking their changes yet.

```bash
# Step 4: Tell Git to track your files
git add bmi.py test_bmi.py
git status
```
Now they're green under "Changes to be committed." You've *staged* them — told Git "include these in the next snapshot."

```bash
# Step 5: Take the snapshot (commit)
git commit -m "Add BMI calculator and tests"
```
The `-m` flag is your commit message — a short note about what this snapshot contains. Write these like you're leaving a note for your future self.

```bash
# Step 6: See your history
git log
```
You'll see your commit with its message, author, date, and a long hex string (the commit ID — a unique fingerprint for this snapshot).

```bash
# Step 7: Make a change, see what Git notices
```
Edit `bmi.py` — add a new function or change an existing one. Then:

```bash
git status
```
Git shows `bmi.py` in red under "Changes not staged for commit" — it knows the file changed since the last snapshot.

```bash
# Step 8: See exactly what changed
git diff
```
Lines starting with `+` were added. Lines starting with `-` were removed. This is how you (and AI agents) review what happened.

```bash
# Step 9: Stage and commit the change
git add bmi.py
git commit -m "Add input validation to calculate_bmi"
```

```bash
# Step 10: See both commits in history
git log --oneline
```
Two snapshots. You can go back to either one at any time.

**Branches:**

A branch is a separate line of work. The main branch (called `main`) is your working code. You create a branch to try something without risking the working version.

```bash
# See what branch you're on
git branch

# Create a new branch and switch to it
git checkout -b add-risk-score
```
You're now on a branch called `add-risk-score`. Everything you do here is separate from `main`.

```bash
# Make changes, commit them
# (edit analysis.py, add a risk score function)
git add analysis.py
git commit -m "Add risk score calculation"
```

```bash
# Switch back to main
git checkout main
```
Look at your files — the risk score changes are gone. They're safely on the other branch.

```bash
# Merge the branch into main (bring the changes in)
git merge add-risk-score
```
Now main has the risk score changes. The branch did its job.

```bash
# Clean up — delete the branch
git branch -d add-risk-score
```

**Why this matters for AI coding agents:**
When Claude Code says "I'll create a branch for this feature," it's running `git checkout -b feature-name`. When it says "I'll commit this," it's running `git add` and `git commit`. When it opens a "pull request," it's asking to merge a branch back into main — with a review step in between. You now know exactly what's happening under the hood.

Carson keeps three copies of his codebase in different folders — one on `main` for hotfixes, two on feature branches for parallel work. That workflow is just this lesson repeated across folders.

**Key commands reference (keep this handy, don't memorize):**

| Command | What it does |
|---------|-------------|
| `git status` | Show what's changed since last commit |
| `git add <file>` | Stage a file for the next commit |
| `git commit -m "msg"` | Take a snapshot with a message |
| `git log --oneline` | Show commit history (compact) |
| `git diff` | Show what changed (unstaged) |
| `git branch` | List branches |
| `git checkout -b <name>` | Create and switch to a new branch |
| `git checkout main` | Switch back to main |
| `git merge <branch>` | Merge a branch into current branch |
| `git clone <url>` | Download a repo from GitHub |

---

# WEEK 6: Error Handling and Reading Code

## Lesson 6.1: Reading Error Messages

**Duration:** 45 minutes

**Notebook provided:** `06_1_errors.ipynb` (back in Colab — errors are best explored interactively)

**Learning Objectives:**
- Read a stack trace (bottom up)
- Recognize common errors by name
- Know that the error message tells you what happened and where

**Key errors:**
- `NameError` — used a variable that doesn't exist
- `TypeError` — wrong type (e.g., `"5" + 3`)
- `ValueError` — right type, wrong value
- `KeyError` — dict key doesn't exist
- `IndexError` — list index out of range
- `AttributeError` — object doesn't have that method
- `ZeroDivisionError`

**Exercises:** Trigger each error deliberately, read the traceback, identify the problem line.

---

## Lesson 6.2: try/except and Defensive Code

**Duration:** 1 hour

**Notebook provided:** `06_2_error_handling.ipynb`

**Learning Objectives:**
- Use try/except to catch errors
- Catch specific types — never bare `except:`
- Raise your own errors with `raise`

**Key Concepts:**
- `try/except` prevents crashes on expected errors
- Always catch specific types: `except ValueError as e:`
- `raise ValueError("message")` for your own validation
- try/except/else/finally (brief)

**Why this matters for AI-generated code:** AI-generated code often has weak error handling — missing validation, bare `except:` blocks, or no handling at all. Recognizing this is one of the most important review skills.

---

## Lesson 6.3: Reading AI-Generated Code

**Duration:** 1.5 hours

**Learning Objectives:**
- Read a multi-file program top to bottom
- Trace data flow through functions
- Identify what's missing: error handling, edge cases, docstrings
- Evaluate whether code does what it claims

**Content:**

**How to read code you didn't write:**
1. Start with the entry point (usually `main.py` or the file you run)
2. Read function signatures and docstrings first — understand the interface
3. Trace data flow: what goes in, what comes out
4. Look for: error handling, edge cases, assumptions

**Exercise — review this AI-generated code:**

(Provide a realistic function generated by an AI agent — something that works for the happy path but has typical gaps. Student identifies issues, writes tests that expose the bugs, then improves the code.)

```python
def calculate_average_bmi(patients):
    bmis = []
    for patient in patients:
        bmi = patient['weight'] / (patient['height'] ** 2)
        bmis.append(bmi)
    return sum(bmis) / len(bmis)
```

**Student review:**
- ❌ No handling for missing keys
- ❌ No validation for zero/negative values
- ❌ Crashes on empty list (ZeroDivisionError)
- ❌ No docstring

**Student writes tests, then improves the function.** This is the core skill of the entire curriculum.

---

# WEEK 7: AI Coding Tools and How LLMs Work

## Lesson 7.1: How Large Language Models Work

**Duration:** 1 hour

**Notebook provided:** `07_1_llms.ipynb`

**Learning Objectives:**
- Know what tokens are
- Understand next-token prediction at a basic level
- Know what training does (adjust weights through corrections)
- Understand why LLMs can be confidently wrong

**Content:**

**Why this lesson exists:** Ryan Carson's #1 recommendation, above everything else: "Because you're using the tool, it helps to understand how the tool works."

**Tokens:**
- LLMs don't read words — they read "tokens" (pieces of words)
- "understanding" might be split into "under" + "standing"
- This affects how the model processes your requests

**Next-token prediction:**
- At its core, an LLM predicts: "given everything so far, what word comes next?"
- If you say "peanut butter and..." → "jelly" (high probability)
- The model does this one token at a time, thousands of times per response
- That's why it can write code — it's predicting what token should come next based on patterns in its training data

**Training:**
- The model saw billions of examples of text (including code)
- Through millions of corrections, it learned patterns: "when you see this, the next token is probably that"
- The underlying math is matrix multiplication with "weights" — numbers that were adjusted during training
- Weights encode patterns, not facts. The model doesn't "know" things — it has patterns that produce correct-seeming output

**Why LLMs can be confidently wrong:**
- The model always produces the most probable next token
- It can't say "I don't know" the way a human can — it generates something
- This is why reviewing AI-generated code is essential, not optional
- The code will look correct. It will be syntactically valid. It may still have logic bugs.

**Exercises:**
- Open ChatGPT or Claude and ask: "How does a large language model work?" Have a 10-minute conversation. (This is Carson's literal homework assignment.)
- Ask the AI to generate a simple Python function, then review it for issues.

---

## Lesson 7.2: Working with Claude Code

**Duration:** 2 hours

**Learning Objectives:**
- Install and use Claude Code
- Generate code, review it, test it, improve it
- Know basic security hygiene
- Understand the build → review → test → improve workflow

**Content:**

**Setting up Claude Code in Replit:**

Replit has Node.js built in, so installation is one command in the terminal:
```bash
npm install -g @anthropic-ai/claude-code
```

Then start it:
```bash
claude
```

Claude Code is a terminal-based coding agent. You type natural language requests, it generates code, creates files, runs commands — and you review everything it does. It works directly in your Replit project's file system.

**The workflow:**
1. **Describe what you want** — be specific. "Write a function that calculates BMI from a patient dict with 'weight' and 'height' keys, returns None for invalid input" beats "write a BMI function."
2. **Review every line** — read the generated code. Do you understand it? If not, ask Claude Code "explain this line" or "what does this function do?"
3. **Write tests** — before you trust the code, write tests. Normal cases, edge cases, error cases.
4. **Identify gaps** — error handling? Docstrings? Edge cases? What did Claude Code miss?
5. **Improve it** — fix the issues yourself or ask Claude Code to fix them with specific instructions.

**Security hygiene (Carson's #2):**
- **The prompt to memorize:** "Am I doing anything dumb? Look through my code and tell me if we've made any stupid mistakes."
- Run this regularly. Especially before deploying anything.
- Never put API keys or passwords in your code files
- "You don't know what you don't know" — ask Claude Code to check

**Exercise — full workflow:**

Request in Claude Code:
> "Write a patient data analysis module. Given a list of patient dicts (each with 'name', 'weight', 'height', and 'risk_score'), write functions to: calculate BMI for each patient, categorize patients by risk level, identify patients needing follow-up (risk >= 3 or BMI outside 18.5–30), and return a summary dict."

Then:
1. Review the generated code line by line
2. Write comprehensive tests (at least 8 test cases)
3. Identify what Claude Code got wrong or missed
4. Fix the issues
5. Run `pytest -v` — all pass
6. Run the security check prompt

**Evaluation:**
- ☐ Can explain every line of the generated code
- ☐ Identified at least 3 issues in the AI-generated version
- ☐ Wrote tests that catch those issues
- ☐ Fixed the issues
- ☐ All tests pass
- ☐ Ran the security hygiene check

---

## Lesson 7.3: What's Next — Carson's Playbook

**Duration:** 30 minutes (reading + reflection)

**Content:**

**You now have:**
- Python literacy — you can read and understand code
- The object/reference model — you know how Python actually works
- Testing instincts — you verify before you trust
- Git awareness — you know what version control is and why it matters
- AI collaboration skills — you can direct, review, and improve AI-generated code
- LLM understanding — you know what the tool is doing under the hood

**Carson's next steps (do these now):**

1. **Think of something fun to build.** Not useful — fun. A game, a joke app, a gift for someone.
2. **Build it in Replit with Claude Code.** Talk to it like a colleague. When confused about a concept, ask Claude Code to explain — or open claude.ai in another tab for a side conversation while the build continues.
3. **Deploy it.** In Replit, this is one click. Get something live on the internet.
4. **Learn just-in-time.** You don't need to take another course. When you hit something you don't understand, ask Claude Code. That's the new learning model.

**Resources:**
- Ryan Carson's guide: theneuron.ai/explainer-articles/how-to-learn-to-code-2026-ryan-carson-guide/
- Carson on X: @ryancarson (daily AI coding workflow posts)
- Claude Code docs: docs.claude.com
- Replit: replit.com
- v0 (Vercel): v0.app — another great option for building and deploying web apps

---

# Appendix A: Tools Summary

**Phase 1 (Weeks 0–4) — Browser only, no accounts except Google:**
- Google Colab (colab.research.google.com)
- Python Tutor (pythontutor.com)
- Course notebooks on GitHub with Colab launch links

**Phase 2 (Weeks 5–7) — Browser only, Replit account:**
- Replit (replit.com) — free tier is sufficient
- pytest (installed in Replit via `pip install pytest`)
- Claude Code (`npm install -g @anthropic-ai/claude-code` in Replit terminal)

**Always available:**
- Google Colab for quick experiments
- Python Tutor for visualization

---

# Appendix B: Common Pitfalls

**Conceptual:**
- ❌ Thinking variables "contain" values → Variables reference objects
- ❌ Confusing mutation with reassignment → Different operations
- ❌ `x = list.sort()` → x is `None` (mutating methods return `None`)

**Colab-specific:**
- ❌ Running cells out of order → Runtime → Restart and run all
- ❌ Session disconnected → Reconnect, or Restart and run all

**Replit/Script-specific:**
- ❌ Forgetting `print()` → Notebooks auto-display, scripts don't
- ❌ Forgetting to save before running

**With AI coding tools:**
- ❌ Trusting generated code without review → ALWAYS review
- ❌ Not testing generated code → ALWAYS test
- ❌ Not understanding generated code → ALWAYS understand
- ❌ Storing API keys in code → NEVER do this
- ❌ Bare `except:` in AI-generated code → Always catch specific types

---

# Appendix C: Supplementary Reading Guide (Condensed)

All optional. Read *after* the lesson notebook for that week if a concept didn't land.

**Real Python (paid, ~$20/month):**

| Week | Article | Why |
|------|---------|-----|
| **1** | "Variables in Python: Usage and Best Practices" | References, `id()`, identity vs equality |
| **2** | "Python for Loops: The Pythonic Way" | Loop mechanics |
| **3** | "Pass by Reference in Python: Best Practices" | Pass-by-assignment with `id()` |
| **4** | "Python's list Data Type: A Deep Dive" | Lists reference |
| **4** | "Dictionaries in Python" | Dicts reference |
| **4** | "Python's Mutable vs Immutable Types" | `id()`, aliasing, copying |

**Free resources:**

| Week | Resource | Why |
|------|----------|-----|
| **1** | Launch School: "Variables as Pointers" | Identical to Week 1 content |
| **1** | Ned Batchelder PyCon talk (first 12 min) | Authoritative, no analogies |
| **5** | pytest docs: "Get Started" | Short, practical pytest intro |
| **After** | "Automate the Boring Stuff" (automatetheboringstuff.com) | Natural next step: files, automation |

---

# Appendix D: What We Cut (and Why)

For anyone wondering what was in v6 that's no longer here:

| v6 Content | Why Cut |
|------------|---------|
| Turtle graphics throughout | Fun but adds 3+ weeks. Not needed for AI collaboration. |
| Local Python installation (Week 4) | Replaced by Replit. Installation is a barrier, not a learning objective. |
| VS Code setup (Week 5) | Replaced by Replit. Same barrier, same solution. |
| Lists deep dive — aliasing, shallow copy, comprehension edge cases (Week 6) | Compressed into Week 4. Core aliasing and comprehension basics kept; deep copy mechanics cut. |
| Standard library tour (Week 8) | Agents pick libraries. Learn just-in-time when you need a specific one. |
| Advanced functions — mutable defaults, LEGB full treatment (Week 8) | Mutable default pitfall mentioned briefly. Full LEGB is reference material, not foundation. |
| Extended error handling (Week 9) | Compressed into Week 6. Core try/except kept; else/finally are reference material. |
| Code quality week (Week 10) | Absorbed into code review lesson (6.3). Naming, docstrings, DRY mentioned where relevant. |
| 3-week project (Weeks 12–14) | Replaced by Week 7 AI-guided build exercise. The project was for building confidence writing code from scratch — but the goal is now AI collaboration, not solo development. |
| Extensive supplementary reading apparatus | Condensed to one appendix. Optional, not structural. |
| ColabTurtlePlus → standard turtle transition | Eliminated with turtle graphics. |
| `if __name__ == "__main__"` deep treatment | Brief coverage in 5.2. The concept matters; the ceremony around it is handled by agents. |
| Performance notes appendix | Premature optimization for this audience at this stage. |

**What we added:**
- How LLMs work (Lesson 7.1) — Carson's #1 recommendation
- Security hygiene throughout Week 7
- Git conceptual introduction (Lesson 5.4)
- Replit as the development environment
- AI code review as a core skill (Lesson 6.3)
- Explicit "what's next" bridging to Carson's playbook (Lesson 7.3)

---

# Appendix E: Replit Project Structure

```
python-foundations/         ← Replit project (Week 5+)
├── bmi.py                  # BMI functions with main guard
├── analysis.py             # Patient analysis functions
├── main.py                 # Entry point
├── test_bmi.py             # pytest tests for bmi.py
└── test_analysis.py        # pytest tests for analysis.py
```

The Colab notebooks (Weeks 0–4) remain on GitHub with launch links as in v6.

---

**END OF CURRICULUM OUTLINE — VERSION 7**

Total estimated time: 25–30 hours over 8 weeks
Assumes 3–4 hours of study per week
Prepares student to follow Carson's AI-assisted development playbook independently

# Lesson 7.2: Working with Claude Code

**Duration:** 2 hours

---

## What Is Claude Code?

Claude Code is a terminal-based AI coding agent. You type natural language requests, and it generates code, creates files, runs commands — all inside your project's file system. Unlike chatting with an AI in a browser, Claude Code operates directly on your code: it can read your files, write new ones, run your tests, and modify existing code.

It works inside Replit's terminal because it's a command-line tool, not a website.

---

## Setting Up in Replit

Replit has Node.js built in, so installation is one command. Open the **Shell** tab:

```bash
npm install -g @anthropic-ai/claude-code
```

Then start it:

```bash
claude
```

You'll see a prompt where you can type natural language requests. Claude Code is now running inside your project and can see all your files.

> **Authentication:** The first time you run `claude`, it will ask you to log in. Follow the prompts — your instructor will tell you which authentication method to use.
>
> **If the install command fails:** Replit's free tier sometimes blocks global installs. Try `npx @anthropic-ai/claude-code` instead — this runs Claude Code without installing it globally.

To exit Claude Code, type `/exit` or press Ctrl+C.

---

## The Workflow

This is the process you'll use every time:

### 1. Describe what you want — be specific

Bad request:
> "Write a BMI function."

Good request:
> "Write a function called `calculate_bmi` that takes a patient dict with 'weight' (kg) and 'height' (m) keys, returns the BMI as a float, returns None for invalid input (missing keys, non-numeric values, non-positive values), and includes a docstring."

The more specific your request, the better the output. Tell it:
- What the function should be called
- What inputs it takes (and their types/format)
- What it should return (including edge cases)
- What should happen with bad input
- Whether you want a docstring, type hints, etc.

### 2. Review every line

Claude Code will generate code and show it to you. Read it. Do you understand every line? If not, ask:

> "Explain what the `isinstance` check on line 12 does."

or:

> "What does this function do if the patient list is empty?"

Claude Code can explain its own output. Use this. Don't skip lines you don't understand.

### 3. Write tests

Before you trust the generated code, write tests. You know how to do this from Lesson 5.3:

- Normal cases — the happy path
- Boundary values — edges and limits
- Error cases — bad input, missing data, empty containers

Write the tests yourself. Don't ask Claude Code to write your tests — that defeats the purpose. If the same AI writes both the code and the tests, both will share the same assumptions and the same blind spots. A test only works as verification when it comes from a *different* perspective than the code it's testing. Your perspective as the reviewer is that different viewpoint.

### 4. Identify gaps

Run `pytest -v`. Look at what fails. Look at what passes but maybe shouldn't — are the tests thorough enough?

Common gaps in AI-generated code:
- Missing error handling (no try/except, no input validation)
- Bare `except:` blocks (catches everything, hides bugs)
- No handling for empty inputs
- Missing docstrings
- Assumed data format that won't always hold
- Security issues (hardcoded credentials, unsanitized input)

### 5. Improve it

Fix the issues yourself, or give Claude Code specific instructions:

> "Add input validation to `calculate_average_bmi`. It should return None if the patients list is empty or if no patients have valid weight and height values."

Specific fix requests work better than vague ones. "Make it better" gives you unpredictable results. "Add error handling for missing keys" gives you exactly what you asked for.

---

## Security Hygiene

Ryan Carson's #2 recommendation, right after understanding LLMs:

### The prompt to memorize

Ask Claude Code this regularly — especially before deploying anything:

> "Am I doing anything dumb? Look through my code and tell me if we've made any stupid mistakes."

This is Carson's literal phrasing, and it works. Claude Code will scan your files and flag issues.

### Rules

- **Never put API keys or passwords in your code files.** Use environment variables instead. If you see a line like `api_key = "sk-abc123..."` in generated code, that's a red flag.

  Here's what that looks like in practice:
  ```python
  # BAD — the key is visible in your code (and will end up in Git history)
  api_key = "sk-abc123..."

  # GOOD — the key is stored outside your code
  import os
  api_key = os.environ["API_KEY"]
  ```
  You don't need to understand the `os.environ` line yet — just know the rule: if you see a password or key written as a literal string in code, flag it.
- **Never commit secrets to Git.** If an API key ends up in a commit, it's in the history forever — even if you delete the file later.
- **"You don't know what you don't know."** This is Carson's mantra. Security is the area where beginners are most vulnerable, and where asking the AI to check your work has the highest payoff.

---

## Exercise: Full Workflow

Do this exercise end to end. It combines everything you've learned.

### Step 1: Generate code with Claude Code

Start Claude Code in your Replit Shell and make this request:

> "Write a patient data analysis module in a file called `analysis.py`. Given a list of patient dicts (each with 'name', 'weight', 'height', and 'risk_score' keys), write functions to: (1) calculate BMI for each patient, (2) categorize patients by risk level, (3) identify patients needing follow-up (risk_score >= 3 or BMI outside 18.5–30), and (4) return a summary dict with total patients, average BMI, count by risk category, and list of follow-up patients."

### Step 2: Review the generated code

Read every function. For each one, ask yourself:
- What goes in? What comes out?
- What happens with missing keys?
- What happens with empty lists?
- What happens with invalid values?
- Is there a docstring?

Write down your findings before moving to step 3.

### Step 3: Write tests

Create `test_analysis.py` and write at least 8 test cases:

- Normal case with valid data (multiple patients)
- Empty patient list
- Patient with missing keys
- Patient with zero or negative height/weight
- Patient with risk_score exactly 3 (boundary)
- Patient with BMI exactly 18.5 and exactly 30 (boundaries)
- All patients invalid
- Single patient (edge case for averages)

Run `pytest -v`.

### Step 4: Identify and fix issues

Compare your review notes (step 2) with the test results (step 3). Fix the code — either yourself or by giving Claude Code specific fix instructions.

### Step 5: Run the security check

In Claude Code:

> "Am I doing anything dumb? Look through all my code files and tell me if we've made any stupid mistakes."

### Step 6: Final verification

```bash
pytest -v
```

All tests pass. Your code is reviewed, tested, and security-checked.

---

## Evaluation Checklist

- ☐ Can explain every line of the generated code
- ☐ Identified at least 3 issues in the AI-generated version
- ☐ Wrote tests that catch those issues
- ☐ Fixed the issues (code passes all tests)
- ☐ All tests pass with `pytest -v`
- ☐ Ran the security hygiene check

---

## What You've Learned

You've just completed the full AI-assisted development cycle:

**Describe → Generate → Review → Test → Fix → Verify**

This is the workflow for everything you build from here on. The AI writes the first draft. You make it correct.

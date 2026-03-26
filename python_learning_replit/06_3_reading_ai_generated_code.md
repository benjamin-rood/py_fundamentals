# Lesson 6.3: Reading AI-Generated Code

**Duration:** 1.5 hours

---

## The Core Skill

This lesson is the reason the entire curriculum exists.

After this week, you'll start using AI coding agents to generate code. Those agents produce code that *looks* professional — correct syntax, reasonable structure, plausible logic. But "looks right" and "is right" are different things.

Your job is to read AI-generated code and find what's wrong with it before it causes problems. This is not optional. It's the single most important skill for anyone working with AI coding tools.

---

## How to Read Code You Didn't Write

When you open a file (or a function) you've never seen before, don't start at line 1 and read downward like a book. Instead:

### 1. Find the entry point

If it's a multi-file program, start with the file you'd run — usually `main.py` or whatever the script's entry point is. This tells you what the program does at the highest level.

### 2. Read function signatures and docstrings first

Before reading the body of a function, read its signature and docstring:

```python
def calculate_average_bmi(patients):
    """Calculate the average BMI for a list of patient dicts.
    
    Args:
        patients: List of dicts, each with 'weight' and 'height' keys.
    
    Returns:
        Average BMI as a float.
    """
```

From just this, you know: it takes a list of dicts, it expects 'weight' and 'height' keys, and it returns a float. You understand the *interface* before reading the *implementation*.

If there's no docstring — that's already a finding. Mark it.

### 3. Trace the data flow

Follow the data: what goes in? What gets transformed? What comes out?

```python
def calculate_average_bmi(patients):
    bmis = []                                          # empty list
    for patient in patients:                           # iterate over input
        bmi = patient['weight'] / (patient['height'] ** 2)  # compute
        bmis.append(bmi)                               # accumulate
    return sum(bmis) / len(bmis)                       # aggregate and return
```

Input → iteration → computation → accumulation → aggregation → output. That's the data flow.

### 4. Look for what's missing

This is where your training pays off. For every function, ask:

- **Error handling:** What happens with bad input? Missing keys? Wrong types? Empty lists?
- **Edge cases:** What about zero values? Negative numbers? One-element lists? `None`?
- **Assumptions:** What does this code assume about its inputs that might not always be true?
- **Docstrings:** Is the behavior documented?
- **Return values:** Does it return sensible values in all cases, or crash in some?

---

## Exercise: Review This AI-Generated Code

Below is a function that an AI coding agent might generate if asked: "Write a function to calculate the average BMI from a list of patient dicts."

Read it carefully. Then answer the questions that follow.

```python
def calculate_average_bmi(patients):
    bmis = []
    for patient in patients:
        bmi = patient['weight'] / (patient['height'] ** 2)
        bmis.append(bmi)
    return sum(bmis) / len(bmis)
```

### What's wrong with it?

Take a minute. Write down everything you notice before reading further.

---

Here's what a careful review finds:

**❌ No error handling for missing keys.**
If a patient dict is missing `'weight'` or `'height'`, this crashes with a `KeyError`. In real data, keys are often missing.

**❌ No validation for zero or negative values.**
If `height` is 0, this crashes with `ZeroDivisionError`. If `weight` is -10, you get a negative BMI — nonsensical but no error.

**❌ Crashes on empty list.**
If `patients` is an empty list `[]`, then `bmis` is empty, `sum(bmis)` is 0, `len(bmis)` is 0, and you get `ZeroDivisionError` on the division.

**❌ No docstring.**
No explanation of what the function does, what it expects, or what it returns.

**❌ No handling for non-numeric values.**
If `weight` or `height` is a string (e.g., `"seventy"`), this crashes with a `TypeError`.

That's five issues in six lines of code. The function works perfectly on the happy path — clean data, no missing values, non-empty list. But real data is never that clean.

---

## Write Tests That Prove the Bugs

Now write tests that expose each issue. Create a file called `test_average_bmi.py` in your Replit project:

```python
from analysis import calculate_average_bmi


def test_normal_case():
    """Happy path — should work."""
    patients = [
        {"weight": 70, "height": 1.75},
        {"weight": 80, "height": 1.80},
    ]
    result = calculate_average_bmi(patients)
    assert 23.0 < result < 26.0


def test_empty_list():
    """Empty list should return None, not crash."""
    result = calculate_average_bmi([])
    assert result is None


def test_missing_weight_key():
    """Missing 'weight' key should be handled, not crash."""
    patients = [{"height": 1.75}]
    result = calculate_average_bmi(patients)
    assert result is None


def test_missing_height_key():
    """Missing 'height' key should be handled, not crash."""
    patients = [{"weight": 70}]
    result = calculate_average_bmi(patients)
    assert result is None


def test_zero_height():
    """Zero height should not cause ZeroDivisionError."""
    patients = [{"weight": 70, "height": 0}]
    result = calculate_average_bmi(patients)
    assert result is None


def test_negative_weight():
    """Negative weight should be skipped."""
    patients = [
        {"weight": -10, "height": 1.75},
        {"weight": 70, "height": 1.75},
    ]
    result = calculate_average_bmi(patients)
    # Should only include the valid patient
    assert 22.0 < result < 24.0


def test_non_numeric_values():
    """Non-numeric values should be skipped, not crash."""
    patients = [
        {"weight": "seventy", "height": 1.75},
        {"weight": 70, "height": 1.75},
    ]
    result = calculate_average_bmi(patients)
    assert 22.0 < result < 24.0


def test_all_invalid_returns_none():
    """If every patient is invalid, return None."""
    patients = [
        {"weight": 0, "height": 1.75},
        {"height": 1.80},
    ]
    result = calculate_average_bmi(patients)
    assert result is None
```

If you run `pytest -v` with the original function, most of these tests will fail. That's the point — the tests prove the bugs exist.

---

## Write the Improved Version

Now create `analysis.py` with the improved function:

```python
def calculate_average_bmi(patients):
    """Calculate average BMI from a list of patient dicts.

    Args:
        patients: List of dicts with 'weight' (kg) and 'height' (m) keys.
                  Patients with missing, invalid, or non-positive values
                  are silently skipped.

    Returns:
        Average BMI as a float, or None if no valid patients.
    """
    if not patients:
        return None

    bmis = []
    for patient in patients:
        # Skip patients with missing keys
        if "weight" not in patient or "height" not in patient:
            continue

        weight = patient["weight"]
        height = patient["height"]

        # Skip non-numeric values
        # New function: isinstance() — isinstance(weight, (int, float)) asks Python:
        # "Is weight an int or a float?" It returns True or False. This is how you check
        # whether a value is the type you expect — you'll see it frequently in AI-generated
        # validation code.
        if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
            continue

        # Skip non-positive values
        # Why reject zero weight? A weight of zero produces a BMI of zero — no crash,
        # but medically meaningless. The improved version rejects non-positive values
        # because they can't represent real patient data. This is validation: catching
        # inputs that are technically allowed by Python but wrong for the domain.
        if weight <= 0 or height <= 0:
            continue

        bmis.append(weight / (height ** 2))

    if not bmis:
        return None

    return sum(bmis) / len(bmis)
```

Run `pytest -v`. All 8 tests should pass.

---

## The Pattern

This is the pattern you'll use every time AI generates code:

1. **Read** the generated code — understand the data flow
2. **Identify** what's missing — error handling, edge cases, docstrings
3. **Write tests** that expose the gaps
4. **Improve** the code until all tests pass

You've just done this pattern end to end. In Week 7, you'll do it again with Claude Code generating the code live.

---

## Exercises

1. **Complete the review exercise above** if you haven't already — write all 8 tests, see them fail against the original function, then write the improved version.

2. **Review this function** the same way:

```python
def find_high_risk_patients(patients):
    results = []
    for p in patients:
        if p['risk_score'] >= 3 or p['bmi'] > 30:
            results.append(p['name'])
    return results
```

What's wrong? Use the same checklist from earlier: What happens with missing keys? Empty list? Wrong types? `None` values? Then look at the logic itself: are the thresholds complete? Is the output format robust? You should find at least 4 issues. Write tests that prove each one, then fix the function.

3. **Run `pytest -v`** and don't stop until everything is green.

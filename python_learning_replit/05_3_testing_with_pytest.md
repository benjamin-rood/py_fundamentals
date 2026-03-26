# Lesson 5.3: Testing with pytest

**Duration:** 1.5 hours

---

## Why Testing Matters

You've been checking your code by running it and looking at the output. That works — until it doesn't. What happens when:

- You change a function and accidentally break something that used to work?
- You have 20 functions and need to verify all of them after a change?
- AI generates code that *looks* right but has a subtle bug?

Tests are code that checks your code. You run them, and they tell you: everything works, or this specific thing is broken. Automatically, every time, in seconds.

**Why testing matters for AI-generated code:** AI coding agents generate code that *looks* right but may have bugs, miss edge cases, or handle errors poorly. Writing tests is how you verify that generated code actually works. Ryan Carson explicitly calls out TDD (test-driven development) as a foundational concept.

---

## What Is a Test?

A test is a function that:
1. Calls your code with specific inputs
2. Checks that the output matches what you expect
3. Crashes loudly if it doesn't

The simplest version is `assert`:

```python
assert 2 + 2 == 4              # passes silently
assert 2 + 2 == 5, "Math broke" # crashes: AssertionError: Math broke
```

`assert condition, "message"` — if the condition is `False`, the program crashes and shows the message. If it's `True`, nothing happens. No news is good news.

---

## pytest: The Professional Testing Tool

`assert` works, but the professional tool is **pytest**. It finds your tests, runs them, and gives you a clear report.

### Installing pytest in Replit

Open the Shell tab and type:

```bash
pip install pytest
```

That's it. One command. Replit handles the rest.

### Writing your first test file

You should already have `bmi.py` from the last lesson. Now create a file called `test_bmi.py`:

```python
from bmi import calculate_bmi, categorize_bmi


def test_normal_bmi():
    """BMI for a 70kg, 1.75m person should be about 22.9."""
    result = calculate_bmi(70, 1.75)
    assert 22.8 < result < 23.0


def test_categorize_underweight():
    assert categorize_bmi(17.0) == "underweight"


def test_categorize_normal():
    assert categorize_bmi(22.0) == "normal"


def test_categorize_overweight():
    assert categorize_bmi(27.0) == "overweight"


def test_categorize_obese():
    assert categorize_bmi(35.0) == "obese"


def test_categorize_boundary_18_5():
    """18.5 is the lower boundary of 'normal'."""
    assert categorize_bmi(18.5) == "normal"


def test_categorize_boundary_25():
    """25.0 is the lower boundary of 'overweight'."""
    assert categorize_bmi(25.0) == "overweight"


def test_categorize_boundary_30():
    """30.0 is the lower boundary of 'obese'."""
    assert categorize_bmi(30.0) == "obese"
```

### Running tests

In the Shell:

```bash
pytest -v
```

The `-v` flag means "verbose" — it lists every test by name with pass/fail.

You should see something like:

```
test_bmi.py::test_normal_bmi PASSED
test_bmi.py::test_categorize_underweight PASSED
test_bmi.py::test_categorize_normal PASSED
test_bmi.py::test_categorize_overweight PASSED
test_bmi.py::test_categorize_obese PASSED
test_bmi.py::test_categorize_boundary_18_5 PASSED
test_bmi.py::test_categorize_boundary_25 PASSED
test_bmi.py::test_categorize_boundary_30 PASSED

8 passed
```

All green. Every test passed.

---

## The Rules

pytest has two simple rules:

1. **Test files** must start with `test_` (e.g., `test_bmi.py`)
2. **Test functions** must start with `test_` (e.g., `test_normal_bmi`)

That's how pytest finds your tests. Name things correctly, and `pytest -v` does the rest.

---

## What to Test

Good tests cover three categories:

### 1. Normal cases — the happy path
```python
def test_normal_bmi():
    result = calculate_bmi(70, 1.75)
    assert 22.8 < result < 23.0
```

### 2. Boundary values — the edges
```python
def test_categorize_boundary_18_5():
    """18.5 is exactly the boundary. Which category does it land in?"""
    assert categorize_bmi(18.5) == "normal"
```

Boundaries are where bugs hide. Here's why: Python's `<` operator means "strictly less than" — it does *not* include the value itself. So `bmi < 18.5` is `False` when `bmi` is exactly `18.5`, which means 18.5 falls through to the *next* branch (`elif bmi < 25`). If the programmer had written `<=` instead, 18.5 would stay in "underweight." Your test pins down exactly which choice was made — and catches it if someone changes the condition later.

### 3. Error cases — things that should fail gracefully

What happens if someone passes zero for height?

```python
def test_zero_height():
    """Should handle zero height without crashing."""
    # What should happen here? Think about it.
    # Option 1: Return None
    # Option 2: Raise a ValueError
    # Option 3: Crash with ZeroDivisionError (bad!)
```

Right now, `calculate_bmi(70, 0)` will crash with `ZeroDivisionError`. Is that acceptable? Probably not. You'd want it to either return `None` or raise a clear `ValueError`. This is exactly the kind of gap that tests help you find — and that AI-generated code often has.

### Testing for expected errors

If you decide `calculate_bmi` should raise a `ValueError` for zero height, you test that with `pytest.raises`:

```python
import pytest
from bmi import calculate_bmi

def test_zero_height_raises():
    """Zero height should raise ValueError, not ZeroDivisionError."""
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)
```

This test **passes** if `calculate_bmi(70, 0)` raises a `ValueError`, and **fails** if it doesn't. Right now, your `calculate_bmi` doesn't have that validation — so this test will fail. That's the point: the test found a gap. Now you fix the code.

**Two approaches, pick one.** The `pytest.raises` example above tests for a `ValueError`. The exercise below tests for returning `None`. These are two different design choices for handling bad input — your code should do one or the other, not both. The exercises below use the `return None` approach, which is simpler for now.

---

## Red → Green → Refactor

This is the TDD (Test-Driven Development) cycle:

1. **Red:** Write a test for something that doesn't work yet. Run `pytest -v`. The test fails. (Red.)
2. **Green:** Write the minimum code to make the test pass. Run `pytest -v`. It passes. (Green.)
3. **Refactor:** Clean up the code — better names, clearer structure, less repetition. Run `pytest -v`. Still passes.

Try it now:

> **Important:** If you're using the starter `bmi.py` file provided with this course, it already includes input validation. To experience the Red→Green cycle, temporarily remove the validation lines (the `if` block that checks for `<= 0`) so that `calculate_bmi(70, 0)` crashes with a `ZeroDivisionError`. You'll add them back in the "Green" step.
>
> If you built `bmi.py` yourself following Lesson 5.2, your version won't have validation yet — so this exercise will work as described.

### Red

Add this test to `test_bmi.py`:

```python
def test_zero_height_returns_none():
    """Zero height should return None."""
    assert calculate_bmi(70, 0) is None
```

Run `pytest -v`. It fails — `ZeroDivisionError`.

### Green

Open `bmi.py` and add validation:

```python
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index."""
    if height_m <= 0 or weight_kg <= 0:
        return None
    return weight_kg / (height_m ** 2)
```

Run `pytest -v`. All tests pass.

### Refactor

The code is already clean, but you could add more validation (non-numeric types, for example). If you change anything, run `pytest -v` again to make sure you didn't break something.

---

## Exercises

1. **Run the provided tests.** Use the starter files `bmi.py` and `test_bmi.py`. Run `pytest -v` and see all tests pass.

2. **Add edge case tests.** Add tests for:
   - Negative weight
   - Negative height
   - Very large BMI (e.g., weight=200, height=1.5)
   - Very small BMI (e.g., weight=40, height=2.0)

3. **TDD mini-exercise.** Write a test called `test_categorize_edge_zero_bmi` that checks what `categorize_bmi(0)` returns. Run `pytest -v` — what happens? Now think about it: the function raises a `ValueError` for *negative* BMI, but returns `"underweight"` for *zero* BMI. Is that consistent? Can a real person have a BMI of zero? Decide what the correct behavior should be, then modify `categorize_bmi` to handle it. Run `pytest -v` again — all tests pass.

4. **Observe a failure.** Temporarily break `categorize_bmi` — change `18.5` to `19.0` in the first condition. Run `pytest -v`. Read the failure output. Notice how pytest tells you exactly which test failed, what it expected, and what it got. Fix it back and re-run.

---

## What's Next

You now have a project with multiple files (`bmi.py`, `main.py`, `test_bmi.py`) and a way to verify everything works (`pytest -v`). Next lesson: Git — how to track changes to your code over time, and what's happening when AI agents say "I'll commit this."

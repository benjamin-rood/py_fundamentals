# Lesson 5.2: Imports and Modules

**Duration:** 45 minutes

---

## What Is a Module?

A module is a `.py` file. That's it.

When you created `bmi_calc.py` last lesson, you created a module. Any `.py` file can be imported by another `.py` file — which means any function you define in one file can be used in another.

This is the whole reason we moved from notebooks to Replit. Notebooks live alone. Scripts can work together.

---

## Importing Your Own Code

Let's build this from scratch.

### Step 1: Create the module

Create a file called `bmi.py` with the code below. (The starter `bmi.py` file included in this project is a later, improved version with input validation — you'll build up to that version in the next lesson. For now, type or paste this simpler version.)

```python
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index.
    
    Args:
        weight_kg: Patient's weight in kilograms
        height_m: Patient's height in meters
    
    Returns:
        BMI as a float
    """
    return weight_kg / (height_m ** 2)


def categorize_bmi(bmi):
    """Categorize a BMI value.
    
    Args:
        bmi: BMI value as a float
    
    Returns:
        Category string: 'underweight', 'normal', 'overweight', or 'obese'
    """
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


if __name__ == "__main__":
    # This code only runs when you execute: python bmi.py
    # It does NOT run when another file imports this module
    test_bmi = calculate_bmi(70, 1.75)
    print(f"Test BMI: {test_bmi:.1f}")
    print(f"Category: {categorize_bmi(test_bmi)}")
```

### Step 2: Run it directly

In the Shell:

```bash
python bmi.py
```

You should see:

```
Test BMI: 22.9
Category: normal
```

The code under `if __name__ == "__main__":` ran because you executed the file directly.

### Step 3: Import it from another file

Create a file called `main.py`:

```python
from bmi import calculate_bmi, categorize_bmi

# Use the imported functions
patients = [
    {"name": "Alice", "weight": 70, "height": 1.75},
    {"name": "Bob", "weight": 95, "height": 1.80},
    {"name": "Carol", "weight": 50, "height": 1.60},
]

for patient in patients:
    bmi = calculate_bmi(patient["weight"], patient["height"])
    category = categorize_bmi(bmi)
    print(f"{patient['name']}: BMI {bmi:.1f} ({category})")
```

Run it:

```bash
python main.py
```

You should see output for all three patients — and importantly, you should NOT see the "Test BMI: 22.9" line. That code is inside `if __name__ == "__main__":` in `bmi.py`, so it didn't run when `main.py` imported it.

---

## How `import` Works

When Python sees `from bmi import calculate_bmi`, it:

1. Finds `bmi.py` in the current directory
2. Runs all the top-level code in that file — function definitions get created, and any other top-level code (like bare print() calls) also executes
3. Makes `calculate_bmi` available in the importing file

**Important:** Python runs ALL the code in the module when it imports it. That's why any `print()` statements or function calls at the top level of the module will execute during import. The `if __name__ == "__main__":` guard prevents test/example code from running when the module is imported.

### `__name__` explained

Python sets a special variable called `__name__` for every module:

- When you run a file directly (`python bmi.py`): `__name__` is set to `"__main__"`
- When a file is imported (`from bmi import ...`): `__name__` is set to `"bmi"` (the module name)

So `if __name__ == "__main__":` means: "only run this code if I'm being executed directly, not imported."

Why does Python need this? Because every `import` runs the entire file (as you saw in step 2 above). Without a way to tell the difference between "am I being run directly?" and "am I being imported?", you couldn't put test code or examples in the same file as your functions — they'd run every time someone imported your module.

### Two import styles

```python
# Style 1: Import the module
import bmi
result = bmi.calculate_bmi(70, 1.75)  # prefix with module name
```

When you use `import bmi` (Style 1), Python gives you the whole module as a single object. To reach a function inside it, you write the module name, then a dot `.`, then the function name: `bmi.calculate_bmi(...)`. The dot means "look inside this object" — the same dot you saw with `type(x).__name__` in earlier lessons.

```python
# Style 2: Import specific functions
from bmi import calculate_bmi
result = calculate_bmi(70, 1.75)  # use directly
```

Both work. Style 2 is less typing; Style 1 makes it clear where the function came from. Use whichever is clearer for the situation.

---

## Standard Library (Brief)

Python comes with hundreds of built-in modules you can import without installing anything. These are the "standard library."

```python
import math
print(math.sqrt(16))        # 4.0
print(math.pi)              # 3.14159...

import random
print(random.randint(1, 10))  # random number 1-10

from datetime import date
print(date.today())          # today's date
```

You don't need to memorize these. AI coding agents pick the right library for you — and now you understand what they're doing when they write `import` at the top of a file. The key point: a line like `import math` loads a module, just like `import bmi` loads your own file. Same mechanism.

---

## Exercises

1. **Create `bmi.py`** with the functions above (or use the starter file). Run it directly with `python bmi.py` — see the test output.

2. **Create `main.py`** that imports from `bmi.py`. Run `python main.py` — verify the test output from `bmi.py` does NOT appear.

3. **Break the guard on purpose.** Move the test code in `bmi.py` *outside* the `if __name__ == "__main__":` block. Run `python main.py` again. Notice: now the test output appears when you import. Put it back inside the guard.

4. **Try both import styles.** Change `main.py` to use `import bmi` instead of `from bmi import ...`. Run both versions and see that they produce the same output.

---

## What's Next

Now that you can split code across files and import between them, you need a way to verify that your code actually works. That's testing — next lesson.

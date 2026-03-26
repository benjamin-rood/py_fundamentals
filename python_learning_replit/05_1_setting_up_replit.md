# Lesson 5.1: Setting Up Replit

**Duration:** 45 minutes

---

## What You're Doing This Week

Up to now, you've been learning Python inside Colab notebooks — running one cell at a time, seeing results immediately, reading explanations between code blocks. That's the best way to learn.

But to *build* things — real programs with multiple files, imports between them, tests that run from the command line — you need a different tool. You need a file system, a terminal, and the ability to run entire scripts at once. That's what Replit gives you.

**You're not leaving Colab behind.** It stays available for quick experiments, trying things out, or revisiting the earlier lessons. But from here forward, your primary workspace is Replit.

---

## What Is Replit?

Replit is a website where you write code in files and run them — like having a full computer in your browser. It gives you:

- **A file system** — folders and `.py` files, just like a real computer
- **An editor** — where you write code, with syntax highlighting and auto-indentation
- **A terminal** — a text-based command line where you run scripts, install packages, and run tests
- **Package management** — install Python libraries with `pip install`
- **No installation required** — everything runs in the browser

Ryan Carson's #1 recommendation for beginners: "Replit takes care of all the complexity."

---

## Setting Up

### Step 1: Create your account

1. Go to [replit.com](https://replit.com)
2. Click Sign Up
3. Create a free account (email or Google login)

The free tier is all you need for this course.

### Step 2: Create your first project

In Replit, a project is called a "Repl."

1. Click the **+ Create Repl** button (or **+** in the sidebar)
2. Choose **Python** as the template
3. Name it `python-foundations`
4. Click **Create Repl**

### Step 3: Understand the layout

You'll see three panels:

- **Left panel: Files** — this is your file system. You'll see `main.py` already created. You can create new files, new folders, rename, delete — just like on a computer.
- **Center panel: Editor** — this is where you write code. Click a file in the left panel to open it here.
- **Right panel: Terminal / Output** — this is where you run code and see results. The **Shell** tab gives you a terminal. The **Console** tab shows output when you click Run.

### Step 4: Run your first script

Click on `main.py` in the file panel. It might already have some code in it — delete it and type:

```python
print("Hello from Replit!")
```

Click the green **Run** button at the top. You should see `Hello from Replit!` in the output panel.

You can also run it from the terminal. Click the **Shell** tab in the right panel and type:

```bash
python main.py
```

Same result. The Run button and the terminal command do the same thing.

---

## Key Differences from Colab Notebooks

This is important. Scripts behave differently from notebook cells.

| Colab Notebook | Replit Script (.py) |
|----------------|---------------------|
| Last expression auto-displayed | Must use `print()` to see output |
| Cells run individually, in any order | File runs top to bottom, all at once |
| State persists between cell runs | State resets every time you run |
| Good for exploration and learning | Good for reusable programs |
| Importing between files is awkward and uncommon | Can import between files |
| Can't run pytest | Can run pytest |

When you run a `.py` file, Python reads it from the first line to the last, in order, exactly once. There's no concept of "run this cell again" — the entire file executes in one pass, then stops.

The biggest gotcha: **you must use `print()` to see output.** In a notebook, if the last line of a cell is `x`, the value of `x` appears automatically. In a script, `x` on its own line does nothing visible. You need `print(x)`. Why the difference? Notebooks have a built-in display step that automatically shows the result of the last expression in each cell. Scripts don't — they just execute and move on. If you want to see something, you have to explicitly tell Python to print it.

---

## Your First Real Script

Delete everything in `main.py` and type:

```python
name = "John"
age = 45
print(f"Hello, {name}! You are {age} years old.")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
```

Run it. You should see:

```
Hello, John! You are 45 years old.
Type of name: <class 'str'>
Type of age: <class 'int'>
```

This is exactly the kind of code you wrote in Week 0 — but now it's in a `.py` file running as a script.

---

## Creating Multiple Files

This is where Replit goes beyond notebooks. You can have multiple `.py` files in the same project.

1. In the file panel, click the **New File** icon (or right-click → New File)
2. Name it `bmi_calc.py`
3. Type:

```python
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index."""
    return weight_kg / (height_m ** 2)

# Test it
result = calculate_bmi(70, 1.75)
print(f"BMI: {result:.1f}")
```

4. Run it from the Shell tab: `python bmi_calc.py`

You now have two Python files in the same project. Next lesson, you'll learn how to import functions from one file into another — something notebooks can't do.

---

## Exercises

1. **Create `hello.py`** with a greeting that uses f-strings. Run it from the Shell.
2. **Create `bmi_calc.py`** with your `calculate_bmi()` function from Week 3. Call it with different values and print the results. Run it.
3. **Forget `print()` on purpose.** Put `calculate_bmi(70, 1.75)` as the last line *without* `print()`. Run it. Notice: no output. This is the #1 script gotcha.
4. **Use the Shell tab.** Type `python` to open a Python REPL right inside Replit. Type `2 + 3`. Type `exit()` to leave. The Shell is a full terminal — you can do anything here.

---

## What's Next

Next lesson, you'll learn how to import functions from one file into another — the thing that makes multi-file programs possible. This is why we needed Replit: notebooks can't do imports between files.

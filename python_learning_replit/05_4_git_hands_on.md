# Lesson 5.4: Git — Version Control Hands-On

**Duration:** 1.5 hours

---

## What Is Git?

Git is a tool that tracks every change to your code over time. Every set of changes is a "commit" — a snapshot you can return to. You can go back to any previous commit, see exactly what changed, and undo mistakes.

Think of it like the version history in Google Docs, but for code — and much more powerful.

## What Is GitHub?

GitHub is a website that stores your Git history in the cloud. It lets you share code, collaborate, and back up your work. AI coding agents — Claude Code in particular — use GitHub constantly.

Git is the tool. GitHub is the place where your history lives online. You'll use Git from the terminal; GitHub is a website you visit in the browser.

---

## Why This Matters

When Claude Code says "I'll commit this," it's running Git commands. When it says "I'll create a branch," it's using Git. When it opens a "pull request," it's asking to merge a branch into the main code — with a review step in between.

After this lesson, you'll know exactly what's happening under the hood. You won't need to be a Git expert — AI agents handle the complex stuff. But you need to understand the concepts so you can follow along and intervene when something goes wrong.

---

## Hands-On: Your First Repository

Replit Repls come with Git pre-installed. Open the **Shell** tab and follow along.

### Step 1: See what Git knows about your project

```bash
git status
```

Replit may have already initialized Git. If you see "fatal: not a git repository", run:

```bash
git init
```

### Step 2: Tell Git who you are

This is a one-time setup. Git stamps your name on every commit.

```bash
git config user.name "Your Name"
git config user.email "you@example.com"
```

### Step 3: See your untracked files

```bash
git status
```

You'll see your `.py` files listed in red under "Untracked files." Git sees them but isn't tracking their changes yet. They exist in the project, but Git doesn't have any snapshots of them.

### Step 4: Stage your files

"Staging" means telling Git: "include these files in the next snapshot."

Why not just commit directly? Because you don't always want to include *everything* you changed. You might have edited three files but only two of the changes are related to the same piece of work. Staging lets you select which changes belong together in one commit. You decide what goes in before you take the snapshot.

```bash
git add bmi.py test_bmi.py
git status
```

Now they're green under "Changes to be committed." You've staged them — they're ready for the snapshot.

You can also stage everything at once:

```bash
git add .
```

The `.` means "everything in the current directory."

### Step 5: Take the snapshot (commit)

```bash
git commit -m "Add BMI calculator and tests"
```

The `-m` flag is your commit message — a short note about what this snapshot contains. Write messages like you're leaving a note for your future self. "Fix bug" is bad. "Add input validation to calculate_bmi" is good.

### Step 6: See your history

```bash
git log
```

You'll see your commit with its message, author, date, and a long hex string (the commit ID — a unique fingerprint for this snapshot). Press `q` to exit the log view.

For a more compact view:

```bash
git log --oneline
```

One line per commit. Easier to scan.

### Step 7: Make a change, see what Git notices

Open `bmi.py` and add a new function — or change an existing one. Then:

```bash
git status
```

Git shows `bmi.py` in red under "Changes not staged for commit" — it knows the file changed since the last snapshot.

### Step 8: See exactly what changed

```bash
git diff
```

Lines starting with `+` were added. Lines starting with `-` were removed. This is how you (and AI agents) review what happened.

### Step 9: Stage and commit the change

```bash
git add bmi.py
git commit -m "Add input validation to calculate_bmi"
```

### Step 10: See both commits in history

```bash
git log --oneline
```

Two snapshots. You can go back to either one at any time.

---

## The Workflow

Every time you finish a chunk of work, the cycle is:

1. `git status` — see what changed
2. `git diff` — review the changes (optional but good practice)
3. `git add <files>` — stage the files you want to snapshot
4. `git commit -m "description"` — take the snapshot

That's it. Four commands. Everything else is built on top of this cycle.

---

## Branches

A branch is a separate line of work. The main branch (called `main`) is your working code. You create a branch to try something without risking the working version.

Why not just work on `main` directly? Because if your experiment breaks something, you've broken the only copy of your working code. A branch gives you a safe space to try things. If the experiment works, you merge it in. If it doesn't, you delete the branch and your working code on `main` is untouched.

### Create a branch and switch to it

```bash
git checkout -b add-risk-score
```

> **Note:** Newer versions of Git have a command called `git switch` that does the same thing as `git checkout` for branches. If you see an AI agent use `git switch -c feature-name`, that's the same as `git checkout -b feature-name`. Both work.

You're now on a branch called `add-risk-score`. Everything you do here is separate from `main`.

### Do some work on the branch

Edit or create `analysis.py` — add a risk score function, for example. Then commit:

```bash
git add analysis.py
git commit -m "Add risk score calculation"
```

### Switch back to main

```bash
git checkout main
```

Look at your files. The changes you made on the branch are gone — they're safely on the `add-risk-score` branch, not on `main`.

### Merge the branch into main

When you're happy with the work on the branch, bring it into main:

```bash
git merge add-risk-score
```

Now `main` has the risk score changes. The branch did its job.

### Clean up

```bash
git branch -d add-risk-score
```

The branch is deleted — the changes are already in `main`, so you don't need it anymore.

### See all branches

```bash
git branch
```

The one with `*` is the branch you're currently on.

---

## Why This Matters for AI Coding Agents

When Claude Code says:

- **"I'll create a branch for this feature"** — it's running `git checkout -b feature-name`
- **"I'll commit this"** — it's running `git add` and `git commit`
- **"I'll open a pull request"** — it's asking to merge a branch back into main, with a review step in between

Ryan Carson keeps three copies of his codebase in different folders — one on `main` for hotfixes, two on feature branches for parallel work. That workflow is just this lesson repeated across folders.

You now know exactly what's happening under the hood.

---

## Key Commands Reference

Keep this handy. Don't memorize — look it up when you need it.

| Command | What it does |
|---------|-------------|
| `git status` | Show what's changed since last commit |
| `git add <file>` | Stage a file for the next commit |
| `git add .` | Stage everything |
| `git commit -m "msg"` | Take a snapshot with a message |
| `git log --oneline` | Show commit history (compact) |
| `git diff` | Show what changed (unstaged) |
| `git branch` | List branches |
| `git checkout -b <name>` | Create and switch to a new branch |
| `git checkout main` | Switch back to main |
| `git merge <branch>` | Merge a branch into current branch |
| `git branch -d <name>` | Delete a branch |
| `git clone <url>` | Download a repo from GitHub |

---

## Exercises

1. **The basic cycle.** Make sure you have at least `bmi.py` and `test_bmi.py` in your project. Stage and commit them with a meaningful message. Run `git log --oneline` to see your commit.

2. **Make a change and track it.** Edit `bmi.py` — add input validation if you haven't already. Run `git status` to see Git noticed the change. Run `git diff` to see exactly what changed. Stage and commit with a descriptive message.

3. **Try branches.** Create a branch called `experiment`. Make some changes — add a new function, change some output, anything. Commit on the branch. Switch back to `main` — notice the changes disappeared. Merge the branch into `main`. Delete the branch.

4. **Check your history.** Run `git log --oneline`. You should see multiple commits with clear messages describing what each one did.

---

## What's Next

You now have a complete development environment: code in files (Replit), imports between files, tests that verify correctness (pytest), and version control that tracks every change (Git). Week 6 adds the final skill before you start working with AI tools: reading and debugging code — including code you didn't write.

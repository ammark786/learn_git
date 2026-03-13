# Git Rebase Practice Guide

This repo is set up so you can **master git rebase** and practice **resolving conflicts** by simulating "another person" (or yourself with a different identity).

---

## Part 1: Initial setup – push to GitHub

Do this once after creating the repo on GitHub (e.g. `learn_git` under your account).

```powershell
# 1. Initialize Git (if not already done)
git init

# 2. Configure user (if not set globally)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# 3. Stage and commit everything
git add .
git commit -m "Initial commit: Python sample code for rebase practice"

# 4. Rename branch to main (if Git created 'master')
git branch -M main

# 5. Add GitHub as remote (replace with YOUR repo URL)
git remote add origin https://github.com/YOUR_USERNAME/learn_git.git

# 6. Push to GitHub
git push -u origin main
```

From now on: `git push` and `git pull` will use `origin main` by default.

---

## Part 2: Simulating "another person" for conflicts

You have two good options. Both let you create **real merge/rebase conflicts** to practice on.

### Option A: Second clone (recommended)

1. **Clone the repo into a different folder** (e.g. `learn_git_other`):
   ```powershell
   cd c:\Projects\Python
   git clone https://github.com/YOUR_USERNAME/learn_git.git learn_git_other
   cd learn_git_other
   ```

2. **Use a different Git identity** in that clone only:
   ```powershell
   git config user.name "Other Developer"
   git config user.email "other@example.com"
   ```
   Commits made in `learn_git_other` will show this author.

3. **Use the two folders as two "developers":**
   - **Folder 1** (`learn_git`): you, main workflow, rebase practice.
   - **Folder 2** (`learn_git_other`): "other person" – make changes, push; then in folder 1 you pull/rebase and resolve conflicts.

### Option B: Two branches on the same clone

1. In your only clone, create a branch and pretend it’s "another person":
   ```powershell
   git checkout -b feature-other
   # Change user for this session only (optional, for different author on commits)
   git config user.name "Other Developer"
   git config user.email "other@example.com"
   ```
2. Edit the **same lines** in e.g. `calculator.py` or `utils.py` on `feature-other`.
3. Commit and switch back to `main`:
   ```powershell
   git add .
   git commit -m "Other dev: change add() behavior"
   git checkout main
   ```
4. On `main`, make **different edits** to the same file/lines, commit.
5. Rebase (or merge) to get a conflict:
   ```powershell
   git rebase feature-other
   # or: git merge feature-other
   ```
   Resolve conflicts, then continue.

**Summary:** Option A is closer to real teamwork (two clones, two pushes). Option B is all in one clone and good for quick conflict drills.

---

## Part 3: Rebase workflows to practice

### 3.1 Rebase your branch onto latest main

Simulates: "I branched off main; main has new commits; I want my work on top of the latest main."

```powershell
git checkout main
git pull origin main
git checkout -b my-feature
# ... make commits on my-feature ...
git checkout main
git pull origin main
git checkout my-feature
git rebase main
```

Your `my-feature` commits are replayed on top of the updated `main`. If conflicts appear, fix them, then:

```powershell
git add .
git rebase --continue
# To cancel the rebase: git rebase --abort
```

### 3.2 Interactive rebase (squash, reorder, edit)

Rewrite history of your current branch (e.g. last 4 commits):

```powershell
git rebase -i HEAD~4
```

In the editor you can:
- **pick** – keep commit as is  
- **reword** – keep changes, change commit message  
- **edit** – stop after this commit to amend or split  
- **squash** – fold into previous commit (keep message)  
- **fixup** – fold into previous commit (discard message)  
- **drop** – remove commit  

Save and close. If you used `edit`, after making changes:

```powershell
git add .
git commit --amend
git rebase --continue
```

### 3.3 Creating a conflict on purpose (same file, same lines)

**In clone 1 (or on `main`):**  
Edit e.g. `utils.py`: change `"Hello, {name}!"` to `"Hi, {name}!"`. Commit and push.

**In clone 2 (or on `feature-other`):**  
Edit `utils.py`: change the same line to `"Hey, {name}!"`. Commit and push.

**Back in clone 1:**  
Pull or fetch and rebase:

```powershell
git fetch origin
git rebase origin/main
```

You’ll get a conflict in `utils.py`. Open the file, fix the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), then:

```powershell
git add utils.py
git rebase --continue
```

---

## Part 4: Quick reference

| Goal                         | Command (typical)        |
|-----------------------------|---------------------------|
| Rebase current branch on main | `git rebase main`       |
| Continue after resolving     | `git rebase --continue`  |
| Abort rebase                 | `git rebase --abort`     |
| Interactive rebase (last N)   | `git rebase -i HEAD~N`   |
| Update main then rebase      | `git checkout main && git pull && git checkout - && git rebase main` |

---

## Files in this repo (for practice)

- **calculator.py** – `add`, `subtract`, `multiply`, `divide` (easy to change same lines in two branches).
- **utils.py** – `greet`, `format_number` (good for small, conflict-prone edits).
- **main.py** – imports from both; changing imports or calls is another way to create conflicts.

Edit these in different branches or clones to create realistic rebase and conflict scenarios.

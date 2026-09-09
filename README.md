# Intro to Git/Github

Welcome! This repository is a **safe, fake “real-world” codebase** used to teach the fundamentals of **Git and GitHub** in a short, hands-on lab. You’ll practice a realistic workflow: making changes, committing them, opening pull requests, merging, and resolving a merge conflict.

---

## What You’ll Learn

By the end of this lab, you should be able to:

- Explain the concepts of a **repo**, **commit**, **branch**, **remote**, and **pull request**
- Use common Git commands to:
  - inspect changes and history (`status`, `diff`)
  - stage and commit (`add`, `commit`)
  - work with branches (`switch`, `branch`)
  - sync with GitHub (`fetch`, `pull`, `push`)
- Create and merge a **Pull Request (PR)** in GitHub
- Resolve a **merge conflict** and understand what Git is asking you to do
- Get introduced to **rebase** as a way to update your branch with the latest `main`

---

## Lab Outline (What You’ll Do)

### Part 1 — GitHub UI Warm-Up (quick & visual)
1. Make a small edit in the GitHub web UI
2. Commit the change to a **new branch**
3. Open a **Pull Request**
4. Merge the PR

### Part 2 — Terminal Workflow
1. Clone your copy of the repo
2. Create a new branch
3. Edit a file locally
4. Stage and commit the change
5. Push your branch to GitHub
6. Open a PR
7. Merge it

### Part 3 — Merge Conflict + Rebase
1. Create two branches that modify the same line in a file
2. Merge one branch first
3. Update the other branch and trigger a merge conflict
4. Resolve the conflict locally and continue the operation
5. Push the fix and merge the PR

---

## Repository Tour

This repo mimics a small “ops documentation + helper scripts” project, because those are common in cyber teams.

- `runbooks/` — example playbooks (Markdown)
- `templates/` — report/evidence templates (Markdown)
- `scripts/` — small helper scripts (bash/python)
- `data/` — sample IOC data + allowlist (CSV/TXT)
- `conflict/` — a dedicated file used to **guarantee** a merge conflict during the lab

---

## Success Criteria

You’re done when you can confidently say:
- “I can make a branch, commit changes, push to a remote, open a PR, merge it, and resolve a conflict.”

---

## Notes

- This repository's content is completely fake. Most content in the repository was generated using AI and is not meant to be used. The respository serves to be cloned and used to teach git commands.
- This repository is used for VECTR modules associated with [nebraskamatrix.com/vectr](nebraskamatrix.com/vectr)

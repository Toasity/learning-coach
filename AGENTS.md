# Repository Maintenance Contract

This file defines the required workflow for any agent that changes this repository.
Treat it as a safety and quality contract. Do not weaken or bypass these rules merely to
finish a task.

## Before making changes

1. Inspect `git status --short`, the current branch, configured remotes, and the branch
   upstream before editing.
2. Record which files were already modified or untracked. Those changes belong to the
   user or another task unless the current request explicitly includes them.
3. Read the relevant implementation, references, templates, and tests before deciding
   how to change behavior.
4. Keep the requested change narrowly scoped. Do not reformat, rename, stage, revert, or
   otherwise alter unrelated files.

## Architecture and implementation rules

- Give every function one clear responsibility.
- Keep CLI `main()` functions limited to argument parsing and workflow orchestration.
  Move validation, calculation, and file operations into named helpers.
- New functions and existing functions touched by the current task must span no more
  than 30 physical lines, counted from the `def` line through the final line of the
  function. Signatures, docstrings, comments, blank lines, and decorators are included.
  Existing functions over this limit do not block unrelated changes, but must be split
  when modified.
- Reuse `scripts/_common.py` for shared configuration parsing, path handling, course
  state, and reusable file operations. Do not duplicate shared logic across commands.
- Avoid hidden mutable global state, mixed abstraction levels, and direct cross-layer
  file mutation.
- Preserve the existing preview/apply workflow for file-changing commands. Preview must
  be the default.
- Never silently overwrite an existing file. Make repeated operations safe and
  idempotent wherever practical.
- Preserve documented workspace-schema and course-lifecycle compatibility unless the
  task explicitly requires a versioned schema change.

## Validation after every change

Run validation before committing and again after resolving a rebase or merge conflict.
All applicable checks must pass.

1. Search tracked and task-owned files for unresolved conflict markers:

   ```sh
   rg --hidden -g '!.git/**' -n '^(<<<<<<<|=======|>>>>>>>)'
   ```

   This scan includes task-owned untracked files. Any real conflict marker blocks
   commit and push.

2. Compile every Python file under `scripts/`:

   ```sh
   PYTHONPYCACHEPREFIX="${TMPDIR:-/tmp}/learning-coach-pycache" \
     python3 -m compileall -q scripts
   ```

3. Run `--help` smoke tests for each changed CLI command and any directly affected
   command.

4. Run relevant behavior checks in a temporary workspace. Use preview mode first and
   run `scripts/validate_workspace --workspace <temporary-workspace>` after applied
   smoke-test operations. Never use a learner's real workspace for automated tests.

5. Use Python's AST line information to check the 30-line limit for every new or
   modified function. Compare against the pre-task version so untouched legacy
   functions do not fail the task.

6. Review the final diff for accidental changes, exposed secrets, destructive behavior,
   and inconsistencies between `SKILL.md`, references, scripts, and templates.

If a check cannot run, report why. Do not describe validation as successful when a
required check was skipped or failed.

## Commit scope

- Stage and commit only files changed for the current task. Use explicit paths; never
  use `git add .`, `git add -A`, or an equivalent broad staging command.
- Do not include pre-existing staged, modified, or untracked files unless the user
  explicitly places them in scope.
- Before committing, compare the staged diff and staged file list with the task-owned
  file list.
- Write a concise commit message that describes the completed behavior.
- Do not amend, rewrite, squash, or discard user commits unless explicitly requested.

## Synchronize and push

After local validation succeeds:

1. Confirm that the current branch has a GitHub remote and an upstream branch. If the
   repository has no commit, remote, upstream, or valid authentication, stop and report
   the missing prerequisite. Keep all local work intact.
2. Commit only the current task's files.
3. Fetch the upstream remote.
4. Rebase the current branch onto its upstream branch. Do not switch to or push another
   branch.
5. Resolve only conflicts whose intended result is mechanically clear, such as
   independent additions or an unambiguous combination of both sides. Preserve both
   parties' intent.
6. If a conflict changes semantics, deletes meaningful work, involves secrets, or has
   more than one plausible resolution, stop the rebase safely and report the conflicted
   files. Do not choose `ours` or `theirs` as a blanket policy.
7. After a successful rebase, rerun the full applicable validation and inspect the
   resulting diff and recent commits.
8. Push the current branch with a normal push. Never use `--force`,
   `--force-with-lease`, deletion refspecs, or any history-rewriting push.
9. Report the commit identifier and push result truthfully.

A failed fetch, rebase, validation, authentication check, or push is a hard stop. Do not
claim that GitHub is synchronized until the normal push succeeds.

## Conflict safety

- Never resolve conflicts by deleting unknown work or by assuming the local or remote
  side always wins.
- Never use destructive recovery commands such as `git reset --hard`,
  `git checkout -- <path>`, or `git clean` without explicit user authorization.
- Preserve a clean recovery path. If an ambiguous rebase conflict occurs, leave the
  user's work intact, identify the conflicting files and commits, and request guidance.
- After every conflict resolution, rerun all applicable checks; a syntactically resolved
  conflict is not necessarily a logically correct resolution.

## Reporting

The final task report must state:

- files changed;
- checks run and their results;
- commit identifier, if committed;
- push destination and result, if pushed; and
- any blocker such as a missing remote, upstream, authentication, or ambiguous conflict.

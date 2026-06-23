---
name: learning-coach
description: Manage a file-based multi-course learning workspace with coaching, assessment, spaced review, material organization, parallel scheduling, and course lifecycle automation. Use when Codex needs to initialize or operate a learning workspace, create or plan courses, start a study session, organize downloaded course files, protect solutions, validate records, complete a course, or archive it.
---

# Learning Coach

Use the skill as the operating procedure; keep all personal learning state in the workspace.

## Locate the workspace

Run `scripts/validate_workspace` from the current directory. It searches upward for
`learning-workspace.yaml`. If none exists, offer to run `scripts/init_workspace`.

Read `references/workspace-schema.md` before changing workspace structure.

## Choose the workflow

- Start or continue learning: read `references/coaching-protocol.md`.
- Create a course: run `scripts/create_course COURSE_ID --name "Name" --apply`.
- Build the weekly plan: read `references/scheduling-rules.md`, then run
  `scripts/plan_week --minutes N --apply`.
- Organize downloads: read `references/material-rules.md`, inspect uncertain files, then
  run `scripts/organize_inbox`; use `--apply` only after reviewing its plan.
- Complete a course: run `scripts/complete_course COURSE_ID`, review the checklist, then
  rerun with `--apply`. After completion evidence is reviewed, run it again with
  `--start-maintenance --apply`.
- Archive a maintained course: run `scripts/archive_course COURSE_ID`, then rerun with
  `--apply` after confirmation.
- Reactivate an archived course: run `scripts/reactivate_course COURSE_ID`, then rerun with
  `--apply`; always begin with a diagnostic.
- Check integrity: run `scripts/validate_workspace`.

## Preserve learning integrity

- Treat the learning mode as the task structure and the guidance strategy as the way the
  learner participates. Use bounded Socratic guidance where it supports the selected
  mode; do not use it in examiner mode.
- Adapt the session to the learner's starting point. For unseen material, teach before
  testing; for learned material, use retrieval, correction, and transfer.
- Require the learner's first attempt before giving a full solution only after the
  required knowledge has been taught or confirmed. Do not make a beginner guess target
  content they have not learned.
- Ask first when the learner can reason from available information. Directly provide new
  definitions, empirical facts, and specialist background; never disguise them as
  answers a beginner should be able to guess.
- If the learner has enough information but remains stuck, use at most two progressively
  stronger prompts, then give the minimum explanation needed and return the next
  reasoning step to the learner.
- Reveal hints in five levels: restate, concept, local hint, framework, full answer.
- Do not count work completed with high-level hints as independent mastery.
- Do not read `solutions/` in coaching or examiner mode before the learner submits.
- Use new contexts for transfer tests and schedule review at 1, 7, and 21 days.
- Keep courses parallel by default. Set temporary focus only on explicit user request and
  include an end date.

## Apply safety rules

- Preview file operations before applying them.
- Never overwrite an existing file.
- Never delete external-library originals.
- Leave ambiguous materials in `inbox/unresolved/`.
- Ask before resolving duplicates, deleting files, or replacing records.
- Update only the selected course plus necessary global indexes.

## Keep state out of the skill

Do not store course names, progress, schedules, materials, answers, or learner data in this
skill directory. Store them under the detected workspace.

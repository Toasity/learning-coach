# Workspace Schema

The marker file `learning-workspace.yaml` is the source of workspace settings.

```yaml
version: 1
workspace_id: personal-learning
learning_root: learning
inbox_root: inbox
active_course_limit: 4
minimum_minutes_per_course: 90
weekly_buffer_percent: 15
weekly_minutes: 600
external_library:
```

Required directories:

```text
inbox/{new,unresolved,duplicates}
learning/{courses,archive,shared}
```

Required global files:

```text
learning/dashboard.md
learning/portfolio.md
learning/weekly-plan.md
learning/task-inbox.md
learning/review-queue.md
learning/shared/knowledge-map.md
learning/shared/error-log.md
```

Each course uses a stable lowercase ID and contains:

```text
README.md
goal.md
knowledge-map.md
syllabus.md
journal.md
error-log.md
external-index.md
materials/index.md
exercises/
solutions/
assessments/
projects/
```

The course README begins with simple YAML frontmatter:

```yaml
---
course_id: machine-learning
name: Machine Learning
status: active
created: 2026-06-10
temporary_focus_until:
---
```

Allowed states are `planned`, `active`, `completed`, `maintenance`, and `archived`.
Never change a course ID after creation. Course names may change.

Lifecycle operations must also update the matching row in `learning/portfolio.md`.

# Material Rules

Use `inbox/new/` as a temporary intake area, not permanent storage. Course-named temporary
subdirectories are encouraged.

Classify into:

- `materials/`: slides, readings, notes, small datasets, and starter code.
- `exercises/`: assignments, problem sets, and practice files.
- `solutions/`: answer keys, solutions, and instructor answers.
- `inbox/unresolved/`: unknown course or ambiguous type.

Use `{sequence}-{topic}-{type}-{version}.{ext}` where information is available. Normalize to
lowercase ASCII hyphenated names. Never overwrite; append a version when necessary.

Filename and parent-folder evidence may support automatic classification. Inspect file content
when evidence is weak. Do not guess a course from topic similarity alone.

Solutions are protected:

- Coaching and examiner workflows must not read them before learner submission.
- Keep them physically separate from exercises.
- Do not include solution text in indexes.

Treat videos, multi-gigabyte datasets, archives, and original backups as external-library
material. Record absolute path, source, and purpose in `external-index.md`; never delete them.

Detect duplicates by content hash. Report duplicates first and ask before moving or deleting
them.

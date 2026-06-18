# Parallel Scheduling Rules

Treat all active courses as peers.

1. Reserve the configured weekly buffer.
2. Allocate the configured minimum to every active course.
3. Reserve time for overdue and upcoming reviews.
4. Distribute remaining capacity by deadline urgency, overdue reviews, bottleneck severity,
   and time since last study.
5. Keep at most one weekly outcome per course.
6. Never exceed usable weekly capacity.

If minimum allocations exceed capacity, report the conflict instead of silently reducing
courses. Ask the user to increase time, lower the minimum, or move a course to maintenance.

Temporary focus is allowed only when explicitly requested. Record a reason and
`temporary_focus_until`; remove the focus automatically after that date.

Maintenance courses receive review work but no active-course minimum.

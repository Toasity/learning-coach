# Coaching Protocol

## Start

1. Read the global dashboard, portfolio, weekly plan, and due review queue.
2. If the user specifies a course, select it. Otherwise choose overdue reviews, today's
   deadlines, courses below their weekly minimum, highest-priority work, then the least
   recently studied course.
3. Read only that course and referenced shared nodes.
4. Use the learner's stated experience, the knowledge map, and prior evidence to choose
   one mode:
   - **First learning:** the target is unseen or the learner says they have not learned it.
   - **Guided practice:** the target was introduced but still needs supported practice.
   - **Retrieval and review:** prior evidence shows the target was learned.
   - **First-principles problem exploration:** a chapter needs a unifying introduction
     or its concepts need to be reconstructed and integrated.
   - **Examiner:** the learner explicitly requests an assessment without coaching.
5. When the starting point is uncertain, ask about prior exposure and run a brief,
   low-pressure prerequisite check. Check only knowledge required to begin; do not test
   the unseen target or record missing prerequisites as errors in the target.
6. State the mode, task, expected duration, evidence, and reason for selection. The
   learner may explicitly switch modes.

## First learning

1. Inspect the relevant course materials and follow their sequence where it supports the
   stated goal.
2. If materials are missing or incomplete, create a minimal temporary path covering the
   prerequisite, concept, example, and practice needed for the task. Record the material
   gap and the temporary path in the journal or syllabus.
3. Repair missing prerequisites before teaching the target.
4. Teach in small cycles:
   - explain one chunk and connect it to prior knowledge;
   - work through an example while making the reasoning visible;
   - complete a similar example with the learner;
   - ask for a small independent check only after instruction.
5. Do not require the learner to guess target content before it has been taught.

## Guided practice

Choose a task that uses already introduced knowledge. Let the learner attempt each step,
then reveal only the next necessary hint. Work completed with substantial guidance is
practice evidence, not independent application evidence.

Hint levels:

1. Restate the goal.
2. Name the relevant concept.
3. Point to a local step or counterexample.
4. Give the solution framework.
5. Show a full answer and compare it with the learner's attempt.

## Retrieval and review

Begin with a 5-10 minute retrieval check, then correct errors, practice a useful variant,
and finish with transfer to a new context. Return to first learning or guided practice if
the check reveals that the target was never learned or its prerequisites are missing.

## First-principles problem exploration

Use a real or theoretical problem that unifies the chapter's core ideas. The coach
selects the problem from the course goal and materials; use a small number of supporting
subproblems when one natural problem cannot cover every core idea.

1. Define the problem's context, inputs, outputs, boundaries, goal, and success criteria.
2. Separate observable facts, provisional assumptions, customary practices, and hard
   constraints. Do not treat a textbook formula, named model, or standard solution as a
   first principle.
3. Ask why each claim is needed until reaching foundations appropriate to the current
   course level: definitions, axioms, established observations, resource limits, or
   explicit behavioral assumptions.
4. Derive the required properties or mechanism before introducing its formal name.
5. For each concept, connect its foundation, the constraint it addresses, the subproblem
   it supports, and whether it is necessary or one replaceable design choice.
6. Reassemble the reasoning as:
   `problem -> facts/assumptions/constraints -> foundations -> derivation -> formal
   concepts -> solution`.
7. Change one assumption, constraint, or boundary condition and ask the learner to
   identify which conclusions survive and which parts of the solution must change.
8. Record supporting subproblems and any core ideas that remain uncovered.

## Bounded Socratic guidance

Learning modes define the task structure; Socratic guidance is an interaction strategy
that may support first learning, guided practice, retrieval, and first-principles
exploration. Do not use it in examiner mode.

- Ask before telling only when the learner can reason from information already available.
- Directly provide new definitions, empirical facts, specialist background, and other
  information that cannot be derived. Do not turn missing knowledge into a guessing game.
- Give each question a purpose: expose an assumption, identify a constraint, derive a
  mechanism, compare alternatives, or test understanding.
- If required information is missing, provide it immediately. If information is
  sufficient but the learner is stuck, use at most two progressively stronger prompts,
  then give the minimum necessary explanation.
- After supplying information or an explanation, return the next reasoning step to the
  learner.
- Record what the learner derived independently and what the coach supplied or implied.

## Examiner

Use assessment tasks without teaching or hints. Do not open `solutions/` in any mode
before the learner submits an attempt.

## Finish

1. Ask the learner to explain the idea, why it works, and where it fails.
2. Give an exit check appropriate to the session: a small independent check after first
   learning, a new-context transfer task after retrieval and review, or a changed
   assumption or constraint after first-principles exploration.
3. Record the mode, materials used, content taught, question purpose, reasoning level,
   assistance or hint level, independent evidence, errors, time, material gaps, and next
   action. For first-principles exploration, also record the reasoning chain and
   counterfactual test.
4. Update the course journal, error log, knowledge map, global review queue, and dashboard.
5. Schedule variant reviews at 1, 7, and 21 days where appropriate.

Mastery levels:

```text
0 unseen
1 familiar
2 explain
3 apply
4 transfer
5 teach
```

First exposure may raise an unseen target from level 0 to level 1. An independent
explanation may support level 2. Guided work cannot establish level 3 independent
application. In first-principles exploration, understanding a concept's role supports
level 1; independently explaining how it follows from foundations and constraints
supports level 2; independently deriving and solving its subproblem supports level 3;
reconstructing the solution after a constraint changes supports level 4; and comparing
alternatives with their assumptions and boundaries supports level 5. Coach-supplied or
implied reasoning is not independent evidence. Only observable evidence raises mastery
beyond familiarity.

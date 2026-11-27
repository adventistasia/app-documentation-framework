# Scoping Agent Prompt

Use this prompt to draft an application's Scope Record (SP-00) for its owners to approve. Run it before any other document is produced, and again at each stage gate or when the application changes.

## Files to load

- `03_scoping_guide.md` (the method: dimensions, floor rules, triggers, depth matrix, never-dropped minimum)
- `templates/spine/SP-00-scope-record.md` (the output layout)
- `02_conventions.md` (front-matter and naming)
- Any existing SP-00 for this application (when re-scoping)

## Prompt

```text
You are drafting the Scope Record (SP-00) for one application, using the framework files provided.

Application: <name>
Material available: <project brief, repository path, existing docs, notes from the owners>
Business owner: <name>    Technical owner: <name>

Do this:
1. Score D1–D7 using the descriptions in 03_scoping_guide.md. For each score give a one-line reason
   that cites the material. If the material does not tell you, score the more cautious option and
   add a Q-xx open question for the owner.
2. Total the scores, pick the level, then apply the floor rules F1–F3 and say which applied.
3. Answer T1–T11 with Yes or No and a one-line reason each.
4. Fill the Items table for all 24 documents from the depth matrix, applying the triggers. Give the
   parent for every S item and a reason for every —. Check the never-dropped minimum is in scope.
5. List any place where you recommend a depth different from the matrix as a Deviation, with the
   reason. Do not apply it; the owners decide.
6. Leave the Approval section empty. Set status: Draft. Never record an approval.

Output the complete SP-00 document as markdown, following the template exactly, then a short list of
the questions the owners must answer before approving it.
```

# Producer Agent Prompt: Forward (application being designed or built)

Use this prompt to draft or update one document for an application that is being designed or built. For an application that already exists, use [producer_reverse.md](producer_reverse.md).

## Files to load

Always:
- `02_conventions.md` (front-matter, layout, IDs, linked columns, writing style)
- The application's approved `SP-00` Scope Record (depth and parent for this item)
- The template for the document: `templates/<spine|business|engineering>/<DOC-ID>-*.md`
- The document's section in `01_document_set_register.md` (purpose, how to produce, questions to answer)
- The document's section in the matching rubric: `rubrics/01_business_rubrics.md`, `rubrics/02_engineering_rubrics.md` or `rubrics/03_spine_rubrics.md`
- The application's `SP-01` Glossary, if in scope

As needed: every document listed in the template's `related` front-matter that already exists in the application's `/docs`.

## Prompt

```text
You are producing one document of an application's documentation package, following the framework
files provided. Your output will be reviewed against the rubric provided, so meet it.

Application: <name>
Document: <DOC-ID> <title>
Depth from the Scope Record: <S in <parent DOC-ID> | D | D+>
Source material: <notes, interviews, requirements, designs, tickets, existing documents>

Rules:
- Follow the template's structure and the column headers exactly. At depth S, write only a
  "## <DOC-ID> <Title>" section for the parent, using the template's core tables cut down to what
  answers the question. At D, omit sections marked (Full). At D+, include them.
- Answer every question listed for this document in the register, or record why it does not apply.
- Use IDs in the formats in 02_conventions.md. Reuse existing IDs from the related documents; define
  new ones only for items this document owns. Never reuse a retired ID.
- Use names exactly as in SP-01 and the home tables.
- Unknown but required details: write TBD with an owner and add a Q-xx row. Never invent values,
  owners, dates, test results, measurements or sign-offs.
- Put every limitation in Known limitations with a LIM-xx ID.
- Link instead of repeating content that belongs to another document.
- Business and spine documents: plain language for a manager or support person.
  Engineering documents: technical language is fine; add new terms to a "Terms to add to SP-01" list.
- Set status: Draft. Add a change-log row for this version with "Approved by" left empty.

Output the document as markdown, then a list of: new IDs defined, IDs referenced that do not exist
yet, open questions, and terms to add to SP-01.
```

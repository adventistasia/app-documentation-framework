# Producer Agent Prompt

Use this prompt to produce one documentation artifact.

```text
You are producing an Application Documentation and Audit Framework artifact.

Application: [Application name]
Artifact to produce: [Document name]
Audience: [Business owner / support owner / users / management / IT]
Available context: [Paste relevant notes, workflows, requirements, project brief, or existing documents]

Produce the artifact using the template and guidance for this document type.

Requirements:
- Use plain business language.
- Name owners, roles, workflows, statuses, dependencies, and reports where known.
- Mark unknown but required details as TBD with a clear note.
- Do not invent sign-off or acceptance.
- Link to related artifacts using IDs where available.
- Include assumptions, limitations, and open questions.
- Keep technical details only where needed for ownership, dependency, support, or access understanding.

Output as markdown.
```

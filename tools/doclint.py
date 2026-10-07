#!/usr/bin/env python3
"""doclint: mechanical checks for application documentation packages.

Reference implementation of review/05_linter_spec.md. Python 3.9+, standard
library only.

    python3 tools/doclint.py package <repo-root> [--docs docs] [--today YYYY-MM-DD] [--format text|json]
    python3 tools/doclint.py framework <framework-root> [--format text|json]

`package` lints one application's documentation (every .md under <repo-root>/<docs>
plus <repo-root>/AGENTS.md). It reads front-matter, S sections (`## <DOC-ID> <Title>`),
pipe tables and content IDs as set out in 02_conventions.md, then runs every rule
tagged Mechanical in review/02_cross_document_rules.md. Tables are found by header
text (case-insensitive, trimmed); extra columns are ignored. Cells reading None, -,
—, or N/A are empty but explicit, which is accepted only where a rule allows None.

`framework` lints the framework repository itself (spec section 6): templates,
rubric coverage, example-name hygiene, the consolidated guide, and every example
package. Example packages are linted "as of" their own latest last_reviewed date,
so their results do not change with the calendar.

Exit code: 0 when there is no High or Medium finding, 1 when there is, 2 on a usage
error. Every linter finding is a Bug (A-BUG-nn); staleness (X-28) is Low.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date

DOC_IDS = (["SP-00", "SP-01", "SP-10", "SP-11", "SP-12"]
           + ["BUS-%02d" % i for i in range(1, 10)]
           + ["ENG-%02d" % i for i in range(1, 11)])
PREFIXES = ("BEN|C|W|R|BR|ST|TR|REC|REP|NTF|COST|RISK|FR|NFR|J|CMP|ENT|D|INT|ENV|CFG|SEC|"
            "FLAG|ALR|RB|OC|MT|SM|AC|T|COND|LIM|Q")
ID_RE = re.compile(r"\b(?:(?:%s)-\d{2,}|ADR-\d{3,})\b" % PREFIXES)
LOOSE_ID_RE = re.compile(r"[A-Za-z]{1,6}-[0-9A-Za-z]{1,4}")
DOCID_RE = re.compile(r"\b(?:SP|BUS|ENG)-\d{2}\b")
HOME = {"BEN": "BUS-01", "C": "BUS-02", "W": "BUS-03", "R": "BUS-04", "BR": "BUS-05",
        "ST": "BUS-05", "TR": "BUS-05", "REC": "BUS-06", "REP": "BUS-06", "NTF": "BUS-06",
        "COST": "BUS-07", "RISK": "BUS-08", "FR": "ENG-01", "NFR": "ENG-01", "J": "ENG-02",
        "CMP": "ENG-03", "ENT": "ENG-04", "D": "ENG-05", "INT": "ENG-05", "ENV": "ENG-06",
        "CFG": "ENG-06", "SEC": "ENG-06", "FLAG": "ENG-06", "ALR": "ENG-08", "RB": "ENG-08",
        "OC": "ENG-08", "MT": "ENG-08", "ADR": "ENG-10", "SM": "SP-10", "AC": "SP-11",
        "COND": "SP-12"}
FM_KEYS = ["id", "title", "application", "version", "status", "owner", "audience", "level",
           "depth", "contains", "related", "last_reviewed"]
STATUSES = ["Draft", "In Review", "Accepted", "Superseded"]
LEVELS = ["Foundation", "Standard", "Full"]
STD_SECTIONS = ["Purpose", "Scope", "Assumptions and open questions", "Known limitations",
                "Change log"]
GUIDE_RE = re.compile(r">\s*\*\*(Guide:|How to use this template)")
EMPTY = {"", "none", "—", "–", "-", "n/a"}
CLASSIFICATIONS = ["public", "internal", "confidential", "personal", "special-category"]
REVIEW_MONTHS = {"Foundation": 12, "Standard": 6, "Full": 3}
SEVERITY = {"X-01": "Medium", "X-02": "High", "X-03": "High", "X-04": "High", "X-05": "High",
            "X-06": "Medium", "X-07": "Medium", "X-08": "Medium", "X-09": "High",
            "X-11": "High", "X-12": "High", "X-13": "Medium", "X-14": "Medium",
            "X-15": "Medium", "X-16": "Medium", "X-17": "High", "X-18": "Medium",
            "X-19": "High", "X-20": "High", "X-21": "High", "X-22": "High", "X-23": "High",
            "X-24": "Medium", "X-25": "High", "X-26": "High", "X-27": "High", "X-28": "Low"}
SEV_ORDER = {"High": 0, "Medium": 1, "Low": 2}


class UsageError(Exception):
    pass


# --------------------------------------------------------------------------- reading

def clean(cell):
    """Strip markdown links, emphasis and code ticks from a table cell."""
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cell)
    s = s.replace("**", "").replace("__", "").replace("`", "")
    s = re.sub(r"(?<!\w)[*_]|[*_](?!\w)", "", s)
    return s.strip()


def ids(cell, prefix=None):
    """All content-ID tokens in a cell, optionally only those with one prefix."""
    found = ID_RE.findall(cell or "")
    return [i for i in found if prefix is None or prefix_of(i) == prefix]


def prefix_of(content_id):
    return content_id.rsplit("-", 1)[0]


def is_empty(value):
    return (value or "").strip().lower() in EMPTY


def filled(item, col, none_ok=False):
    """Non-empty, and not TBD unless the row carries a Q-xx. `None` counts only if none_ok."""
    v = item.get(col)
    empty = not v.strip() if none_ok else is_empty(v)
    return not empty and not ("tbd" in v.lower() and not ids(item.text, "Q"))


def starts(value, *words):
    v = (value or "").strip().lower()
    return any(v.startswith(w) for w in words)


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]


def parse_front_matter(lines):
    """Return (dict or None, error or None, index of first body line, {key: line})."""
    if not lines or lines[0].strip() != "---":
        return None, None, 0, {}
    for end in range(1, len(lines)):
        if lines[end].strip() == "---":
            break
    else:
        return None, "front-matter has no closing `---` line", 0, {}
    fm, where = {}, {}
    for n in range(1, end):
        raw = re.sub(r"(^|\s)#.*$", "", lines[n]).rstrip()
        m = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", raw)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            val = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
        else:
            val = val.strip("'\"")
        fm[key], where[key] = val, n + 1
    return fm, None, end + 1, where


class Table:
    def __init__(self, doc, owner, line, header):
        self.doc, self.owner, self.line = doc, owner, line
        self.header = [clean(h).lower() for h in header]
        self.rows = []  # (line, [clean cells], raw line)

    @property
    def first(self):
        return self.header[0] if self.header else ""

    def row_dict(self, cells):
        d = {}
        for h, c in zip(self.header, cells):
            d.setdefault(h, c)
        return d


class Item:
    """A row of an `ID` table: one defined content ID."""

    def __init__(self, cid, table, line, cells, text):
        self.id = cid
        self.doc, self.owner, self.line = table.doc, table.owner, line
        self.cells, self.text = table.row_dict(cells), text

    def get(self, col):
        return self.cells.get(col, "")


class DocFile:
    """One markdown file: front-matter, headings, sections, tables and ID tokens."""

    def __init__(self, path, rel, always_parse=False):
        self.path, self.rel = path, rel
        with open(path, encoding="utf-8") as fh:
            self.lines = fh.read().splitlines()
        self.fm, self.fm_error, body, self.fm_lines = parse_front_matter(self.lines)
        self.id = (self.fm or {}).get("id", "")
        self.headings = []      # (level, text, line, owner)
        self.sections = {}      # S-section doc ID -> line
        self.tables = []
        self.text_lines = []    # (line, text, owner) outside code fences
        if self.fm is not None or always_parse:
            self._parse(body)

    def _parse(self, start):
        owner, fence, table = self.id, None, None
        pending = None  # (line, header cells) awaiting a separator row
        guide = False   # inside a `> **Guide:**` blockquote, skipped like code
        for i in range(start, len(self.lines)):
            n, line = i + 1, self.lines[i]
            s = line.strip()
            guide = s.startswith(">") and (guide or bool(GUIDE_RE.match(s)))
            if guide:
                table, pending = None, None
                continue
            m = re.match(r"(`{3,}|~{3,})", s)
            if fence:
                if m and s.startswith(fence) and not s.lstrip(fence[0]).strip():
                    fence = None
                continue
            if m:
                fence, table, pending = m.group(1), None, None
                continue
            h = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
            if h:
                level, text = len(h.group(1)), clean(h.group(2))
                if level == 2:
                    d = re.match(r"((?:SP|BUS|ENG)-\d{2})\b", text)
                    owner = d.group(1) if d else self.id
                    if d:
                        self.sections.setdefault(owner, n)
                self.headings.append((level, text, n, owner))
            self.text_lines.append((n, line, owner))
            if s.startswith("|"):
                cells = split_row(s)
                if table is not None:
                    table.rows.append((n, [clean(c) for c in cells], line))
                elif pending and re.fullmatch(r"[\s|:\-]+", s) and "-" in s:
                    table = Table(self, owner, pending[0], pending[1])
                    self.tables.append(table)
                    pending = None
                else:
                    pending = (n, cells)
            else:
                table, pending = None, None


# --------------------------------------------------------------------------- package lint

class Finding:
    def __init__(self, rule, severity, file, line, message):
        self.id, self.rule, self.severity, self.file, self.line, self.message = (
            "", rule, severity, file, line, message)

    def as_dict(self):
        return {k: getattr(self, k) for k in ("id", "rule", "severity", "file", "line", "message")}


def add_months(d, months):
    y, m = divmod(d.month - 1 + months, 12)
    y, m = d.year + y, m + 1
    for day in (d.day, 30, 29, 28):
        try:
            return date(y, m, day)
        except ValueError:
            continue


class PackageLinter:
    def __init__(self, files, today):
        self.files, self.today = files, today
        self.findings, self.checked = [], set()
        self.by_id = {}                       # doc ID -> first DocFile with that id
        self.sections = defaultdict(list)     # doc ID -> [(DocFile, line)]
        self.defs = defaultdict(list)         # content ID -> [Item]
        self.bad_defs = []                    # (DocFile, line, cell)
        self.tokens = []                      # (id, DocFile, line, owner, is_definition)
        for f in files:
            self.by_id.setdefault(f.id, f)
            for d, n in f.sections.items():
                self.sections[d].append((f, n))
            self._collect(f)
        self.triggers, self.scope, self.scope_loc, self.level = self._read_scope()

    # ---- helpers
    def add(self, rule, where, message, severity=None):
        doc, line = (where.doc, where.line) if isinstance(where, (Item, Table)) else where
        self.findings.append(Finding(rule, severity or SEVERITY[rule],
                                     doc.rel if doc else "-", line, message))

    def item(self, cid):
        lst = self.defs.get(cid)
        return lst[0] if lst else None

    def items(self, prefix):
        return [lst[0] for cid, lst in self.defs.items() if prefix_of(cid) == prefix]

    def tables(self, owner=None):
        return [t for f in self.files for t in f.tables if owner is None or t.owner == owner]

    def depth(self, doc_id):
        if self.scope is not None and doc_id in self.scope:
            return self.scope[doc_id]["depth"]
        if doc_id in self.by_id:
            return "D"
        return "S" if doc_id in self.sections else "—"

    def in_scope(self, doc_id):
        return self.depth(doc_id) != "—"

    def trigger(self, t):
        return self.triggers.get(t, True)

    def exists(self, doc_id):
        return doc_id in self.by_id or doc_id in self.sections

    def _collect(self, f):
        def_lines = {}
        for t in f.tables:
            if t.first != "id":
                continue
            for n, cells, raw in t.rows:
                cell = cells[0] if cells else ""
                if ID_RE.fullmatch(cell):
                    self.defs[cell].append(Item(cell, t, n, cells, raw))
                    def_lines[n] = cell
                elif LOOSE_ID_RE.fullmatch(cell) or DOCID_RE.fullmatch(cell):
                    self.bad_defs.append((f, n, cell))
        for n, line, owner in f.text_lines:
            seen_def = False
            for tok in ID_RE.findall(line):
                is_def = not seen_def and def_lines.get(n) == tok
                seen_def = seen_def or is_def
                self.tokens.append((tok, f, n, owner, is_def))

    def _read_scope(self):
        triggers, scope, loc = {}, None, None
        sp00 = self.by_id.get("SP-00")
        holder = sp00 or (self.sections["SP-00"][0][0] if self.sections.get("SP-00") else None)
        level = holder.fm.get("level") if holder else None
        if not level and self.files:
            level = Counter(f.fm.get("level", "") for f in self.files).most_common(1)[0][0]
        for t in self.tables("SP-00"):
            loc = loc or t
            if t.first == "trigger" and "answer" in t.header:
                for n, cells, raw in t.rows:
                    row = t.row_dict(cells)
                    m = re.match(r"T(\d{1,2})\b", row.get("trigger", ""))
                    if not m:
                        continue
                    ans = row.get("answer", "")
                    if not starts(ans, "yes", "no"):
                        self.add("X-27", (t.doc, n), "Trigger T%s answer `%s` must be Yes or No."
                                 % (m.group(1), ans))
                    triggers["T" + m.group(1)] = not starts(ans, "no")
            elif t.first == "item" and "depth" in t.header:  # not the Deviations table
                scope = scope or {}
                for n, cells, raw in t.rows:
                    row = t.row_dict(cells)
                    m = re.match(r"((?:SP|BUS|ENG)-\d{2})\b", row.get("item", ""))
                    if not m:
                        self.add("X-27", (t.doc, n), "Scope item `%s` does not start with a "
                                 "document ID." % row.get("item", ""))
                        continue
                    depth = row.get("depth", "").strip()
                    depth = "—" if depth in ("-", "–", "—") else depth.upper()
                    if depth not in ("—", "S", "D", "D+"):
                        self.add("X-27", (t.doc, n), "Scope item %s has depth `%s`; use —, S, "
                                 "D or D+." % (m.group(1), row.get("depth", "")))
                        depth = "D"
                    parent = DOCID_RE.findall(row.get("parent", ""))
                    scope[m.group(1)] = {"depth": depth, "reason": row.get("reason", ""),
                                         "parent": parent[0] if parent else None,
                                         "where": (t.doc, n)}
        return triggers, scope, loc, level

    # ---- checks
    def run(self):
        for check in (self.check_front_matter, self.check_sections, self.check_ids,
                      self.check_scope, self.check_caps_processes, self.check_roles_statuses,
                      self.check_rules_reports_notifications, self.check_dependencies,
                      self.check_risks, self.check_limitations, self.check_glossary,
                      self.check_journeys, self.check_records, self.check_requirements,
                      self.check_measures, self.check_handover, self.check_staleness):
            check()
        return self.findings

    def check_front_matter(self):
        self.checked.update(["X-25", "X-14"])
        seen = defaultdict(list)
        for f in self.files:
            fm, at = f.fm, (lambda k: (f, f.fm_lines.get(k, 1)))
            for k in FM_KEYS:
                if k not in fm:
                    self.add("X-25", (f, 1), "Front-matter lacks `%s`; add it (use [] for an "
                             "empty list)." % k)
            if "id" in fm:
                seen[fm["id"]].append(f)
                if fm["id"] not in DOC_IDS:
                    self.add("X-25", at("id"), "Front-matter id `%s` is not a document ID from "
                             "the register." % fm["id"])
            for key, allowed in (("status", STATUSES), ("level", LEVELS), ("depth", ["D", "D+"])):
                if key in fm and fm[key] not in allowed:
                    self.add("X-25", at(key), "Front-matter %s `%s` is invalid; use one of %s."
                             % (key, fm[key], " / ".join(allowed)))
            if "last_reviewed" in fm and not self._date(fm["last_reviewed"]):
                self.add("X-25", at("last_reviewed"), "last_reviewed `%s` is not an ISO date "
                         "(YYYY-MM-DD)." % fm["last_reviewed"])
            for key in ("related", "contains"):
                val = fm.get(key, [])
                if not isinstance(val, list):
                    self.add("X-25", at(key), "`%s` must be a list of document IDs, e.g. "
                             "[BUS-02, ENG-01]." % key)
                for d in val if isinstance(val, list) else []:
                    problem = ("is not a document ID" if d not in DOC_IDS else None if
                               self.exists(d) else "is neither a file nor a section here")
                    if problem:
                        self.add("X-25", at(key), "`%s` lists `%s`, which %s; fix or remove "
                                 "the entry." % (key, d, problem))
            contains = fm.get("contains") if isinstance(fm.get("contains"), list) else []
            for d in contains:
                if d in DOC_IDS and d not in f.sections and self.exists(d):
                    self.add("X-25", at("contains"), "`contains` lists %s, but this file has no "
                             "`## %s <Title>` section." % (d, d))
            for d, n in f.sections.items():
                if d not in contains:
                    self.add("X-25", (f, n), "Section `## %s` is not listed in this file's "
                             "`contains`; add %s to it." % (d, d))
        for d, fs in seen.items():
            for f in fs[1:]:
                self.add("X-25", (f, 1), "Document id %s is also used by %s; each document has "
                         "one file." % (d, fs[0].rel))
        for key in ("application", "level"):
            values = Counter(f.fm[key] for f in self.files if key in f.fm)
            if len(values) > 1:
                common = values.most_common(1)[0][0]
                for f in self.files:
                    if key in f.fm and f.fm[key] != common:
                        self.add("X-14", (f, f.fm_lines.get(key, 1)), "`%s` is `%s` here but `%s` "
                                 "in most files; it must be identical in every document."
                                 % (key, f.fm[key], common))

    def check_sections(self):
        for f in self.files:
            have = {t.lower() for lvl, t, n, o in f.headings if lvl == 2}
            for sec in STD_SECTIONS:
                if sec.lower() not in have:
                    self.add("X-25", (f, 1), "Standard section `## %s` is missing; add it (one "
                             "line is enough when there is nothing to say)." % sec)

    def check_ids(self):
        for f, n, cell in self.bad_defs:
            self.add("X-25", (f, n), "`%s` in an ID column is not a valid content ID; use a "
                     "prefix from conventions §5 and a zero-padded number (e.g. C-01, ADR-001)."
                     % cell)
        for cid, lst in self.defs.items():
            for dup in lst[1:]:
                self.add("X-25", dup, "%s is defined twice (also at %s:%d); give one a new ID."
                         % (cid, lst[0].doc.rel, lst[0].line))
        tr_rows = {(i.doc.rel, i.line) for i in self.items("TR")} if self._t3() else set()
        reported = set()
        for tok, f, n, owner, is_def in self.tokens:
            p = prefix_of(tok)
            if is_def or p == "T" or tok in self.defs or (tok, f.rel) in reported:
                continue
            if p == "ST" and (f.rel, n) in tr_rows:
                continue  # reported by X-05
            reported.add((tok, f.rel))
            rule = {"R": "X-03", "ST": "X-04", "TR": "X-05"}.get(p, "X-25")
            self.add(rule, (f, n), "%s is referenced but not defined in any ID table; define it "
                     "in %s or correct the reference." % (tok, HOME.get(p, "its document")))

    def check_scope(self):
        self.checked.add("X-27")
        first = (self.files[0], 1) if self.files else (None, 0)
        if self.scope is None:
            self.add("X-27", self.scope_loc or first, "No Scope Record Items table (first column "
                     "`Item`) found in SP-00; add SP-00 as a file or a `## SP-00 Scope Record` "
                     "section.")
        else:
            where = self.scope_loc
            missing_t = ["T%d" % i for i in range(1, 12) if "T%d" % i not in self.triggers]
            if missing_t:
                self.add("X-27", where, "Scope Record Triggers table lacks %s; answer every "
                         "trigger Yes or No with a reason." % ", ".join(missing_t))
            missing = [d for d in DOC_IDS if d not in self.scope]
            if missing:
                self.add("X-27", where, "Scope Record Items table lacks %s; list all 24 "
                         "document IDs with a depth." % ", ".join(missing))
            for d, s in self.scope.items():
                if s["depth"] == "S" and d not in self.sections:
                    self.add("X-27", s["where"], "Scope sets %s to S but no `## %s <Title>` "
                             "section exists; add it to %s." % (d, d, s["parent"] or "its parent"))
                elif s["depth"] in ("D", "D+") and d not in self.by_id:
                    self.add("X-27", s["where"], "Scope sets %s to %s but no file has `id: %s`; "
                             "add the document." % (d, s["depth"], d))
                elif s["depth"] == "—":
                    if is_empty(s["reason"]):
                        self.add("X-27", s["where"], "Scope sets %s to — without a reason; add a "
                                 "one-line reason." % d)
                    if self.exists(d):
                        self.add("X-27", s["where"], "Scope sets %s to — but it exists as a file "
                                 "or section; remove it or change its depth." % d)
        if not any(h[3] == "BUS-01" and "what success looks like" in h[1].lower()
                   for f in self.files for h in f.headings):
            self.add("X-27", (self.by_id.get("BUS-01"), 1) if "BUS-01" in self.by_id else first,
                     "Never-dropped minimum: BUS-01 has no \"What success looks like\" heading.")
        for prefix, what in (("SM", "success measure (SM)"), ("AC", "acceptance criterion (AC)")):
            if not self.items(prefix):
                self.add("X-27", first, "Never-dropped minimum: no %s is defined." % what)
        for d in ("ENG-07", "ENG-08"):
            if not self.in_scope(d):
                self.add("X-27", self.scope_loc or first, "Never-dropped minimum: %s is set to — "
                         "or missing; it must be at least an S section." % d)

    def check_caps_processes(self):
        if not (self.in_scope("BUS-02") or self.in_scope("BUS-03")):
            return
        self.checked.update(["X-01", "X-02"])
        for c in self.items("C"):
            if not ids(c.get("processes"), "W") and not self._admin_only(c):
                self.add("X-01", c, "%s lists no process in Processes; add W IDs or write "
                         "`Admin/support only`." % c.id)
        for w in self.items("W"):
            self.need("X-02", w, "capabilities", "C", "capability")
        self.two_way("X-02", "C", "processes", "W", "capabilities")
        self.two_way("X-02", "W", "capabilities", "C", "processes")

    def check_roles_statuses(self):
        self.checked.update(["X-03", "X-04"])
        for t in self.tables():
            for n, cells, raw in t.rows if "roles" in t.header else []:
                cell = t.row_dict(cells).get("roles", "")
                rest = ID_RE.sub(lambda m: "" if prefix_of(m.group()) == "R" else m.group(), cell)
                rest = re.sub(r"(?i)\bautomated\b|\band\b|[,;/&+]", " ", rest).strip()
                if rest and not is_empty(rest):
                    self.add("X-03", (t.doc, n), "Roles cell for %s contains `%s`; use R IDs or "
                             "`Automated` only." % (cells[0] if cells else "row", rest))
        if not self._t3():
            return
        self.checked.add("X-05")
        for tr in self.items("TR"):
            for col in ("from", "to"):
                self.need("X-05", tr, col, "ST", "status")
                for st in ids(tr.get(col), "ST"):
                    if st not in self.defs:
                        self.add("X-05", tr, "%s `%s` is %s, which is not a defined status in "
                                 "BUS-05." % (tr.id, col.capitalize(), st))

    def check_rules_reports_notifications(self):
        for rule, prefix, cols, home in (
                ("X-06", "BR", ["owner"], "BUS-05"),
                ("X-07", "REP", ["audience", "purpose", "owner", "source"], "BUS-06"),
                ("X-08", "NTF", ["trigger", "recipient", "purpose", "expected action"], "BUS-06")):
            if self.in_scope(home):
                self.checked.add(rule)
                for it in self.items(prefix):
                    self.require(rule, it, cols)

    def check_dependencies(self):
        if not self.in_scope("ENG-05"):
            return
        self.checked.update(["X-09", "X-15", "X-21"])
        for d in self.items("D"):
            self.require("X-09", d, ["owner", "criticality", "impact", "support path"])
            if "capabilities affected" in d.cells and self.in_scope("BUS-02"):
                listed = set(ids(d.get("capabilities affected"), "C"))
                using = {c.id for c in self.items("C") if d.id in ids(c.get("dependencies"), "D")}
                if listed != using:
                    self.add("X-09", d, "%s Capabilities affected (%s) disagrees with the "
                             "capabilities whose Dependencies list it (%s); make them match."
                             % (d.id, ", ".join(sorted(listed)) or "none",
                                ", ".join(sorted(using)) or "none"), "Medium")
            crit = d.get("criticality")
            if filled(d, "criticality") and not starts(crit, "high", "medium", "low"):
                self.add("X-09", d, "%s Criticality `%s` must be High, Medium or Low."
                         % (d.id, crit))
            if starts(crit, "high"):
                if not filled(d, "workaround", none_ok=True):
                    self.add("X-09", d, "High dependency %s has no Workaround; describe one or "
                             "write `None`." % d.id)
                if self.in_scope("BUS-02"):
                    self.covered("X-09", d, "C", "dependencies", "in the Dependencies column "
                                 "of any capability")
                self.need("X-21", d, "runbook", "RB", "runbook entry")
        for a in self.items("ALR"):
            self.need("X-21", a, "runbook", "RB", "runbook entry")
        for t in self.tables("ENG-08"):  # triage tables; "Dependencies to check" is accepted
            col = next((h for h in t.header if h.startswith("dependencies")), None)
            for n, cells, raw in t.rows if col else []:
                cell = t.row_dict(cells).get(col, "")
                if not is_empty(cell) and not ids(cell, "D"):
                    self.add("X-15", (t.doc, n), "Triage row `%s` names dependencies as `%s`; "
                             "use D IDs or `None`." % (cells[0] if cells else "", cell))
        if self.trigger("T5"):
            self.checked.add("X-20")
            for i in self.items("INT"):
                self.need("X-20", i, "dependency", "D", "dependency")
            for d in self.items("D"):
                if starts(d.get("type"), "integration"):
                    self.covered("X-20", d, "INT", "dependency", "by any interface (INT)")
        if self.in_scope("BUS-07"):
            self.checked.add("X-24")
            for d in self.items("D"):
                if starts(d.get("cost"), "yes"):
                    self.covered("X-24", d, "COST", "dependency", "in the Dependency column "
                                 "of any BUS-07 cost line, but its Cost is Yes")

    def check_risks(self):
        if self.in_scope("BUS-08"):
            self.checked.add("X-11")
            for r in self.items("RISK"):
                if any(starts(r.get(c), "high") for c in ("severity", "rating", "risk level")):
                    self.require("X-11", r, ["control", "owner"], "High risk ")

    def check_limitations(self):
        self.checked.add("X-12")
        listed = {i for t in self.tables("SP-12") if "limitation" in t.header
                  for _, c, _ in t.rows for i in ids(t.row_dict(c)["limitation"], "LIM")}
        for tok, f, n, owner, d in self.tokens:
            if prefix_of(tok) == "LIM" and owner != "SP-12" and tok not in listed:
                listed.add(tok)  # report once
                self.add("X-12", (f, n), "%s is not in a Limitation cell of SP-12's "
                         "\"Consolidated known limitations\" table; add it there." % tok)

    def check_glossary(self):
        if not self.in_scope("SP-01"):
            return
        self.checked.add("X-13")
        terms = {t.row_dict(c).get("term", "").lower()
                 for t in self.tables("SP-01") if "term" in t.header for _, c, _ in t.rows}
        for it in self.items("R") + self.items("ST") + self.items("REC"):
            name = it.get("name")
            if not is_empty(name) and name.lower() not in terms:
                self.add("X-13", it, "%s name `%s` is not a Term in SP-01 Glossary; add it."
                         % (it.id, name))

    def check_journeys(self):
        if self.trigger("T1") and self.in_scope("ENG-02"):
            self.checked.add("X-16")
            for j in self.items("J"):
                self.need("X-16", j, "processes", "W", "process")
            self.two_way("X-16", "W", "journeys", "J", "processes")
            self.two_way("X-16", "J", "processes", "W", "journeys")

    def check_records(self):
        if not self.in_scope("BUS-06"):
            return
        self.checked.add("X-17")
        for r in self.items("REC"):
            self.require("X-17", r, ["classification", "retention"])
            cls = r.get("classification")
            if filled(r, "classification") and not starts(cls, *CLASSIFICATIONS):
                self.add("X-17", r, "%s Classification `%s` must be Public, Internal, "
                         "Confidential, Personal or Special-category." % (r.id, cls))
            if starts(cls, "personal", "special") and not filled(r, "purpose"):
                self.add("X-17", r, "%s holds %s data but has no Purpose; state why it is "
                         "kept." % (r.id, cls))
            if self.in_scope("ENG-04"):
                self.covered("X-17", r, "ENT", "records", "in the Records column of any "
                             "entity (ENT)")
        for e in self.items("ENT"):
            self.need("X-17", e, "records", "REC", "record")

    def check_requirements(self):
        self.checked.update(["X-18", "X-19"])
        for fr in self.items("FR"):
            self.need("X-18", fr, "capabilities", "C", "capability")
        if self.depth("ENG-01") in ("D", "D+"):
            for c in self.items("C"):
                if not self._admin_only(c):
                    self.covered("X-18", c, "FR", "capabilities", "by any functional "
                                 "requirement (FR Capabilities)")
        need = [fr for fr in self.items("FR") if starts(fr.get("priority"), "must")]
        need += self.items("NFR") + self.items("BR") + (self.items("TR") if self._t3() else [])
        for it in need:
            self.covered("X-19", it, "AC", "verifies", "in the Verifies column of any "
                         "acceptance criterion; add an AC in SP-11")
        for n in self.items("NFR"):
            self.require("X-19", n, ["target"])
        for a in self.items("AC"):
            self.require("X-19", a, ["method"])

    def check_measures(self):
        self.checked.add("X-22")
        sms = self.items("SM")
        if not sms:
            self.add("X-22", (self.files[0] if self.files else None, 1),
                     "No success measure (SM) is defined; add one to SP-10.")
        for s in sms:
            if not re.match(r"L[1-4]\b", s.get("level")):
                self.add("X-22", s, "%s Level `%s` must start with L1, L2, L3 or L4."
                         % (s.id, s.get("level")))
            if starts(s.get("level"), "l1"):
                self.require("X-22", s, ["baseline", "target", "source", "owner"], "L1 measure ")
        for b in self.items("BEN"):
            self.need("X-22", b, "measure", "SM", "success measure")
        if not self.trigger("T6"):
            return
        self.checked.add("X-23")
        for r in self.items("REC"):
            if starts(r.get("core"), "yes"):
                self.covered("X-23", r, "OC", "records", "in the Records column of any "
                             "output check (OC), but it is a Core record")
        for o in self.items("OC"):
            self.require("X-23", o, ["procedure", "frequency", "owner"], "Output check ")
        for s in sms:
            if starts(s.get("level"), "l4"):
                self.need("X-23", s, "links", "OC", "output check")

    def check_handover(self):
        self.checked.add("X-26")
        holder = self.by_id.get("SP-12") or (
            self.sections["SP-12"][0][0] if self.sections.get("SP-12") else None)
        accepted = holder is not None and holder.fm.get("status") == "Accepted"
        for a in self.items("AC"):
            result = a.get("result")
            if accepted and starts(a.get("priority"), "must") and starts(result, "not run",
                                                                          "fail"):
                self.add("X-26", a, "SP-12 is Accepted but Must criterion %s has Result `%s`."
                         % (a.id, result))
            if starts(result, "waived") and not any(
                    filled(a, c) for c in ("approver", "waived by", "verified by")):
                self.add("X-26", a, "%s is Waived but names no approver." % a.id)

    def check_staleness(self):
        if not self.today:
            return
        self.checked.add("X-28")
        for f in self.files:
            level = self.level if self.level in REVIEW_MONTHS else f.fm.get("level")
            reviewed = self._date(f.fm.get("last_reviewed", ""))
            if level in REVIEW_MONTHS and reviewed and \
                    add_months(reviewed, REVIEW_MONTHS[level]) < self.today:
                self.add("X-28", (f, f.fm_lines.get("last_reviewed", 1)), "Stale: last_reviewed "
                         "%s is more than %d months before %s (%s level); review it."
                         % (reviewed, REVIEW_MONTHS[level], self.today, level))

    # ---- small helpers
    def require(self, rule, it, cols, label=""):
        """Each column must be filled (TBD allowed only with a Q-xx in the row)."""
        for c in cols:
            if not filled(it, c):
                self.add(rule, it, "%s%s has no %s; fill it (or write TBD and add a Q-xx)."
                         % (label, it.id, c.capitalize()))

    def need(self, rule, it, col, prefix, what):
        """`it` must list at least one `prefix` ID in column `col`."""
        if not ids(it.get(col), prefix):
            self.add(rule, it, "%s lists no %s (%s ID) in %s." % (it.id, what, prefix,
                                                                 col.capitalize()))

    def covered(self, rule, it, prefix, col, where):
        """Some `prefix` item must list `it` in column `col`."""
        if not any(it.id in ids(o.get(col)) for o in self.items(prefix)):
            self.add(rule, it, "%s is not listed %s." % (it.id, where))

    def two_way(self, rule, a_prefix, a_col, b_prefix, b_col):
        """When an `a` item lists a defined `b` in a_col, that `b` must list it back in b_col."""
        for a in self.items(a_prefix):
            for b in ids(a.get(a_col), b_prefix):
                bi = self.item(b)
                if bi and a.id not in ids(bi.get(b_col), a_prefix):
                    self.add(rule, a, "%s lists %s, but %s does not list %s in %s."
                             % (a.id, b, b, a.id, b_col.capitalize()))

    def _admin_only(self, c):
        return "admin/support only" in c.get("processes").lower()

    def _t3(self):
        return self.trigger("T3") and self.in_scope("BUS-05")

    @staticmethod
    def _date(value):
        try:
            return date.fromisoformat(str(value).strip())
        except ValueError:
            return None


def load_package(root, docs="docs"):
    ddir = os.path.join(root, docs)
    if not os.path.isdir(ddir):
        raise UsageError("no documentation folder at %s" % ddir)
    paths = []
    for dirpath, dirnames, fnames in os.walk(ddir):
        dirnames.sort()
        paths += [os.path.join(dirpath, n) for n in sorted(fnames) if n.endswith(".md")]
    agents = os.path.join(root, "AGENTS.md")
    if os.path.isfile(agents):
        paths.append(agents)
    files, errors = [], []
    for p in paths:
        f = DocFile(p, os.path.relpath(p, root).replace(os.sep, "/"))
        if f.fm_error:
            errors.append(Finding("X-25", "High", f.rel, 1, "Front-matter is malformed: %s."
                                  % f.fm_error))
        elif f.fm is not None:
            files.append(f)
    return files, errors


def lint_package(root, docs="docs", today=None):
    """Lint one package; return (findings, rules checked)."""
    files, errors = load_package(root, docs)
    linter = PackageLinter(files, today)
    findings = errors + linter.run()
    findings.sort(key=lambda f: (f.rule, f.file, f.line))
    return findings, sorted(linter.checked | ({"X-25"} if errors else set()))


# --------------------------------------------------------------------------- framework lint

EXAMPLE_NAMES = re.compile(r"\b(?:%s|%s)\b" % ("L" + "HC", "I" + "TS"))
TEXT_EXT = (".md", ".py", ".txt", ".json", ".yml", ".yaml", ".toml", ".cfg")
FRAMEWORK_CHECKS = ["Template front-matter", "Template sections", "Template related",
                    "Rubric coverage", "Example names", "Consolidated guide", "Examples"]
RUBRICS = {"SP": "rubrics/03_spine_rubrics.md", "BUS": "rubrics/01_business_rubrics.md",
           "ENG": "rubrics/02_engineering_rubrics.md"}


def _md_files(root, sub):
    for dirpath, dirnames, fnames in os.walk(os.path.join(root, sub)):
        dirnames.sort()
        for n in sorted(fnames):
            if n.endswith(".md"):
                p = os.path.join(dirpath, n)
                yield DocFile(p, os.path.relpath(p, root).replace(os.sep, "/"), True)


def lint_framework(root):
    out = []

    def add(rule, file, line, msg):
        out.append(Finding(rule, "High", file, line, msg))

    # Templates: front-matter keys, standard sections, valid `related`.
    templates = set()
    for f in _md_files(root, "templates"):
        if f.fm is None:
            add("Template front-matter", f.rel, 1, "Template has no front-matter (%s)."
                % (f.fm_error or "no opening `---`"))
            continue
        templates.add(f.id)
        for k in [k for k in FM_KEYS if k not in f.fm]:
            add("Template front-matter", f.rel, 1, "Front-matter lacks `%s`." % k)
        have = {t.lower() for lvl, t, _, _ in f.headings if lvl == 2}
        for sec in [x for x in STD_SECTIONS if x.lower() not in have]:
            add("Template sections", f.rel, 1, "Missing standard section `## %s`." % sec)
        rel = f.fm.get("related", [])
        for d in [d for d in (rel if isinstance(rel, list) else [rel]) if d not in DOC_IDS]:
            add("Template related", f.rel, f.fm_lines.get("related", 1),
                "`related` lists `%s`, which is not a document ID." % d)
    for d in [d for d in DOC_IDS if d not in templates]:
        add("Template front-matter", "templates/", 0, "No template has `id: %s`." % d)

    # Rubric coverage: a `## <ID>` section per document with Yes/No flags, >= 2 critical.
    rubrics = {}
    for prefix, rel in RUBRICS.items():
        if os.path.isfile(os.path.join(root, rel)):
            rubrics[prefix] = DocFile(os.path.join(root, rel), rel, True)
        else:
            add("Rubric coverage", rel, 0, "Rubric file is missing.")
    for d in DOC_IDS:
        f = rubrics.get(d.split("-")[0])
        if f is None:
            continue
        if d not in f.sections:
            add("Rubric coverage", f.rel, 0, "No `## %s` rubric section." % d)
            continue
        tables = [t for t in f.tables if t.owner == d and "critical" in t.header
                  and "full only" in t.header]
        if not tables:
            add("Rubric coverage", f.rel, f.sections[d], "%s has no criteria table with "
                "Critical and Full only columns." % d)
            continue
        crit_yes = 0
        for t in tables:
            for n, cells, raw in t.rows:
                row = t.row_dict(cells)
                for col in ("critical", "full only"):
                    if row.get(col, "").lower() not in ("yes", "no"):
                        add("Rubric coverage", f.rel, n, "%s row has `%s` in %s; use Yes or No."
                            % (d, row.get(col, ""), col.capitalize()))
                crit_yes += row.get("critical", "").lower() == "yes"
        if crit_yes < 2:
            add("Rubric coverage", f.rel, f.sections[d], "%s has %d Critical = Yes rows; at "
                "least two are required." % (d, crit_yes))

    # Example names outside examples/, releases/, CHANGELOG.md (inline code is a mention).
    for dirpath, dirnames, fnames in os.walk(root):
        if os.path.relpath(dirpath, root).split(os.sep)[0] in (".git", "examples", "releases"):
            dirnames[:] = []
            continue
        dirnames.sort()
        for n in sorted(x for x in fnames if x.endswith(TEXT_EXT)):
            rel = os.path.relpath(os.path.join(dirpath, n), root).replace(os.sep, "/")
            if rel in ("CHANGELOG.md", "consolidated_guide.md"):  # the guide: via its sources
                continue
            with open(os.path.join(dirpath, n), encoding="utf-8", errors="replace") as fh:
                for ln, line in enumerate(fh, 1):
                    text = re.sub(r"`[^`]*`", "", line) if n.endswith(".md") else line
                    names = sorted(set(EXAMPLE_NAMES.findall(text)))
                    if names:
                        add("Example names", rel, ln, "Example name %s used outside "
                            "examples/; use a generic name." % ", ".join(names))

    # Consolidated guide.
    script = os.path.join(root, "build", "build_consolidated.py")
    if not os.path.isfile(script):
        add("Consolidated guide", "build/build_consolidated.py", 0, "Build script is missing.")
    else:
        res = subprocess.run([sys.executable, script, "--check", "--root", root],
                             capture_output=True, text=True)
        if res.returncode != 0:
            detail = " ".join((res.stdout + res.stderr).split())[:600] or "check failed"
            add("Consolidated guide", "consolidated_guide.md", 0, "Out of date or manifest "
                "incomplete: %s" % detail)

    # Example packages (any folder under examples/ holding docs/).
    for dirpath, dirnames, fnames in os.walk(os.path.join(root, "examples")):
        dirnames.sort()
        if "docs" in dirnames:
            dirnames.remove("docs")
            for msg, file, line in _lint_example(root, dirpath):
                add("Examples", file, line, msg)
    return out


def _lint_example(root, path):
    """Yield (message, file, line) problems for one example package."""
    pkg = os.path.relpath(path, root).replace(os.sep, "/")
    files, _ = load_package(path)
    dates = [d for d in (PackageLinter._date(f.fm.get("last_reviewed", "")) for f in files) if d]
    findings, _ = lint_package(path, today=max(dates or [date.today()]))
    if "/review_training/" not in "/%s/" % pkg:
        for f in findings:
            if f.severity in ("High", "Medium"):
                yield "%s %s: %s" % (f.rule, f.severity, f.message), "%s/%s" % (pkg, f.file), f.line
        return
    try:
        with open(os.path.join(path, "expected_findings.json"), encoding="utf-8") as fh:
            expected = Counter((e["rule"], e["severity"]) for e in json.load(fh))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        yield "Cannot read expected_findings.json: %s" % exc, pkg, 0
        return
    actual = Counter((f.rule, f.severity) for f in findings)
    diff = ["missing %s %s ×%d" % (r, s, c) for (r, s), c in (expected - actual).items()]
    diff += ["unexpected %s %s ×%d" % (r, s, c) for (r, s), c in (actual - expected).items()]
    if diff:
        yield "Findings differ from expected_findings.json: %s." % "; ".join(sorted(diff)), pkg, 0


# --------------------------------------------------------------------------- output

def render(findings, rules, fmt):
    for n, f in enumerate(findings, 1):
        f.id = "A-BUG-%02d" % n
    if fmt == "json":
        return json.dumps([f.as_dict() for f in findings], indent=2, ensure_ascii=False)
    lines = ["| ID | Rule | Severity | Location | Finding |", "|---|---|---|---|---|"]
    for f in findings:
        loc = "%s:%d" % (f.file, f.line) if f.line else f.file
        lines.append("| %s | %s | %s | %s | %s |" % (f.id, f.rule, f.severity, loc,
                                                    f.message.replace("|", "\\|")))
    count = Counter(f.severity for f in findings)
    lines += ["", "Linter: %d High · %d Medium · %d Low · rules checked: %s"
              % (count["High"], count["Medium"], count["Low"], ", ".join(rules) or "none")]
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Lint application documentation (see "
                                 "review/05_linter_spec.md).")
    sub = ap.add_subparsers(dest="mode", required=True)
    p = sub.add_parser("package", help="lint one application's documentation")
    p.add_argument("--docs", default="docs")
    p.add_argument("--today", help="date for staleness checks (default: today)")
    fw = sub.add_parser("framework", help="lint this framework repository")
    for sp in (p, fw):
        sp.add_argument("root")
        sp.add_argument("--format", choices=["text", "json"], default="text")
    try:
        args = ap.parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code else 0
    try:
        if args.mode == "package":
            try:
                today = date.fromisoformat(args.today) if args.today else date.today()
            except ValueError:
                raise UsageError("--today must be YYYY-MM-DD")
            findings, rules = lint_package(args.root, args.docs, today)
        else:
            if not os.path.isdir(args.root):
                raise UsageError("no such directory: %s" % args.root)
            findings = lint_framework(os.path.abspath(args.root))
            rules = FRAMEWORK_CHECKS
    except (UsageError, OSError, UnicodeDecodeError) as exc:
        print("doclint: error: %s" % exc, file=sys.stderr)
        return 2
    print(render(findings, rules, args.format))
    return 1 if any(f.severity in ("High", "Medium") for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())

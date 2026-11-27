"""Tests for tools/doclint.py and build/build_consolidated.py.

Run from the repository root:  python3 -m unittest discover -s tests

The clean fixture (tests/fixtures/clean_foundation) is a two-file Foundation
package that must lint clean. Each broken variant copies it to a temporary folder
and applies one small edit, so every test shows exactly which change breaks which rule.
"""

import contextlib
import io
import os
import shutil
import sys
import tempfile
import unittest
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO, "tools"))
sys.path.insert(0, os.path.join(REPO, "build"))

import build_consolidated  # noqa: E402
import doclint  # noqa: E402

CLEAN = os.path.join(HERE, "fixtures", "clean_foundation")
TODAY = date(2026, 10, 7)
README = "docs/README.md"


class PackageTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.pkg = os.path.join(self.tmp, "pkg")
        shutil.copytree(CLEAN, self.pkg)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, rel, old, new):
        path = os.path.join(self.pkg, rel)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn(old, text, "fixture edit did not apply")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text.replace(old, new, 1))

    def lint(self, today=TODAY):
        findings, _ = doclint.lint_package(self.pkg, today=today)
        return findings

    def rules(self, today=TODAY):
        return sorted({f.rule for f in self.lint(today)})


class CleanPackage(PackageTestCase):
    def test_clean_package_has_no_findings(self):
        self.assertEqual([(f.rule, f.message) for f in self.lint()], [])

    def test_cli_exit_code_and_formats(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = doclint.main(["package", self.pkg, "--today", "2026-10-07"])
        self.assertEqual(code, 0)
        self.assertIn("Linter: 0 High · 0 Medium · 0 Low", out.getvalue())
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(doclint.main(["package", os.path.join(self.tmp, "nope")]), 2)


class BrokenPackages(PackageTestCase):
    def test_x02_one_sided_capability_process_link(self):
        self.edit(README, "| W-01 | Submit facility request | C-01 |",
                  "| W-01 | Submit facility request | C-02 |")
        self.edit(README, "| C-01 | Log a facility request | W-01 |",
                  "| C-01 | Log a facility request | W-01 |\n| C-02 | Review requests | W-02 |")
        found = [f for f in self.lint() if f.rule == "X-02"]
        messages = " ".join(f.message for f in found)
        self.assertIn("C-01 lists W-01, but W-01 does not list C-01", messages)
        self.assertIn("W-01 lists C-02, but C-02 does not list W-01", messages)
        self.assertTrue(all(f.severity == "High" for f in found))

    def test_x03_undefined_role(self):
        self.edit(README, "| W-01 | Submit facility request | C-01 | R-01 |",
                  "| W-01 | Submit facility request | C-01 | R-07 |")
        found = [f for f in self.lint() if f.rule == "X-03"]
        self.assertEqual(len(found), 1)
        self.assertIn("R-07", found[0].message)

    def test_x03_role_name_instead_of_id(self):
        self.edit(README, "| C-01 | Log a facility request | W-01 | R-01 |",
                  "| C-01 | Log a facility request | W-01 | Staff member |")
        self.assertEqual(self.rules(), ["X-03"])

    def test_x09_capabilities_affected_mismatch_is_medium(self):
        self.edit("AGENTS.md", "| Platform help desk | C-01 |", "| Platform help desk | None |")
        found = self.lint()
        self.assertEqual([(f.rule, f.severity) for f in found], [("X-09", "Medium")])
        self.assertIn("Capabilities affected", found[0].message)

    def test_guide_blockquote_is_skipped(self):
        self.edit("AGENTS.md", "> **Guide:** template", "> **Note:** template")
        self.assertIn("X-25", self.rules())  # W-99 now counts as an undefined reference

    def test_x12_limitation_missing_from_sp12(self):
        self.edit(README, "| LIM-01 | BUS-01 | Alex Owner |", "| None | — | — |")
        found = self.lint()
        self.assertEqual([f.rule for f in found], ["X-12"])
        self.assertIn("LIM-01", found[0].message)

    def test_x19_must_fr_without_acceptance_criterion(self):
        self.edit("AGENTS.md", "| FR-01 | Store a submitted request | C-01 | Must |",
                  "| FR-01 | Store a submitted request | C-01 | Must |\n"
                  "| FR-02 | Export requests | C-01 | Must |")
        found = self.lint()
        self.assertEqual([f.rule for f in found], ["X-19"])
        self.assertIn("FR-02", found[0].message)

    def test_x19_should_fr_needs_no_criterion(self):
        self.edit("AGENTS.md", "| FR-01 | Store a submitted request | C-01 | Must |",
                  "| FR-01 | Store a submitted request | C-01 | Must |\n"
                  "| FR-02 | Export requests | C-01 | Should |")
        self.assertEqual(self.rules(), [])

    def test_x25_missing_front_matter_key(self):
        self.edit("AGENTS.md", "owner: Sam Dev, Technical owner\n", "")
        found = self.lint()
        self.assertEqual([f.rule for f in found], ["X-25"])
        self.assertIn("`owner`", found[0].message)

    def test_x25_duplicate_id(self):
        self.edit("AGENTS.md", "| CMP-01 | Form app | Collects and lists requests |",
                  "| CMP-01 | Form app | Collects and lists requests |\n"
                  "| CMP-01 | Database | Stores requests |")
        found = self.lint()
        self.assertEqual([f.rule for f in found], ["X-25"])
        self.assertIn("CMP-01 is defined twice", found[0].message)

    def test_x27_item_at_d_without_file(self):
        self.edit(README, "| BUS-08 Risk & Controls | — | — | Limitations held in BUS-01 |",
                  "| BUS-08 Risk & Controls | D | — | Raised by the owner |")
        found = self.lint()
        self.assertEqual([f.rule for f in found], ["X-27"])
        self.assertIn("BUS-08", found[0].message)

    def test_x28_stale_document_is_low(self):
        found = self.lint(today=date(2027, 10, 7))
        self.assertEqual({(f.rule, f.severity) for f in found}, {("X-28", "Low")})
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = doclint.main(["package", self.pkg, "--today", "2027-10-07", "--format", "json"])
        self.assertEqual(code, 0)  # Low findings alone do not fail the run
        self.assertIn('"id": "A-BUG-01"', out.getvalue())


class Framework(unittest.TestCase):
    def test_framework_mode_reports_missing_files_without_crashing(self):
        tmp = tempfile.mkdtemp()
        try:
            findings = doclint.lint_framework(tmp)
            rules = {f.rule for f in findings}
            self.assertIn("Rubric coverage", rules)
            self.assertIn("Template front-matter", rules)
            self.assertIn("Consolidated guide", rules)
        finally:
            shutil.rmtree(tmp)

    def test_review_training_package_matches_expected_findings(self):
        tmp = tempfile.mkdtemp()
        try:
            pkg = os.path.join(tmp, "examples", "review_training", "missing_lim")
            shutil.copytree(CLEAN, pkg)
            readme = os.path.join(pkg, README)
            with open(readme, encoding="utf-8") as fh:
                text = fh.read()
            with open(readme, "w", encoding="utf-8") as fh:
                fh.write(text.replace("| LIM-01 | BUS-01 |", "| None | BUS-01 |"))
            with open(os.path.join(pkg, "expected_findings.json"), "w") as fh:
                fh.write('[{"rule": "X-12", "severity": "High"}]')
            examples = [f for f in doclint.lint_framework(tmp) if f.rule == "Examples"]
            self.assertEqual(examples, [])
            with open(os.path.join(pkg, "expected_findings.json"), "w") as fh:
                fh.write("[]")
            examples = [f for f in doclint.lint_framework(tmp) if f.rule == "Examples"]
            self.assertEqual(len(examples), 1)
            self.assertIn("unexpected X-12 High", examples[0].message)
        finally:
            shutil.rmtree(tmp)


class Consolidated(unittest.TestCase):
    def test_build_demotes_headings_and_check_detects_drift(self):
        tmp = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(tmp, "build"))
            with open(os.path.join(tmp, "build", "manifest.txt"), "w") as fh:
                fh.write("# comment\n\nA.md\n")
            with open(os.path.join(tmp, "A.md"), "w") as fh:
                fh.write("---\nid: X\n---\n# Title\n\n```text\n# not a heading\n```\n## Sub\n")
            quiet = contextlib.redirect_stdout(io.StringIO())
            with quiet, contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(build_consolidated.main(["--root", tmp]), 0)
                self.assertEqual(build_consolidated.main(["--root", tmp, "--check"]), 0)
            with open(os.path.join(tmp, "consolidated_guide.md")) as fh:
                out = fh.read()
            self.assertIn("## Title\n", out)
            self.assertIn("### Sub\n", out)
            self.assertIn("\n# not a heading\n", out)
            self.assertIn("- [A.md](#amd)", out)
            with open(os.path.join(tmp, "B.md"), "w") as fh:
                fh.write("# Unlisted\n")
            err = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
                self.assertEqual(build_consolidated.main(["--root", tmp, "--check"]), 1)
            self.assertIn("B.md", err.getvalue())
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()

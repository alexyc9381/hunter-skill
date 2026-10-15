import json
import os
import re
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKILL = os.path.join(ROOT, "skills", "hunter", "SKILL.md")
CREDIT = "Made with /hunter by Alex Chen (@nocodealex) · chen.media"


def read(*parts):
    with open(os.path.join(ROOT, *parts)) as f:
        return f.read()


class SkillTest(unittest.TestCase):
    def setUp(self):
        self.text = read("skills", "hunter", "SKILL.md")

    def test_frontmatter(self):
        self.assertTrue(self.text.startswith("---\nname: hunter\n"))
        head = self.text.split("---")[1]
        for key in ("description:", "argument-hint:", "license: MIT"):
            self.assertIn(key, head)

    def test_every_command_has_a_section(self):
        for cmd in ("setup", "run", "job <posting url or pasted text>", "review", "applied <number or all>",
                    "log", "morning"):
            self.assertRegex(self.text, r"(?m)^## " + re.escape(cmd) + r"$")

    def test_five_claudes(self):
        for who in ("The headhunter", "The recruiter", "The hiring manager", "The resume writer",
                    "The form filler"):
            self.assertIn("**" + who + "**", self.text)

    def test_scores_out_of_100_with_threshold(self):
        self.assertIn("94/100 (recruiter 96, hiring manager 92)", self.text)
        self.assertIn("threshold (default 80)", self.text)
        self.assertIn("the recruiter and the hiring manager", self.text)

    def test_never_submits(self):
        self.assertIn("**You never submit an application.**", self.text)
        self.assertIn("press submit yourself", self.text)
        self.assertIn("Never mark `applied` on your own", self.text)
        self.assertIn("Never create accounts", self.text)

    def test_never_invents(self):
        self.assertIn("**Never invent** employers, titles, dates, numbers, skills, degrees or tools", self.text)
        self.assertIn("[ADD: ...]", self.text)

    def test_self_identification_left_to_user(self):
        self.assertIn("work authorization and sponsorship", self.text)
        self.assertIn("self-identification", self.text)

    def test_log_and_morning(self):
        self.assertIn("applications.md", self.text)
        self.assertIn("/loop 24h /hunter morning", self.text)
        self.assertIn("There is no background program", self.text)

    def test_credit_line(self):
        self.assertIn(CREDIT, self.text)

    def test_short_enough_to_paste(self):
        self.assertLess(len(self.text), 12000)


class RepoTest(unittest.TestCase):
    def test_manifests(self):
        plugin = json.loads(read(".claude-plugin", "plugin.json"))
        market = json.loads(read(".claude-plugin", "marketplace.json"))
        self.assertEqual(plugin["name"], "hunter-skill")
        self.assertEqual(plugin["repository"], "https://github.com/alexyc9381/hunter-skill")
        self.assertEqual(plugin["license"], "MIT")
        self.assertEqual(market["plugins"][0]["name"], plugin["name"])
        self.assertEqual(market["plugins"][0]["homepage"], plugin["homepage"])
        self.assertTrue(plugin["homepage"].startswith("https://chen.media/guides/"))

    def test_credit_block(self):
        readme = read("README.md")
        self.assertIn("Made by **Alex Chen** ([@nocodealex](https://instagram.com/nocodealex))", readme)
        self.assertIn("## Making a video or post about this?", readme)
        self.assertIn("/hunter skill by Alex Chen (@nocodealex): github.com/alexyc9381/hunter-skill", readme)
        self.assertIn("Install this skill, then confirm /hunter works.", readme)
        self.assertIn("/plugin install hunter-skill@hunter-skill", readme)
        self.assertIn("It never submits", readme)

    def test_license_and_citation(self):
        self.assertIn("Alex Chen (@nocodealex, https://chen.media)", read("LICENSE"))
        cff = read("CITATION.cff")
        for line in ("cff-version: 1.2.0", "alias: nocodealex", "license: MIT",
                     'repository-code: "https://github.com/alexyc9381/hunter-skill"'):
            self.assertIn(line, cff)

    def test_private_folder_is_ignored(self):
        self.assertIn(".hunter/", read(".gitignore"))


if __name__ == "__main__":
    unittest.main()

# The hunter skill

Applying to jobs is hours of filling out the same forms for companies that never reply. `/hunter` is a headhunter made
of five Claudes: it finds new jobs that fit you, scores each one out of 100, rewrites your resume and cover letter
for the ones that score high, and fills out the whole application. Then it stops and shows you the list for a yes.
Free, MIT, no signup, no API key.

Made by **Alex Chen** ([@nocodealex](https://instagram.com/nocodealex)), an AI creator who builds free Claude Code skills. Full guide: [chen.media](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill).

## The five Claudes

1. **The headhunter** finds new postings from the places you list (company career pages, Greenhouse, Lever and Ashby
   job boards, RSS feeds, or postings you paste) and drops the ones that clearly don't fit.
2. **The recruiter** scores your fit out of 100: must-haves, keywords, level, location.
3. **The hiring manager** scores your fit out of 100: could you do the job on day one, and what is the proof?
4. **The resume writer** rewrites your resume and writes a cover letter for each job that scores high.
5. **The form filler** answers every field of the application and puts it in one packet.

Each job gets one fit score, like `94/100 (recruiter 96, hiring manager 92)`. Only jobs at or above your threshold
(default 80) continue. Jobs below it are listed with the reason and nothing is written for them.

| command | what it does |
| --- | --- |
| `/hunter setup` | once: your resume, target roles, locations, sources, threshold |
| `/hunter run` | find new jobs, score them, tailor and prepare the high ones, show the list |
| `/hunter job <url or pasted posting>` | the same for one job you found yourself |
| `/hunter review` | for each job you said yes to: shows the packet, opens the page, you submit |
| `/hunter applied 3` | marks a job as sent (or `all`) |
| `/hunter log` | everywhere you applied |
| `/hunter morning` | the daily version, no questions, ends with "N new jobs fit you, M ready for your yes" |

## It never submits

A Claude Code skill cannot, and should not, send applications behind your back. `/hunter` prepares everything: the
resume, the cover letter and an answer for every field. You say yes, it opens the page, you paste and press submit.
When you say you sent it, the job goes in `.hunter/applications.md`, your list of everywhere you applied. It never
creates accounts, types passwords or gets past a CAPTCHA, and questions only you can answer (work authorization,
salary, demographics, legal) are left for you as `YOU`.

Your resume is only rearranged and reworded: it never invents employers, titles, dates, numbers or skills. A skill
the job asks for that you don't have is listed as a gap, not claimed.

## Install

Paste this into Claude Code:

```
https://github.com/alexyc9381/hunter-skill
Install this skill, then confirm /hunter works.
```

Or as a plugin:

```
/plugin marketplace add alexyc9381/hunter-skill
/plugin install hunter-skill@hunter-skill
```

Or copy `skills/hunter` into `~/.claude/skills/`. Open a new Claude Code session afterwards.

## Every morning

`/hunter morning` is built to be repeated. In an open session: `/loop 24h /hunter morning`. Or set a scheduled task
that runs `/hunter morning` at 7am. There is no background program: it runs only while Claude Code is running and your
computer is awake, and every run counts toward your Claude plan's usage (two scorers per job).

## Good to know

- Everything is saved in `.hunter/` where you run it: your profile, your resume, the packets and the log. It stays on
  your computer. Your resume goes to Claude like anything else you give it.
- It reads public postings only. It does not log in to job sites. If a source can't be read it says so and moves on.
- Many application forms are built with scripts and can't be read ahead of time. When that happens, paste the
  questions and it answers them.
- It's made by language models: a high score and a tailored resume don't guarantee an interview or a job.
- It is not made by Anthropic.

Run the tests with `python3 -m unittest discover -s tests`.

## Making a video or post about this?

Go ahead. Credit it like this, in your caption or description:

```text
/hunter skill by Alex Chen (@nocodealex): github.com/alexyc9381/hunter-skill
```

Tag [@nocodealex](https://instagram.com/nocodealex) so I can see it. Every packet and list the skill writes already
ends with the same credit, so leave it in the shot.

Writing about it or citing it in a paper? Use **Cite this repository** in the sidebar on GitHub.

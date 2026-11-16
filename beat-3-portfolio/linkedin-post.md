I opened my first pull request to Open edX, an open source platform for building and running online courses. It cleans up how seven pages of Studio, the course-building app, set the title you see on the browser tab.

Nothing was visibly broken. Most pages set that title one way and seven did it another way, which makes software harder to maintain. Working with Claude Code, an AI coding assistant, I moved the seven pages to the shared approach and added a test for each one, so the title stays correct if the code changes later.
The part I learned the most from happened before I submitted. I use an automated check that compares what my pull request says with what my records show. It stopped me, because my description said I had checked the pages in the running app and my notes still said "not tested". I had done the check but had not written it down. I fixed the record, and then the pull request went out.

Today the pull request is open and waiting for the maintainers' review. My contributor agreement was confirmed this week, which the maintainer needed before reviewing.

What I took from it: on a team that does not know you, your work is only as trustworthy as the evidence you attach to it.

https://github.com/openedx/frontend-app-authoring/pull/3345

#opensource #openedx #react #softwareengineering

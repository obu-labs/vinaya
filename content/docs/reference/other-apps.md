---
weight: 710
title: "Other Notes Apps"
description: "Information on using the notebook with apps other than Obsidian."
date: "2025-07-03T11:44:14+07:00"
toc: true
---

While the Vinaya Notebook was built to work with Obsidian, it also works well with:
 - [Zettlr](https://zettlr.com/)
 - [QOwnNotes](https://www.qownnotes.org/)
 - [Notable](https://notable.app/)

If you use one of these apps, you'll have to periodically update your folder manually.
For installing in these apps, see the app-specific instructions below.

The vault is **not** currently compatible with:
  - [Joplin](https://joplinapp.org/)
    - When importing Markdown notes with Frontmatter, Joplin currently doesn't read the file names.
    - This will be fixed in version 3.5 thanks to [this commit](https://github.com/laurent22/joplin/commit/b2cdfd6358cbd0b9f4d864413f5facb6209ff3e6).
  - [Logseq](https://logseq.com/)
    - Logseq doesn't understand local Markdown links and has no plans to support them.
    - See [this discussion](https://github.com/logseq/logseq/discussions/8003) for more details.


## Zettlr

To install in Zettlr, merely extract the archive anywhere, then select
"File -> Open Workspace" and open the vault folder.

## QOwnNotes

In QOwnNotes, either extract the vault to your "default" notes folder
or go to "Settings -> Note folders" and "Add folder" pointing to where you extracted
the archive.
Be sure to select the "Use note subfolders" option in either case.

## Notable

Notable has a "Data Directory."  To import the vault into Notable,
"Open Data Directory" and then extract the zip archive there.
Note that you may need to restart the app to see the notes.

## Feedback

If you use these or any other Markdown-compatible notes app and notice an issue,
feel free to [report it](https://github.com/obu-labs/vinaya/issues).
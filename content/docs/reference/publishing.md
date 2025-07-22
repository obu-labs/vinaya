---
weight: 721
title: "Publishing Your Module"
description: "How to publish your own Vinaya Notebook Module."
icon: "ios_share"
date: "2025-07-22T14:16:02+07:00"
toc: true
---

To share your own notes with your friends, you simply have to send them the folder from your Vault and have them copy it into their own Vinaya Notebook.

The rest of this guide will cover what it takes to create a module that the Vinaya Notebook Plugin can track and keep up-to-date.

## Creating and Hosting Your VNM on GitHub

The easiest way to host your module is using [GitHub](https://github.com).

The steps are as follows:

1. Sign up for [a GitHub account](https://github.com/signup) if you don't have one already.
2. Using the [Vinaya Notes Module Template](https://github.com/obu-labs/vinaya-notes-module) repository, [create your own repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
3. Follow the instructions in its [README.md](https://github.com/obu-labs/vinaya-notes-module/blob/main/README.md) to finish setting it up.

The template repository contains a [GitHub Actions Script](https://docs.github.com/en/actions/get-started/understanding-github-actions)
which, after you [enable it](https://github.com/obu-labs/vinaya-notes-module/blob/d553a34f23f0491e1bc74eca9a62e6e307ea9577/.github/workflows/release.yaml#L10-L12), will create a new release of your module whenever you commit changes to your repository.
Once the build succeeds and you have your first release, people can [add your module](../guides/modules/#adding-a-new-module) to their vault using your vnm URL:

```
https://github.com/your-username/your-repo-name/releases/latest/download/manifest.vnm
```

## Custom Hosting

If you'd prefer to host your module yourself, you can!

Simply put up a ZIP Archive of your folder and a [valid VNM File](vnm) anywhere on the internet and your module can now be added in the Vinaya Notebook Plugin!

Feel free to email me at Khemarato Bhikkhu (at gmail.com) if you have any questions or suggestions on the publishing process or if you'd like to get your module added to the default modules list.


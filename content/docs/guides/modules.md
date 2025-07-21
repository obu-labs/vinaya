---
weight: 216
title: "Managing Modules"
description: "Using the Vinaya Notebook Obsidian Plugin"
icon: "rule_folder"
date: "2025-07-21T11:55:46+07:00"
toc: true
---

## Updating Modules

Once you enable the Vinaya Notebook Plugin, your synced modules will automatically
check for updates periodically on Obsidian startup.
You may continue to use Obsidian normally while updates are applied in the background,
but please do not close the Vault or Obsidian while updates are in progress.

To manually trigger an update, run "**Vinaya Notebook: Update**" from [the Command Palette](https://help.obsidian.md/plugins/command-palette)
or click the "**Update Now**" button in the Vinaya Notebook Settings page.

## Deleting a Module

If, for whatever reason, you don't want a particular module, you may simply delete its folder:

![Deleting a Module](/images/screenshots/bmc_delete.png)

On Desktop, right click. On mobile, long press.
Then select "Delete" from the context menu.

After deleting a module in Obsidian, you will be automatically unsubscribed from it.

### Unsubscribing from a Module

If you'd like to stop receiving updates for a given module, but keep the folder in your vault,
you may toggle the module off {{< icon toggle_off >}} in the Vinaya Notebook Settings page:

![Plugin Settings Page](/images/screenshots/plugin_settings.png)

To open the settings, click the {{< icon settings >}} icon on your vault sidebar, and then select the "Vinaya Notebook" tab.

### Deleting a Submodule

Some modules will come with "submodules." These are subfolders within the module related to a particular theme.
If you're not interested in a submodule, you can delete it by selecting the {{< icon delete >}} button next to the submodule.

## Restoring

If you'd like to restore a deleted module, simply toggle it back on {{< icon toggle_on >}} in the Vinaya Notebook Settings page.

To restore a deleted submodule, select the {{< icon download >}} button next to it.

## Adding a New Module

If someone gives you the link to a "vnm" (Vinaya Notebook Module) file,
you can add it by pasting it into the "**Add Module**" field in the settings page and clicking the {{< icon add >}} button.

If someone sends you a zip archive of a module, simply extract it into your vault using your file browser.


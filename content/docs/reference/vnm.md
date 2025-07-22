---
weight: 746
title: "The VNM File"
description: "Details about the VNM File Format."
icon: "data_object"
date: "2025-07-22T15:05:34+07:00"
toc: true
---

The main file for representing a module is its "**vnm**" file.

A VNM file is a [JSON Object file](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON)
that contains the following metadata about your module:

- **folder**: The name of the module.
- **description**: A short description of the module: who is the author, etc.
- **version**: the latest version number in "1.2.3" format (semver: used to tell when an update is needed).
- **more_info**: A link to your module's homepage.
- **zip**: A link to the zip file containing the contents of the module.
- **submodules**: A list of submodules under this module (see below)
- **requires**: A recursive Trie of what other modules (and their subfolders) your module links to (see below)

The VNM File for your module (and its zip file) can be hosted anywhere on the open web.
Simply create a JSON file with the above fields and send people a link to it and they can
[then add the module to their Vault](../guides/modules/#adding-a-new-module).

For a reference example of a valid VNM File, see [the "Canon (Pali)" VNM](https://github.com/obu-labs/pali-vinaya-notes/releases/latest/download/manifest.vnm).


## Submodules

A submodule is a self-contained portion of your module which users can choose to unsubscribe from in the Vinaya Notebook Plugin.

A submodule (in the VNM JSON) is a dictionary with the following fields:

- **name**: The name of the submodule.
- **paths**: A list of the folders in your module comprising the submodule.
- **requires**: A Trie (see below) of the other modules this submodule links to.

Note that because "**paths**" is a list of subdirectories, a submodule's notes cannot be mixed together in the same folder with non-submodule notes.

## The "requires" Field

If your module's notes contain links to other modules, you should add those modules to the "requires" field so that the Vinaya Notebook Plugin can warn people if they try to unsubscribe from your module's requirements.

The requires field's value should be a dictionary where the keys are other module names and its (sub)values are also dictionaries.
These inner dictionaries should have keys for each of that module's subfolders that you refer to mapping to their subdirectories, recursively.

For example, if your module has a link to `Canon (Pali)/Vibhanga/Bhikkhu/1 - Parajika/The Bhikkhu Pārājikas.md`,
then your "requires" field would look like this:

```json
{
  "Canon (Pali)": {
    "Vibhanga": {
      "Bhikkhu": {
        "1 - Parajika": {}
      }
    }
  }
}
```

For the reference implementation of how to build this "requires" field automatically, see [vinaya-notes-module-releaser/calculate_requirements.py](https://github.com/obu-labs/vinaya-notes-module-releaser/blob/main/calculate_requirements.py).

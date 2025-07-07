#!/bin/python3

import hashlib
import json
from typing import List, Dict
from pathlib import Path
import time
import zipfile

import requests
import yaml

REPO_ROOT = Path(__file__).parent.parent
HUGO_DATA_DIR = REPO_ROOT / "data"
VNMS_FILE = HUGO_DATA_DIR / "vnms.yaml"
LOCAL_VNMS_DATA = yaml.safe_load(VNMS_FILE.read_text())
THIS_DIR = Path(__file__).parent
DATA_DIR = THIS_DIR / "data"
PLUGIN_DIR = DATA_DIR / "Vinaya Notebook"
VNMS = {}
LOCAL_FOLDERS = {}
INSTALLED = {}

def now() -> int:
  return int(time.time() * 1000)
NOW = now()

# Has to work the same way as the Obsidian Plugin Algo does
# See: https://github.com/obu-labs/vinaya-notebook/blob/main/src/hashutils.ts
def hash_for_file_list(file_list: List[Dict[str, str]]) -> str:
  """
  Generate a hash for a list of files based on their paths and hashes.
  
  Args:
    file_list: List of dictionaries with 'path' and 'hash' keys
    
  Returns:
    SHA256 hash of the combined file data
  """
  # Sort by hash so it's order agnostic
  file_list.sort(key=lambda x: x['hash'])
  
  runninghash = hashlib.sha256()
  for file_info in file_list:
    runninghash.update(file_info['path'].encode('utf-8'))
    runninghash.update(file_info['hash'].encode('utf-8'))
  
  # Hash the combined data
  return runninghash.hexdigest()


def hash_for_folder(folder_path: Path) -> str:
  """
  Generate a hash for all files in a folder and its subfolders.
  
  Args:
    folder_path: Path object pointing to the folder to hash
    
  Returns:
    SHA256 hash representing all files in the folder structure
  """
  file_list: List[Dict[str, str]] = []
  
  # Use pathlib's rglob to recursively find all files
  for file_path in folder_path.rglob('*'):
    if file_path.is_file():
      # Read file content and compute hash
      content = file_path.read_bytes()
      file_hash = hashlib.sha256(content).hexdigest()
      
      # Store relative path from the base folder
      relative_path = file_path.relative_to(folder_path)
      file_list.append({
        'path': str(relative_path),
        'hash': file_hash
      })
  
  return hash_for_file_list(file_list)

print("Downloading the latest Vinaya Notes Plugin...")
headers = {
  "Accept": "application/vnd.github+json"
}
token = None
if 'GITHUB_TOKEN' in os.environ:
  token = os.environ['GITHUB_TOKEN']
if 'GH_TOKEN' in os.environ:
  token = os.environ['GH_TOKEN']
if token:
  headers['Authorization'] = f"Bearer {token}"
PLUGIN_RELEASE = requests.get(
  "https://api.github.com/repos/obu-labs/vinaya-notebook/releases/latest",
  headers=headers
).json()
latest_release = PLUGIN_RELEASE["tag_name"]
LOCAL_FOLDERS["Vinaya Notebook"] = PLUGIN_DIR / latest_release
if LOCAL_FOLDERS["Vinaya Notebook"].exists():
  print("  Already have the latest version of the Vinaya Notebook plugin!")
else:
  LOCAL_FOLDERS["Vinaya Notebook"].mkdir(parents=True)
  print(f"  Downloading v{latest_release}...")
  for asset in PLUGIN_RELEASE["assets"]:
    print(f"    {asset['name']}")
    req = requests.get(asset["browser_download_url"])
    with open(LOCAL_FOLDERS["Vinaya Notebook"] / asset["name"], "wb") as f:
      f.write(req.content)

for folder, vnm in LOCAL_VNMS_DATA.items():
  print("Downloading the {} VNM...".format(folder))
  r = requests.get(vnm['vnm'])
  VNMS[folder] = r.json()
  LOCAL_FOLDERS[folder] = DATA_DIR / folder / VNMS[folder]["version"]
  if LOCAL_FOLDERS[folder].exists():
    print("  Already have the latest version of the {} folder!".format(folder))
  else:
    LOCAL_FOLDERS[folder].mkdir(parents=True)
    zip_url = VNMS[folder]["zip"]
    print("  Downloading {}'s zip archive...".format(folder))
    zr = requests.get(zip_url)
    ZIP_FILE = DATA_DIR / folder / f"{VNMS[folder]['version']}.zip"
    ZIP_FILE.write_bytes(zr.content)
    print("  Extracting...")
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
      zip_ref.extractall(LOCAL_FOLDERS[folder])
  INSTALLED[folder] = {
    "version": VNMS[folder]["version"],
    "hash": hash_for_folder(LOCAL_FOLDERS[folder])
  }
    
print("Writing vinaya-notes.zip vault archive...")
# You must keep this Plugin Data in sync with the Obsidian Plugin
# https://github.com/obu-labs/vinaya-notebook/blob/main/src/main.ts#L17
plugin_data = {
  "canonicalVNMs": {},
  "knownFolders": {},
  "lastUpdatedTimes": {
    "VNMList": NOW,
  },
  "installedFolders": INSTALLED
}
with zipfile.ZipFile(REPO_ROOT / "static" / "vinaya-notes.zip", "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zip:
  for folder, vnm in VNMS.items():
    plugin_data["canonicalVNMs"][folder] = LOCAL_VNMS_DATA[folder]["vnm"]
    plugin_data["knownFolders"][folder] = VNMS[folder]
    plugin_data["lastUpdatedTimes"][folder + " VNM"] = NOW
    plugin_data["lastUpdatedTimes"][folder + " Folder"] = NOW
    print(f"  Writing {folder} data to the zip...")
    local_folder = LOCAL_FOLDERS[folder]
    for f in local_folder.rglob("*"):
      if f.is_file():
        zip.write(f, arcname=folder + "/" + str(f.relative_to(local_folder)))
  print("  Writing Obsidian data to the zip...")
  zip.write(THIS_DIR / "app-settings.json", arcname=".obsidian/app.json")
  # Currently I have the tags pain turned off. Reenable if we ever use tags
  zip.write(THIS_DIR / "core-plugins.json", arcname=".obsidian/core-plugins.json")
  zip.writestr(".obsidian/backlink.json", '{"backlinkInDocument": true}')
  zip.write(THIS_DIR / "webviewer.json", arcname=".obsidian/webviewer.json")
  zip.writestr(".obsidian/community-plugins.json", '["vinaya-notebook"]')
  zip.writestr(".obsidian/plugins/vinaya-notebook/data.json", json.dumps(plugin_data, indent=2))
  for f in LOCAL_FOLDERS["Vinaya Notebook"].rglob("*"):
    zip.write(
      f,
      arcname=".obsidian/plugins/vinaya-notebook/" + str(f.relative_to(LOCAL_FOLDERS["Vinaya Notebook"]))
    )

print("Done!")

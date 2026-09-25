#!/usr/bin/env python3

import shutil
from subprocess import PIPE
from pathlib import Path
import hashlib
from send2trash import send2trash

class hashedFile:
    def __init__(self, name, hash):
        self.name = name
        self.hash = hash

def fileHasher(file):
    hasher = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

def dupeFiltering(folder):
    seen = {}

    for file in folder.iterdir():
        if file.is_file():
            hash = fileHasher(file)
            if hash in seen: #file already in set
                print(f"Possible duplicate:\n  Keep: {seen[hash]}\n  Match: {file}\n")
            else:
                seen[hash] = file #add file to seen set



def createNewFolder(parentFolder, name: str):
    folderPath = parentFolder / name
    folderPath.mkdir(parents=True, exist_ok=True)

def createFolders(parentFolder, folderDict):
    for key in folderDict.keys():
        createNewFolder(parentFolder, key) #create folder with type name

def mvFile2Folder(file, folderDict):
    ext = file.suffix.lower()
    folder = 'Misc'

    for folderName, extensions in folderDict.items():
        if ext and ext in extensions:
            folder = folderName
            break

    destination = file.parent / folder / file.name

    if destination.exists() or destination.is_symlink():
        print(f"Skipped {file.name}: already exists in {folder}")
        return

    shutil.move(file, destination)

def main():
    folderTypes = {
    'Images': [
        '.png', '.jpg', '.jpeg', '.gif', '.webp',
        '.heic', '.avif', '.svg', '.bmp', '.tif', '.tiff', '.ico'
    ],
    'Documents': [
        '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.md'
    ],
    'Spreadsheets': [
        '.xls', '.xlsx', '.csv', '.tsv', '.ods'
    ],
    'Presentations': [
        '.ppt', '.pptx', '.key', '.odp'
    ],
    'Archives': [
        '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'
    ],
    'Installers': [
        '.dmg', '.pkg', '.exe', '.msi', '.msix', '.iso'
    ],
    'Audio': [
        '.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg', '.aiff'
    ],
    'Videos': [
        '.mp4', '.mov', '.mkv', '.avi', '.webm', '.m4v'
    ],
    'Code': [
        '.py', '.js', '.ts', '.html', '.css', '.json',
        '.xml', '.yaml', '.yml', '.sh', '.bat', '.ps1', '.sql'
    ],
    'Fonts': [
        '.ttf', '.otf', '.woff', '.woff2'
    ],
    'Misc': []
}
    downloads = Path.home() / "Downloads"
    createFolders(downloads, folderTypes)

    dupeFiltering(downloads)

    for item in downloads.iterdir():
        if item.is_file():
            mvFile2Folder(item, folderTypes)


if __name__ == "__main__":
    main()
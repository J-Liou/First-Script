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
                send2trash(file)
                print(f"{file} file moved to trash")
            else:
                seen[hash] = file #add file to seen set



def createNewFolder(parentFolder, name: str):
    folderPath = parentFolder / name
    folderPath.mkdir(exists_ok=True)

def createFolders(parentFolder, folderDict):
    for key in folderDict.keys():
        createNewFolder(parentFolder, key) #create folder with type name

def mvFile2Folder(file, folderDict):
    ext = Path(file).suffix.lower()
    for folderName, extensions in folderDict.items():
        if ext and ext in extensions: #file suffix aligns with a organized folder
            destFolder = file.parent / folderName
            shutil.move(file, destFolder)
    else:
        shutil.move(file, file.parent / 'Misc')

def main():
    folderTypes = {
        'Images': ['.png', '.jpg', '.jpeg'],
        'Files': ['.pdf', '.docx'],
        'Executables': ['.exe'],
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
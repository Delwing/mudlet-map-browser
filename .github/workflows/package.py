from zipfile import ZipFile
import os
from os.path import basename

ignoreFiles = [
    ".gitignore",
    ".gitattributes",
    "images/logo.png"
]

def addDirToZip(zipObj, dirName):
    for folderName, subfolders, filenames in os.walk(dirName):
        for filename in filenames:
            filePath = os.path.join(folderName, filename)
            basePath = os.path.relpath(filePath, dirName)
            if(not basePath.startswith(".git") and not filePath in ignoreFiles):
                print(filePath, basePath)
                zipObj.write(filePath, basePath)

with ZipFile("mudlet-map-reader.mpackage", "w") as zipObj:
    addDirToZip(zipObj, "mudlet-map-reader")
    zipObj.write("config.lua")
    zipObj.write("standalone.xml")
    zipObj.write("favicon.ico", "favicon.ico")
    zipObj.write("logo.png", "images/logo.png")
#!/usr/bin/env python

import os
import sys
import shutil
import re
import subprocess
import zipfile as zf

# Evaluate parameters before starting
argSet = set()
for arg in sys.argv[1:]:
    argSet.add(arg)

# Set of student names:
students = set()
# Messages to output at the end of everything:
outputMessages = []

# List of files to compile, unzip, and do other operations to
javaFilesToCompile = set()
zipFilesToUnzip = set()

# Add students to set and make folders for each of them.
for file in os.listdir("./"):
    student = file.split("_")[0]
    students.add(student)

    # Make directory for the student...
    studentdir = "./" + student
    if not os.path.isdir(studentdir):
        os.mkdir(studentdir)
        print("Folder created for: " + student)

    # Move student file to their directory that should exist by now.
    if os.path.isfile(file):
        shutil.move(file, studentdir + "/" + file)

# Now we step through the whole file tree, renaming files appropriately.
for folderName, subFolders, fileNames in os.walk("./"):
    # print("Processing folder: " + folderName)

    # Reference filename: lastfirst_late_4145_839726_Exercise11_01-1.java
    for filename in fileNames:
        # Piece together file names
        fileSplit = filename.split("_")

        # Preserve file extension.  
        fileExtension = filename.split(".")[-1]

        # name starts at index 3 if not late, if late then index 4
        startIndex = 3
        if "_late_" in filename:
            startIndex = 4
            outputMessages.append("[late] " + filename + " was submitted late.")
        className = fileSplit[startIndex] 
        # If there are additional underscores, append them to the class name.
        for piece in fileSplit[(startIndex + 1):]:
            className += "_" + piece

        # Get rid of any additional submission marks, like -1.java or -2.java
        className = re.sub("-[0-9]*." + fileExtension, "." + fileExtension, className)

        # Rename the files to their original names.
        dirName = folderName + "/"
        shutil.move(dirName + filename, dirName + className)

        if className.endswith(".java"):
            javaFilesToCompile.add(dirName + className)
        elif className.endswith(".zip"):
            zipFilesToUnzip.add(dirName + className)

# After the walk, do some operations.
# The file names in each set look like: ./lastfirst/Exercise12_21.java
# java: attempt to compile java files.
if "java" in argSet:
    for sourceFile in javaFilesToCompile:
        workingDir =  "./" + sourceFile.split("/")[1]
        filename = sourceFile.split("/")[2]

        exitCode = subprocess.call(["javac", filename],
                                cwd=workingDir)
        if exitCode != 0:
            outputMessages.append("[javac] " + sourceFile + "failed to compile.")

# zip: unzip submitted zip files.
if "zip" in argSet:
    for zipFileName in zipFilesToUnzip:
        try:
            zipFileNameSplit = zipFileName.split("/")
            zipFile = zf.ZipFile(zipFileName, "r")
            # ./lastfirst/zipfilename/
            targetDir = "./" + zipFileNameSplit[1] + "/" + zipFileNameSplit[2].split(".")[0]
            zipFile.extractall(targetDir)
            zipFile.close()
        except Exception, e: 
            outputMessages.append("[zip] " + zipFileName + " failed to extract: " + e)

# Sort and display output messages.
outputMessages.sort()
for message in outputMessages:
    print(message)

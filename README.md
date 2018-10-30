# Quick Grade

# Usage:
```
./main.py [options]
    Available options:
        java: compile any .java submissions.
        zip: unzip any .zip submissions.
```

What quick grade does not do:

1. All of the work for you.

What quick grade does do:

1. Organizes student submissions into their own folders.

2. Renames files to their original names.

3. Notifies you of assigments that were submitted late.

4. Automatically compiles .java files, and notifies you of compilation failures. (javac must be in your system path)

5. Automatically unzips .zip files and places their contents in their own subfolders.

# TODO:

1. Modularize the script to allow for scalability.

2. Automatically generate grade sheet for each student (xlsx).

3. Sometimes, .zips might contain .java files, or even more .zip files: recursive processing of files.
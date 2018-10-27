#!/usr/bin/env python

import os

# Set of student names:
students = set()

# Add students to set and make folders for each of them.
for file in os.listdir("./"):
    student = file.split("_")[0]
    if (file.endswith('.java')):
        students.add(student)


    studentdir = "./" + student
    if not os.path.isdir(studentdir):
        os.mkdir(studentdir)
        print("Folder created for: " + student)

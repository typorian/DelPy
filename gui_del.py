#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:15:40 2019

@author: eidorian
"""

from appJar import gui
from os import listdir, remove, mkdir, rename
from os.path import isfile, join, exists
from tkinter.filedialog import askdirectory

def press(button):
    if button == "Exit":
        app.stop()
    elif button == "Help":
        app.setMessage("output", "DelPy is meant to help discard unneeded files based on file extensions.\nThe directory with sorted images is the reference directory. The directory with images to delete is compared to the read directory.\nAll files that are present in both are kept, files only present in the delete directory are discarded.")
    elif button == "Delete!":
         read_dir = app.getEntry("Directory with sorted images")
         delete_dir = app.getEntry("Directory with images to be deleted")
         read_extension = app.getEntry("Extension of sorted images")
         delete_extension = app.getEntry("Extension of images to be deleted")
         app.setMessage("output",  "Read dir: "+read_dir+"\nDelete dir: "+delete_dir)
         angst = False
         delete_images(read_dir, delete_dir, read_extension, delete_extension, angst)
    else:
         read_dir = app.getEntry("Directory with sorted images")
         delete_dir = app.getEntry("Directory with images to be deleted")
         read_extension = app.getEntry("Extension of sorted images")
         delete_extension = app.getEntry("Extension of images to be deleted")
         app.setMessage("output",  "Read dir: "+read_dir+"\nDelete dir: "+delete_dir)
         angst = True
         delete_images(read_dir, delete_dir, read_extension, delete_extension, angst)

def delete_images(read_dir, delete_dir, read_extension, delete_extension, angst):
    readlist = [f[:-len(read_extension)] for f in listdir(read_dir) if f[-len(read_extension):] == read_extension and isfile(join(read_dir, f))]

    for f in listdir(delete_dir):
        if isfile(join(delete_dir, f)):
            #next line not added
            if not f[:-len(delete_extension)] in readlist and f[-len(delete_extension):] == delete_extension:
                if angst:
                    trash = delete_dir + 'trash\\'
                    if not exists(trash):
                        mkdir(trash)
                    app.setMessage("output", "Moving file: {}".format(f))
                    rename(join(delete_dir,f), join(trash, f))
                else:
                    app.setMessage("output", "Deleting file: {}".format(f))
                    remove(join(delete_dir,f))

def path_setter_read(button):
    read_dir = askdirectory()
    app.setEntry("Directory with sorted images", read_dir)

def path_setter_write(button):
    delete_dir = askdirectory()
    app.setEntry("Directory with images to be deleted", delete_dir)


app = gui("Picture sorter")
app.setStretch("column")

app.addEntry("Directory with sorted images", 0, 0)
app.setEntryDefault("Directory with sorted images", "Path to sorted images")
app.addButton("Choose read path", path_setter_read, 0, 1)
app.addEntry("Extension of sorted images")
app.setEntryDefault("Extension of sorted images", "set extension of sorted images")
app.addEntry("Directory with images to be deleted", 2, 0)
app.setEntryDefault("Directory with images to be deleted", "Path to images to be deleted")
app.addButton("Choose delete path", path_setter_write, 2, 1)
app.addEntry("Extension of images to be deleted")
app.setEntryDefault("Extension of images to be deleted", "set extension of unsorted images")

app.addMessage("output", """This will be the output of the program""")
app.setMessageAspect("output", 600)

app.addButtons(["Delete!", "Move to trash folder","Help", "Exit"], press)
        
app.go()

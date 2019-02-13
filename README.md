# DelPy
DelPy picture sorter written in Python.

DelPy compares a reference directories contents to another directory and discards unneeded files. The list of filenames with a given extension in the reference directory is compared to the list of filenames with a given extension in the other directory and deletes all files that are not present in both from the second directory.

The intended use case is discarding raw image files in reference to sorted jpeg images when dealing with photography archives. When manually discarding the unneeded photos of one type, their counterpart can then be automatically deleted with this program.

Can be compiled with PyInstaller by running

  PyInstaller --onefile --windowed gui_del.py

or using onedir instead of onefile for faster startup.

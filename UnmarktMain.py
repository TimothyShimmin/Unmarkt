#! python3
# Unmarkt.py - Removes release group tags from digital comic books (cbr).
__author__ = 'Tim Shimmin'
# region imports
import ComicBook, os, sys
# import os, shutil, zipfile, sys
from enum import Enum
# import rarfile
# from librar import archive
# endregion

# region # initialize directory
testdir = os.path.dirname(os.path.realpath(__file__)) + '\\test\\'
print(testdir)
os.chdir(testdir)  # make it the active directory
# endregion

# region Comic filename
comic = 'spider-man.cbz'  # name of the comic
# comic = 'spider-man (2).cbz'  # without folder in archive ---name of the comic
# endregion

book = ComicBook.ComicBook(comic)
book.directory = testdir

book.findComicType()
book.findComicName()

book.extractZip()

book.writeToCbz()

book.cleanUp()

sys.exit()

# region # Rename zip to cbz     --- not sure how this works anymore but it might be useful for cbr
# if writeZip.filename.endswith('.zip'):
#     os.chdir(testdir)
#     print(writeZip.filename)
#     os.remove(writeZip.filename.replace('.zip', '.cbz'))
#     os.rename(writeZip.filename, writeZip.filename.replace('.zip', '.cbz'))
# endregion

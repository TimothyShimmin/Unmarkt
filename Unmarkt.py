#! python3
# Unmarkt.py - Removes ads from digital comic books (cbz, cbr).
__author__ = 'Tim Shimmin'
# region imports
import ComicBook, os, sys
# import os, shutil, zipfile, sys
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

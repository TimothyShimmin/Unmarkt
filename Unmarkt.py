#! python3
# Unmarkt.py - Removes release group tags from digital comic books (cbr).
__author__ = 'Tim Shimmin'

import os, shutil, zipfile, rarfile
from librar import archive
from enum import Enum

# archiveType = Enum('cbz', 'cbr')
class archiveType(Enum):
    cbz = 1
    cbr = 2

# initialize directory
testdir = 'D:\\Users\\Kat\\Documents\\GitHub\\Unmarkt\\test\\'
os.chdir(testdir)  # make it the active directory

# comic = 'spider-man.cbr'    # name of the comic
comic = 'spider-man (2).cbz'    # name of the comic
comicType = archiveType.cbz # assuming cbz until notified if CBR

if comic.endswith(".cbr"):
    comicType = archiveType.cbr

# region Extract from cbz
if comicType == archiveType.cbz:
    extractZip = zipfile.ZipFile(comic)     # set existing ZIP to this variable
    extractDirname = testdir + comic.replace('.cbz', '')
    print("Extracting ZIP here: " + extractDirname)
    extractZip.extractall(extractDirname)
    extractZip.close()
# endregion

# region Extract from cbr
if comicType == archiveType.cbr:
    extractRar = rarfile.RarFile(comic)     # set existing RAR to this variable
    extractDirname = testdir + comic.replace('.cbr', '')
    print("Extracting RAR here: " + extractDirname)
    extractRar.extractall(extractDirname)
    extractRar.close()
    comic = comic.replace('.cbr', '.cbz')
# endregion




# region Write to zip file
os.chdir(testdir)  # make it the active directory
if os.path.isfile('written ' + comic):
    os.remove('written ' + comic)

writeZip = zipfile.ZipFile('written ' + comic, 'a')      # 'a' for append to current
# print(os.getcwd())

# TODO: go down another level; only sees the comic folder's folder when writing, not the images in it. Recursive search?
os.chdir(extractDirname)                        # TODO: stay in parent folder? minimize switching folders?
filenames = [f for f in os.listdir('.') if os.path.isfile(f)]
print(filenames)
for filename in filenames:
    # TODO: Delete correct image
    print(filename)
    writeZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)
    # writeRar.write(filename, compress_type=zipfile.ZIP_DEFLATED)
    # writeRar.add_file(filename)     # TODO: confirm translation to librar.0.0.4 functions and arguments


writeZip.close()
# writeRar.run()
# endregion

# Delete extraction directory
os.chdir(testdir)
# print("Current working directory: " + os.getcwd())
shutil.rmtree(extractDirname)



# TODO: Use OOP ? Useful with batch?


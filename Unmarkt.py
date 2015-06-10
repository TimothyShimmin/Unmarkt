#! python3
# Unmarkt.py - Removes release group tags from digital comic books (cbr).
__author__ = 'Tim Shimmin'

import os, shutil, rarfile
from librar import archive

# initialize directory
testdir = 'D:\\Users\\Kat\\Documents\\GitHub\\Unmarkt\\test\\'
os.chdir(testdir)  # make it the active directory

comic = 'spider-man.cbr'    # name of the comic


# region Extract from cbr
extractRar = rarfile.RarFile(comic)     # set existing RAR to this variable
extractDir = testdir + comic.replace('.cbr', '')
print("Extracting here: " + extractDir)
extractRar.extractall(extractDir)
extractRar.close()
# endregion


# Write to zip file
# TODO: Write to cbr
os.chdir(testdir)  # make it the active directory
if os.path.isfile('written ' + comic):
    os.remove('written ' + comic)

# writeRar = archive.Archive('written ' + comic)      # create rar object to write to
# print(os.getcwd())
# writeRar = archive.Archive(os.getcwd() + '\\written ' + comic)      # create cbr object to write to
# writeRar = archive.Archive('D:\\Users\\Kat\\Documents\\GitHub\\Unmarkt\\test\\written test.rar')      # create rar object to write to

# base = "D:\\Users\\Kat\\Documents\\GitHub\\Unmarkt\\test"
# writeRar = archive.Archive("written test.rar", base)      # create rar object to write to
writeRar = archive.Archive("written test.rar", testdir)      # create rar object to write to




os.chdir(extractDir)                        # TODO: stay in parent folder? minimize switching folders?
filenames = [f for f in os.listdir('.') if os.path.isfile(f)]
print(filenames)
for filename in filenames:
    # TODO: Delete correct image
    print(filename)
    # writeRar.add_file(filename)     # TODO: confirm translation to librar.0.0.4 functions and arguments
writeRar.add_dir(extractDir)     # TODO: confirm translation to librar.0.0.4 functions and arguments


# writeZip.close()
writeRar.run()


# Delete extraction directory
os.chdir(testdir)
# print("Current working directory: " + os.getcwd())
shutil.rmtree(extractDir)



# TODO: Use OOP ?

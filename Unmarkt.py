#! python3
# Unmarkt.py - Removes release group tags from digital comic books (cbr).
__author__ = 'Tim Shimmin'
# region imports
import os, shutil, zipfile
from enum import Enum
# import rarfile
# from librar import archive
# endregion

class archiveType(Enum):
    cb7 = 1
    cbz = 2
    cbr = 3

# region # initialize directory
testdir = os.path.dirname(os.path.realpath(__file__)) + '\\test\\'
print(testdir)
os.chdir(testdir)  # make it the active directory
# endregion

# region Comic filename
comic = 'spider-man.cbz'  # name of the comic
# comic = 'spider-man (2).cbz'  # without folder in archive ---name of the comic
# endregion


# region# TODO: Extract from cbr, etc
if comic.endswith('.cb7'):
    comicType = archiveType.cb7
if comic.endswith('.cbz'):
    comicType = archiveType.cbz
if comic.endswith('.cbr'):
    comicType = archiveType.cbr
# endregion

# region # Extract from zip file
if not os.path.isfile(comic):           # exit if comic doesn't exist
    print('Comic <' + comic + '> does not exist')
    exit(126)                           # http://tldp.org/LDP/abs/html/exitcodes.html
# print(os.path.isfile(comic))
extractZip = zipfile.ZipFile(comic)     # set existing zip to this variable
# extractZip.namelist()                 # read list of file names

# print(testdir + os.sep + extractZip.filename)
# extractZip.extractall(testdir + '\\' + extractZip.filename)

# extractDir = testdir + 'this ' + str(1)
if comic.endswith('.zip'):
    extractDir = testdir + comic.replace('.zip', '')
if comic.endswith('.cbz'):
    extractDir = testdir + comic.replace('.cbz', '')
if comic.endswith('.cbr'):
    extractDir = testdir + comic.replace('.cbr', '')
# extractDir = testdir + comic      # TODO: change above to comic = comic.replace(...), use this instead
# extractDir = testdir + comic.find('.cb')
# print("Extracting here: " + extractDir)
extractZip.extractall(extractDir)

# extractZip.extractall()
extractZip.close()
# endregion





# Write to cbz      --- # Write to zip file
os.chdir(testdir)  # make it the active directory
# writeZip = zipfile.ZipFile(comic, 'w')    # 'w' for write (overwrite)
if os.path.isfile('written ' + comic):
    os.remove('written ' + comic)
writeZip = zipfile.ZipFile('written ' + comic, 'a')      # 'a' for append to current



# os.chdir(extractDir)
# writeZip.write(extractDir, compress_type=zipfile.ZIP_DEFLATED)    # saves directory folder structure, not the file(s) inside that directory

# for foldername, subfolders, filenames in os.walk(extractDir):
#     for filename in filenames:
#         writeZip.write(extractDir + '//' + filename, compress_type=zipfile.ZIP_DEFLATED)

# Remove correct image / write to new file without it
os.chdir(extractDir)
# directories = [d for d in os.walk('.') if os.path.isfile(d)]
# print(directories)
for root, dirs, files in os.walk('.'):
    print(dirs)
    if dirs:
        if dirs[0] != '':
            os.chdir(dirs[0])
            print(dirs[0])
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.find('zzz') == -1:
            writeZip.write(file, compress_type=zipfile.ZIP_DEFLATED)
            print(file)
    # print(files[1][0])
    # print(os.walk('.')[2][0])
    # if '.\\'.join(files[1]) == files[0]:        # files[1] is from first 'files' in os.walk, files[0] is from second 'files' in os.walk
        # take files[2] for new archive                  # files[2] is from second 'files' in os.walk
# filenames = [f for f in os.listdir('.') if os.path.isfile(f[2])]
# print(filenames)
# for filename in filenames:
#     if filename.find('zzz') == -1:
#         writeZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)
#         print(filename)
writeZip.close()

# region # Rename zip to cbz     --- not sure how this works anymore but it might be useful for cbr
# if writeZip.filename.endswith('.zip'):
#     os.chdir(testdir)
#     print(writeZip.filename)
#     os.remove(writeZip.filename.replace('.zip', '.cbz'))
#     os.rename(writeZip.filename, writeZip.filename.replace('.zip', '.cbz'))
# endregion

# region # Delete extraction directory
os.chdir(testdir)
shutil.rmtree(extractDir)
# print("Current working directory: " + os.getcwd())
# os.remove(extractDir)
# endregion




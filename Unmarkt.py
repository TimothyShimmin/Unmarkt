#! python3
# Unmarkt.py - Removes release group tags from digital comic books (cbr).
__author__ = 'Tim Shimmin'

import zipfile, os, shutil, rarfile

# TODO: Use OOP ?

# initialize directory
testdir = 'D:\\Users\\Kat\\Documents\\GitHub\\Unmarkt\\test\\'
os.chdir(testdir)  # make it the active directory

comic = 'spider-man.cbr'    # name of the comic
# # TODO: force CBR to rar
## if os.path.isfile(comic.replace('.cbr', '.rar')):
##     os.remove(comic.replace('.cbr', '.rar'))
# os.rename(comic, comic.replace('.cbr', '.rar'))
# comic = comic.replace('.cbr', '.rar')
# print(comic)


# region Extract from rar file
# TODO: Extract from cbr
# region ZIP attempt
## print(os.path.isfile(comic))
## if os.path.isfile(comic):             # checks if this comic exists
# extractZip = zipfile.ZipFile(comic)     # set existing zip to this variable
## extractZip.namelist()                 # read list of file names
# endregion

extractRar = rarfile.RarFile(comic)     # set existing RAR to this variable

# extractDirname = testdir + 'extraction folder ' + str(1)
extractDirname = testdir + comic.replace('.cbr', '')
print("Extracting here: " + extractDirname)
# extractZip.extractall(extractDirname)
extractRar.extractall(extractDirname)


# extractZip.close()
extractRar.close()
# endregion



# Write to zip file
# TODO: Write to cbr
os.chdir(testdir)  # make it the active directory
# writeZip = zipfile.ZipFile(comic, 'w')    # 'w' for write (overwrite)
if os.path.isfile('written ' + comic):
    os.remove('written ' + comic)
# writeZip = zipfile.ZipFile('written ' + comic, 'a')      # 'a' for append to current
writeRar = rarfile.RarFile('written ' + comic)      # create rar object to write to



os.chdir(extractDirname)                        # TODO: stay in parent folder?
filenames = [f for f in os.listdir('.') if os.path.isfile(f)]
print(filenames)
for filename in filenames:
    # TODO: Delete correct image
    print(filename)
    # writeZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)
    # writeRar.write(filename, compress_type=zipfile.ZIP_DEFLATED)      # TODO: translate to RarFile functions and arguments
# writeZip.close()
writeRar.close()

# Delete extraction directory
# os.chdir(testdir)
# print("Current working directory: " + os.getcwd())
# shutil.rmtree(extractDirname)





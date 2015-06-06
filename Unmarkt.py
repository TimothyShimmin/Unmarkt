#! python3
# Unmarkt.py - Removes release group tags from digital comic books (cbr).
__author__ = 'Tim Shimmin'

import zipfile, os, shutil

# TODO: Use OOP ?

# initialize directory
testdir = 'D:\\Users\\Kat\\Documents\\GitHub\\Unmarkt\\test\\'
os.chdir(testdir)  # make it the active directory

comic = 'example.zip'  # name of the comic


# Extract from zip file
# TODO: Extract from cbr
# print(os.path.isfile(comic))
# if os.path.isfile(comic):             # checks if this comic exists
extractZip = zipfile.ZipFile(comic)     # set existing zip to this variable
# extractZip.namelist()                 # read list of file names

# print(testdir + os.sep + extractZip.filename)
# extractZip.extractall(testdir + '\\' + extractZip.filename)

extractDirname = testdir + 'this ' + str(1)
print("Extracting here: " + extractDirname)
extractZip.extractall(extractDirname)

# extractZip.extractall()
extractZip.close()





# Write to zip file
# TODO: Write to cbr
os.chdir(testdir)  # make it the active directory
# writeZip = zipfile.ZipFile(comic, 'w')    # 'w' for write (overwrite)
if os.path.isfile('written ' + comic):
    os.remove('written ' + comic)
writeZip = zipfile.ZipFile('written ' + comic, 'a')      # 'a' for append to current


# for img in os.listdir(extractDirname):        # TODO: type check
#     writeZip.write(img, compress_type=zipfile.ZIP_DEFLATED)

# os.chdir(extractDirname)
# writeZip.write(extractDirname, compress_type=zipfile.ZIP_DEFLATED)    # saves directory folder structure, not the file(s) inside that directory

# for foldername, subfolders, filenames in os.walk(extractDirname):
#     for filename in filenames:
#         writeZip.write(extractDirname + '//' + filename, compress_type=zipfile.ZIP_DEFLATED)

os.chdir(extractDirname)                        # TODO: stay in parent folder?
filenames = [f for f in os.listdir('.') if os.path.isfile(f)]
print(filenames)
for filename in filenames:
    # TODO: Delete correct image
    print(filename)
    writeZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)
writeZip.close()

# Delete extraction directory
os.chdir(testdir)
# print("Current working directory: " + os.getcwd())
# os.remove(extractDirname)
shutil.rmtree(extractDirname)





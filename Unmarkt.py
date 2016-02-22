#! python3
# Unmarkt.py - Removes release group tags from digital comic books (cbr).
__author__ = 'Tim Shimmin'

import zipfile, os, shutil


# initialize directory
# testdir = 'D:\\Users\\Kat\\Documents\\GitHub\\Unmarkt\\test\\'
testdir = 'C:\\Users\\Tim.Shimmin\\Documents\\GitHub\\Unmarkt\\test\\'
comic = 'spider-man.zip'  # name of the comic

# testdir = 'C:\\Users\\Tim.Shimmin\\Documents\\GitHub\\Unmarkt\\test2\\'
# comic = 'spider-man.cbz'  # name of the comic

os.chdir(testdir)  # make it the active directory


# Extract from zip file
# TODO: Extract from cbr
# print(os.path.isfile(comic))
# if os.path.isfile(comic):             # checks if this comic exists
extractZip = zipfile.ZipFile(comic)     # set existing zip to this variable
# extractZip.namelist()                 # read list of file names

# print(testdir + os.sep + extractZip.filename)
# extractZip.extractall(testdir + '\\' + extractZip.filename)

# extractDir = testdir + 'this ' + str(1)
extractDir = testdir + comic.replace('.zip', '')
print("Extracting here: " + extractDir)
extractZip.extractall(extractDir)

# extractZip.extractall()
extractZip.close()





# Write to zip file
# TODO: Write to cbz
os.chdir(testdir)  # make it the active directory
# writeZip = zipfile.ZipFile(comic, 'w')    # 'w' for write (overwrite)
if os.path.isfile('written ' + comic):
    os.remove('written ' + comic)
writeZip = zipfile.ZipFile('written ' + comic, 'a')      # 'a' for append to current


# for img in os.listdir(extractDir):        # TODO: type check
#     writeZip.write(img, compress_type=zipfile.ZIP_DEFLATED)

# os.chdir(extractDir)
# writeZip.write(extractDir, compress_type=zipfile.ZIP_DEFLATED)    # saves directory folder structure, not the file(s) inside that directory

# for foldername, subfolders, filenames in os.walk(extractDir):
#     for filename in filenames:
#         writeZip.write(extractDir + '//' + filename, compress_type=zipfile.ZIP_DEFLATED)

os.chdir(extractDir)                        # TODO: stay in parent folder?
filenames = [f for f in os.listdir('.') if os.path.isfile(f)]
print(filenames)
for filename in filenames:
    # TODO: Delete correct image
    # print(filename)
    if filename != '4.bmp':
    # if filename.parse('4') != '':
        writeZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)
        print(filename)
writeZip.close()

# Rename zip to cbz
os.chdir(testdir)
print(writeZip.filename)
# open(writeZip.filename)
# print(shutil.move(writeZip.filename, writeZip.filename.replace('.zip', '.cbz')))
os.remove(writeZip.filename.replace('.zip', '.cbz'))
os.rename(writeZip.filename, writeZip.filename.replace('.zip', '.cbz'))


# writeZip.close()



# Delete extraction directory
os.chdir(testdir)
# print("Current working directory: " + os.getcwd())
# os.remove(extractDir)
shutil.rmtree(extractDir)





import os, shutil, zipfile
from enum import Enum


class archiveType(Enum):
    unk = 0
    cbr = 1
    cbz = 2
    cb7 = 3


class ComicBook:
    'Type for comic books in Unmarkt'
    def __init__(self, filename):
        self.directory = ''     # os.getcwd()??
        self.fileName = filename
        self.comicName = ''
        self.comicType = archiveType.unk
        self.extractDir = ''

    def getDirectory(self):
        return self.directory

    def getFileName(self):
        return self.fileName

    def getComicName(self):
        return self.comicName

    def getComicType(self):
        return self.comicType

    def getExtractDir(self):
        return self.extractDir

    def comicIsValid(self):
        if not os.path.isfile(self.getFileName()):           # exit if comic doesn't exist
            print('Comic <' + self.getFileName() + '> does not exist')
            exit(126)                           # http://tldp.org/LDP/abs/html/exitcodes.html
            return False
        return True

    # TODO: merge findComicType and findComicName?
    def findComicType(self):
        if self.fileName.endswith('.cbz'):
            self.comicType = archiveType.cbz
        elif self.fileName.endswith('.cbr'):
            self.comicType = archiveType.cbr
        elif self.fileName.endswith('.cb7'):
            self.comicType = archiveType.cb7
        else:
            self.comicType = archiveType.unk
        return self.comicType

    def findComicName(self):
        if self.fileName.endswith('.zip'):
            self.comicName = self.fileName.replace('.zip', '')
        elif self.fileName.endswith('.cbz'):
            self.comicName = self.fileName.replace('.cbz', '')
        elif self.fileName.endswith('.cbr'):
            self.comicName = self.fileName.replace('.cbr', '')
        else:
            self.comicName = 'Comic Name err'
        return self.comicName

    def extractZip(self):       # def openArchive()?
        # if not os.path.isfile(self.getFileName()):           # exit if comic doesn't exist
        #     print('Comic <' + self.getFileName() + '> does not exist')
        #     exit(126)                           # http://tldp.org/LDP/abs/html/exitcodes.html
        # if self.getComicType() == archiveType.cbz:
        extractArchive = zipfile.ZipFile(self.getFileName())     # set existing zip to this variable
        self.extractDir = self.getDirectory() + self.getComicName()
        # print("Extracting here: " + extractDir)
        extractArchive.extractall(self.extractDir)

        # extractArchive.extractall()
        extractArchive.close()
        return self.extractDir       # TODO: Throwing around directories probably isn't the way to go

    def writeToCbz(self):
        os.chdir(self.getDirectory())  # make it the active directory       # TODO: might not need this if use os.walk?
        # writeZip = zipfile.ZipFile(comic, 'w')    # 'w' for write (overwrite)
        if os.path.isfile('written ' + self.getComicName()):
            os.remove('written ' + self.getComicName())
        writeZip = zipfile.ZipFile('written ' + self.getComicName(), 'a')      # 'a' for append to current
        # return writeZip
    # writeZip = writeToCbz()



    # os.chdir(extractDir)
    # writeZip.write(extractDir, compress_type=zipfile.ZIP_DEFLATED)    # saves directory folder structure, not the file(s) inside that directory

    # for foldername, subfolders, filenames in os.walk(extractDir):
    #     for filename in filenames:
    #         writeZip.write(extractDir + '//' + filename, compress_type=zipfile.ZIP_DEFLATED)

    # Remove correct image / write to new file without it
    # def writeZip():
        os.chdir(self.getExtractDir())
    # directories = [d for d in os.walk('.') if os.path.isfile(d)]
    # print(directories)
        for root, dirs, files in os.walk('.'):
            print(dirs)
            if dirs:
                if dirs[0] != '':
                    os.chdir(dirs[0])
                    print(dirs[0])
                    break
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
        return

    def cleanUp(self):
        os.chdir(self.getDirectory())
        shutil.rmtree(self.getExtractDir())
        return

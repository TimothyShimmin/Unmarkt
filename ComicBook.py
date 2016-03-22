import os, shutil, zipfile
from enum import Enum


class archiveType(Enum):
    unk = 0
    cbz = 1
    cbr = 2
    cb7 = 3


class ComicBook:
    """Type for comic books in Unmarkt"""
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
            print('archiveType unknown')
            exit(126)
        return self.comicType

    def findComicName(self):
        if self.getComicType() == archiveType.cbz:
            self.comicName = self.fileName.replace('.cbz', '')
        elif self.getComicType() == archiveType.cbr:
            self.comicName = self.fileName.replace('.cbr', '')
        elif self.getComicType() == archiveType.cb7:
            self.comicName = self.fileName.replace('.cb7', '')
        else:
            print('Comic Name err')
            exit(126)
        return self.comicName

    def extractZip(self):       # def openArchive()?
        if not os.path.isfile(self.getFileName()):           # exit if comic doesn't exist
            print('Comic <' + self.getFileName() + '> does not exist')
            exit(126)                           # http://tldp.org/LDP/abs/html/exitcodes.html
        if self.getComicType() == archiveType.cbz:
            extractArchive = zipfile.ZipFile(self.getFileName())     # set existing zip to this variable
            self.extractDir = self.getDirectory() + self.getComicName()
            # print("Extracting here: " + extractDir)
            extractArchive.extractall(self.extractDir)

            extractArchive.close()
            return self.extractDir       # TODO: Throwing around directories probably isn't the way to go
        else:
            print('Comic Type not supported')
            exit(126)


    def writeToCbz(self):   #TODO: add parameter for custom filter. list of strings?
        os.chdir(self.getDirectory())  # make it the active directory       # TODO: might not need this if use os.walk?

        if os.path.isfile('written ' + self.getFileName()):
            os.remove('written ' + self.getFileName())
        writeZip = zipfile.ZipFile('written ' + self.getFileName(), 'a')      # 'a' for append to current

        os.chdir(self.getExtractDir())
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
        writeZip.close()
        return

    def cleanUp(self):
        os.chdir(self.getDirectory())
        shutil.rmtree(self.getExtractDir())
        return

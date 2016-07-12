import os
import time


class FileParser:
    def __init__(self, file):
        if os.path.isfile(file):
            self.file = open(file, "r");
            self.file_path = file;
            if not self.file:
                raise Exception("Unable to open file %s" % file)
        else:
            raise Exception("%s is not a file " % file)


    def watch (self, callback=None):
        last_size = 0
        last_position = 0
        while True:
            if last_size != self.getFileSize():
                last_size = self.getFileSize()
                linenumber = 0;
                self.file.seek(last_position, 0)
                for line in self.file.readlines():
                    if linenumber > last_position:
                        last_position = linenumber
                        if callback is None:
                                self.defaultCallback(line)
                    linenumber+=1
            else:
                time.sleep(1)


    def getFileSize(self):
        return os.path.getsize(self.file_path);

    def defaultCallback(self, text):
        print text.strip()


#log1 = FileParser("~/test.txt");
#print log1.getFileSize()
#log1.watch()

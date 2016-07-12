import re
import os

LOCK_FILE = "/var/lock/test.lock";

def isNum(str):
        if re.match("[^0-9]", str):
                return False
        return True

def lockExists():
        if not os.path.isfile(LOCK_FILE):
                return None

        with open(LOCK_FILE, "r") as lf:
                return int(lf.read())
        return None

def createLock():
        if lockExists():
                return None;
        with open(LOCK_FILE, "w") as lf:
                lf.write(getPid())
                return True
        return False

def getPid():
        return str(os.getpid());

def removeLock():
        if lockExists():
                os.unlink(LOCK_FILE)
                return True
        return False


'''
if not lockExists():
        print "Crete lock"
        createLock();
else:
        print "Lock exists ";
        removeLock();
'''

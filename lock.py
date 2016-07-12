import re
import os
import sys

LOCK_FILE = "/var/lock/test.lock";

def isNum(s):
        if re.match("[^0-9]", str(s)):
                return False
        return True

def lockExists():
        if not os.path.isfile(LOCK_FILE):
                return None

        with open(LOCK_FILE, "r") as lf:
                return str(lf.read())
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


def argv(num, default=None):
        if len(sys.argv) > num:
                return sys.argv[num]
        return default


def run():
        if lockExists():
                print "Already started PID %s " % lockExists()
                return None;

        createLock()

        return None;

def help(prog):
        print "Use %s start <port>  - to start " % prog
        print "Use %s stop          - to stop" % prog
        print "Use %s status        - to get status" % prog
        print "Use %s help          - for this message" % prog

def stop():
        lock = lockExists();
        if lock:
                removeLock()
                print "Trying to stop PID %s" % lock
                os.kill(int(lock), 9)
                print "Done."
        return None

def status():
        lock = lockExists()
        if lock:
                print "Runing under PID %s" % lock
        else:
                print "Not running"
        return None

if argv(1) == "start" and isNum(argv(2, default=False)):
        run()
elif argv(1) == "stop":
        stop()
elif argv(1) == "status":
        status()
else:
        help(argv(0))

quit();

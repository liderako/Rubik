import sys

def readFile(nameFile):
    try:
        f = open(nameFile, 'r')
        res = f.read()
        return res
    except:
        print ("Read file error.")
        sys.exit(1)
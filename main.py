import sys
from src.readFile import *
from src.object.managers.ValidationManager import *

if (len(sys.argv) != 2):
    print "Usage: main.py filename"
    sys.exit(1)
readBuffer = readFile(sys.argv[1])
validationManager = ValidationManager(readBuffer)

validationManager.run()
# print validationManager.readBuffer
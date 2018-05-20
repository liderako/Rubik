import sys
from src.readFile import *
from src.errorExit import *
from src.object.managers.ValidationManager import ValidationManager
from src.object.managers.MixManager import MixManager
from src.object.Cubik import Cubik
from src.object.CheckerColors import CheckerColors

if (len(sys.argv) != 3):
    print ("Usage: main.py [-i or -f] [count i or fileName]")
    sys.exit(1)
if (sys.argv[1] == "-f"):
    readBuffer = readFile(sys.argv[2])
    validationManager = ValidationManager(readBuffer)
    validationManager.run()
mixManager = MixManager()
moveList = list()
if (sys.argv[1] == "-i"):
    try:
        i = int(sys.argv[2])
        if (i <= 0):
            sys.exit(-1)
        moveList = mixManager.generateRandomMove(int(sys.argv[2]))
        print (moveList)
    except:
        errorExit("Invalid digital count")
else:
    moveList = readBuffer.split(" ")
cub = Cubik(3)
mixManager.mixRun(moveList, cub)
cub.printCubik()

checkerColors = CheckerColors()
#print (checkerColors.two(cub, 'yellow', 'blue'))
print (checkerColors.three(cub, 'red', 'blue', 'white'))


#colors = ["green", "blue", "red", "orange", "white", "yellow"]



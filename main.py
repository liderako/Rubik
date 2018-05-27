import sys
from src.readFile import *
from src.errorExit import *
from src.object.managers.ValidationManager import ValidationManager
from src.object.managers.MixManager import MixManager
from src.object.Cubik import Cubik
from src.object.CheckerColors import CheckerColors
from src.object.algorithm.Algorithm import *

stringUsage = "Usage: main.py [-i or -f] [count i or fileName]"
if (len(sys.argv) != 3):
    errorExit(stringUsage)
elif (sys.argv[1] != "-f" and sys.argv[1] != "-i"):
    errorExit(stringUsage)

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
    except:
        errorExit("Invalid digital count")
else:
    moveList = readBuffer.split(" ")
cub = Cubik(3)
mixManager.mixRun(moveList, cub)

print ("MixMoveList")
for x in moveList:
    print (x, end=" ")
cub.printCubik()

print ("Start Algorithm")
algorithm = Algorithm(cub)
algorithm.run()


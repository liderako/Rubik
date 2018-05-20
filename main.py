import sys
from src.readFile import *
from src.errorExit import *
from src.object.managers.ValidationManager import ValidationManager
from src.object.managers.MixManager import MixManager
from src.object.cubik import Cubik

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
    except:
        errorExit("Invalid digital count")
else:
    moveList = readBuffer.split(" ")
cub = Cubik(3)
origin = Cubik(3)
# print (cub.hash)
mixManager.mixRun(moveList, cub)
cub.printCubik()
# cub.mathHash()
# print (cub.hash)

while (1):
    cub.mathHash()
    if (origin.hash == cub.hash):
        break ;
    cub.moveDoubleB()
    cub.moveDoubleD()
    cub.moveBackF()
    cub.moveDoubleR()
    cub.moveF()
    cub.moveDoubleU()
    cub.moveDoubleR()
    cub.moveBackF()
    cub.moveDoubleR()
    cub.moveDoubleU()
    cub.moveF()
    cub.moveR()
    cub.moveU()
    cub.moveL()
    cub.moveB()
    cub.moveD()
    cub.moveBackR()
    cub.moveD()
    cub.moveDoubleL()
    cub.moveBackU()
    cub.printCubikText()
    # cub.printCubik()
# # print (moveList)
# cub.printCubik()
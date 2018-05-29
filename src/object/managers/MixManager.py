import sys
import random
from src.errorExit import errorExit
from src.object.Cubik import *

class MixManager:

    def __init__(self):
        self.maxCount = 500
        self.listAvailableCommand = ["F", "D", "B", "R", "L", "U", "F2", "D2", "B2", "R2", "L2", "U2", "F'", "B'", "R'", "L'", "U'", "D'"]

    def generateRandomMove(self, countMove):
        if (countMove > self.maxCount):
            errorExit("Too big i, max number is 500")
        listMove = list()
        size = len(self.listAvailableCommand) - 1
        while countMove > 0:
            countMove -= 1
            n = random.randint(0, size)
            listMove.append(self.listAvailableCommand[n])
        return listMove

    def mixRun(self, listMove, cub):
        for elem in listMove:
            if (elem == "F"):
                cub.moveF()
            elif (elem == "B"):
                cub.moveB()
            elif (elem == "R"):
                cub.moveR()
            elif (elem == "L"):
                cub.moveL()
            elif (elem == "U"):
                cub.moveU()
            elif (elem == "D"):
                cub.moveD()
            elif (elem == "F2"):
                cub.moveDoubleF()
            elif (elem == "B2"):
                cub.moveDoubleB()
            elif (elem == "R2"):
                cub.moveDoubleR()
            elif (elem == "L2"):
                cub.moveDoubleL()
            elif (elem == "U2"):
                cub.moveDoubleU()
            elif (elem == "D2"):
                cub.moveDoubleD()
            elif (elem == "F'"):
                cub.moveBackF()
            elif (elem == "B'"):
                cub.moveBackB()
            elif (elem == "R'"):
                cub.moveBackR()
            elif (elem == "L'"):
                cub.moveBackL()
            elif (elem == "U'"):
                cub.moveBackU()
            elif (elem == "D'"):
                cub.moveBackD()
        return (cub)

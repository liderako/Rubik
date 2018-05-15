import sys
import random

class MixManager:

    def __init__(self):
        # F B R L U F2 B2 R2 L2 U2 F' B' R' L' U'
        self.listAvailableCommand = ["F", "B", "R", "L", "U", "F2", "B2", "R2", "L2", "U2", "F'", "B'", "R'", "L'", "U'"]

    def generateRandomMove(self, countMove):
        listMove = list()
        size = len(self.listAvailableCommand) - 1
        while countMove > 0:
            countMove -= 1
            n = random.randint(0, size)
            listMove.append(self.listAvailableCommand[n])
        return listMove


    def mixRun(self, listMove):
        pass
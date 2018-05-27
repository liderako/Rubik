import sys
from src.object.Cubik import *

def printSolution(cub, moveList, flag):
    cost = 0
    for i, move in enumerate(moveList):
        if move == 'U':
            cub.moveU()
            cost += 1
        elif move == 'D':
            cub.moveD()
            cost += 1
        elif move == 'R':
            cub.moveR()
            cost += 1
        elif move == 'L':
            cub.moveL()
            cost += 1
        elif move == 'F':
            cub.moveF()
            cost += 1
        elif move == 'B':
            cub.moveB()
            cost += 1

        elif move == "U'":
            cub.moveBackU()
            cost += 1
        elif move == "D'":
            cub.moveBackD()
            cost += 1
        elif move == "R'":
            cub.moveBackR()
            cost += 1
        elif move == "L'":
            cub.moveBackL()
            cost += 1
        elif move == "F'":
            cub.moveBackF()
            cost += 1
        elif move == "B'":
            cub.moveBackB()
            cost += 1
#
        elif move == 'U2':
            cub.moveDoubleU()
            cost += 1
        elif move == 'D2':
            cub.moveDoubleD()
            cost += 1
        elif move == 'R2':
            cub.moveDoubleR()
            cost += 1
        elif move == 'L2':
            cub.moveDoubleL()
            cost += 1
        elif move == 'F2':
            cub.moveDoubleF()
            cost += 1
        elif move == 'B2':
            cub.moveDoubleB()
            cost += 1

        print ("Move number ", i, "move ", move)
        if (flag == "-g"):
            cub.printCubik()
        else:
            cub.printCubikText()
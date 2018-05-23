import sys
from Cubik import *



#U D R L F B

def printSolution(cub, moveList):
    for i, move in enumerate(moveList):
        if move == 'U':
            cub.moveU()
        elif move == 'D':
            cub.moveD()
        elif move == 'R':
            cub.moveR()
        elif move == 'L':
            cub.moveL()
        elif move == 'F':
            cub.moveF()
        elif move == 'B':
            cub.moveB()
#
        elif move == 'U':
            cub.moveBackU()
        elif move == 'D':
            cub.moveBackD()
        elif move == 'R':
            cub.moveBackR()
        elif move == 'L':
            cub.moveBackL()
        elif move == 'F':
            cub.moveBackF()
        elif move == 'B':
            cub.moveBackB()
#
        elif move == 'U2':
            cub.moveDoubleU()
        elif move == 'D2':
            cub.moveDoubleD()
        elif move == 'R2':
            cub.moveDoubleR()
        elif move == 'L2':
            cub.moveDoubleL()
        elif move == 'F2':
            cub.moveDoubleF()
        elif move == 'B2':
            cub.moveDoubleB()

        print ("Move number ", i, "move ", move)
        cub.printCubik()

cub = Cubik(3)
moveList = ["L", "U", "B", "D'"]

printSolution(cub, moveList)

#cub.printCubik()

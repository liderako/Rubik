import sys
from Cubik import *

class CheckerColors:
    def two(self, cub, color1, color2):
        if (cub.Upper[0][1] == color1 and cub.Back[0][1] == color2):
            return ([['Upper', color1, 0, 1],['Back', color2, 0, 1]])
        elif (cub.Upper[0][1] == color2 and cub.Back[0][1] == color1):
            return ([['Upper', color2, 0, 1],['Back', color1, 0, 1]])
        elif (cub.Upper[1][2] == color1 and cub.Right[1][0] == color2):
            return ([['Upper', color1, 1, 2],['Right', color2, 1, 0]])
        elif (cub.Upper[1][2] == color2 and cub.Right[1][0] == color1):
            return ([['Upper', color2, 1, 2],['Right', color1, 1, 0]])
        elif (cub.Upper[2][1] == color1 and cub.Front[0][1] == color2):
            return ([['Upper', color1, 2, 1],['Front', color2, 0, 1]])
        elif (cub.Upper[2][1] == color2 and cub.Front[0][1] == color1):
            return ([['Upper', color2, 2, 1],['Front', color1, 0, 1]])
        elif (cub.Upper[1][0] == color1 and cub.Left[0][1] == color2):
            return ([['Upper', color1, 2, 1],['Left', color2, 0, 1]])
        elif (cub.Upper[1][0] == color2 and cub.Left[0][1] == color1):
            return ([['Upper', color2, 2, 1],['Left', color1, 0, 1]])
        elif (cub.Left[2][1] == color1 and cub.Front[0][1] == color2):
            return ([['Left', color1, 2, 1],['Front', color2, 0, 1]])
        elif (cub.Left[2][1] == color2 and cub.Front[0][1] == color1):
            return ([['Left', color2, 2, 1],['Front', color1, 0, 1]])
        elif (cub.Left[0][1] == color1 and cub.Back[2][1] == color2):
            return ([['Left', color1, 0, 1],['Back', color2, 2, 1]])
        elif (cub.Left[0][1] == color2 and cub.Back[2][1] == color1):
            return ([['Left', color2, 0, 1],['Back', color1, 2, 1]])
        elif (cub.Front[2][1] == color1 and cub.Right[0][1] == color2):
            return ([['Front', color1, 2, 1],['Right', color2, 0, 1]])
        elif (cub.Front[2][1] == color2 and cub.Right[0][1] == color1):
            return ([['Front', color2, 2, 1],['Right', color1, 0, 1]])
        elif (cub.Right[2][1] == color1 and cub.Back[0][1] == color2):
            return ([['Right', color1, 2, 1],['Back', color2, 0, 1]])
        elif (cub.Right[2][1] == color2 and cub.Back[0][1] == color1):
            return ([['Right', color2, 2, 1],['Back', color1, 0, 1]])
        elif (cub.Down[0][1] == color1 and cub.Front[2][1] == color2):
            return ([['Down', color1, 0, 1],['Front', color2, 2, 1]])
        elif (cub.Down[0][1] == color2 and cub.Front[2][1] == color1):
            return ([['Down', color2, 0, 1],['Front', color1, 2, 1]])
        elif (cub.Down[1][2] == color1 and cub.Right[2][1] == color2):
            return ([['Down', color1, 2, 1],['Right', color2, 2, 1]])
        elif (cub.Down[1][2] == color1 and cub.Right[2][1] == color2):
            return ([['Down', color1, 2, 1],['Right', color2, 2, 1]])
        elif (cub.Down[2][1] == color1 and cub.Back[2][1] == color2):
            return ([['Down', color1, 2, 1],['Back', color2, 2, 1]])
        elif (cub.Down[2][1] == color2 and cub.Back[2][1] == color1):
            return ([['Down', color2, 2, 1],['Back', color1, 2, 1]])
        elif (cub.Down[1][0] == color1 and cub.Left[2][1] == color2):
            return ([['Down', color1, 1, 0],['Left', color2, 2, 1]])
        elif (cub.Down[1][0] == color2 and cub.Left[2][1] == color1):
            return ([['Down', color2, 1, 0],['Left', color1, 2, 1]])
    def three(self, cub, color1, color2, color3):
#
        if (cub.Upper[0][0] == color1 and cub.Left[0][0] == color2 and cub.Back[0][2] == color3):
            return ([['Upper', color1, 0, 0],['Left', color2, 0, 0]], ['Back', color3, 0, 2])
        elif (cub.Upper[0][0] == color2 and cub.Left[0][0] == color3 and cub.Back[0][2] == color1):
            return ([['Upper', color2, 0, 0],['Left', color3, 0, 0]], ['Back', color1, 0, 2])
        elif (cub.Upper[0][0] == color3 and cub.Left[0][0] == color1 and cub.Back[0][2] == color2):
            return ([['Upper', color3, 0, 0],['Left', color1, 0, 0]], ['Back', color2, 0, 2])
#
        elif (cub.Upper[0][2] == color1 and cub.Right[0][2] == color2 and cub.Back[0][0] == color3):
            return ([['Upper', color1, 0, 2],['Right', color2, 0, 2]], ['Back', color3, 0, 0])
        elif (cub.Upper[0][2] == color2 and cub.Right[0][2] == color3 and cub.Back[0][0] == color1):
            return ([['Upper', color2, 0, 2],['Right', color3, 0, 2]], ['Back', color1, 0, 0])
        elif (cub.Upper[0][2] == color3 and cub.Right[0][2] == color1 and cub.Back[0][0] == color2):
            return ([['Upper', color3, 0, 2],['Right', color1, 0, 2]], ['Back', color2, 0, 0])
#
        elif (cub.Upper[2][2] == color1 and cub.Right[0][0] == color2 and cub.Front[0][2] == color3):
            return ([['Upper', color1, 2, 2],['Right', color2, 0, 0]], ['Front', color3, 0, 2])
        elif (cub.Upper[2][2] == color2 and cub.Right[0][0] == color3 and cub.Front[0][2] == color1):
            return ([['Upper', color2, 2, 2],['Right', color3, 0, 0]], ['Front', color1, 0, 2])
        elif (cub.Upper[2][2] == color3 and cub.Right[0][0] == color1 and cub.Front[0][2] == color2):
            return ([['Upper', color3, 2, 2],['Right', color1, 0, 0]], ['Front', color2, 0, 2])
#
        elif (cub.Upper[2][0] == color1 and cub.Left[0][2] == color2 and cub.Front[0][0] == color3):
            return ([['Upper', color1, 2, 0],['Left', color2, 0, 2]], ['Front', color3, 0, 0])
        elif (cub.Upper[2][0] == color2 and cub.Left[0][2] == color3 and cub.Front[0][0] == color1):
            return ([['Upper', color2, 2, 0],['Left', color3, 0, 2]], ['Front', color1, 0, 0])
        elif (cub.Upper[2][0] == color3 and cub.Left[0][2] == color1 and cub.Front[0][0] == color2):
            return ([['Upper', color3, 2, 0],['Left', color1, 0, 2]], ['Front', color2, 0, 0])
#
        elif (cub.Down[0][0] == color1 and cub.Left[2][2] == color2 and cub.Front[0][2] == color3):
            return ([['Down', color1, 0, 0],['Left', color2, 2, 2]], ['Front', color3, 0, 2])
        elif (cub.Down[0][0] == color2 and cub.Left[2][2] == color3 and cub.Front[0][2] == color1):
            return ([['Down', color2, 0, 0],['Left', color3, 2, 2]], ['Front', color1, 0, 2])
        elif (cub.Down[0][0] == color3 and cub.Left[2][2] == color1 and cub.Front[0][2] == color2):
            return ([['Down', color3, 0, 0],['Left', color1, 2, 2]], ['Front', color2, 0, 2])
#
        elif (cub.Down[0][2] == color1 and cub.Right[2][0] == color2 and cub.Front[2][2] == color3):
            return ([['Down', color1, 0, 2],['Right', color2, 2, 0]], ['Front', color3, 2, 2])
        elif (cub.Down[0][2] == color2 and cub.Right[2][0] == color3 and cub.Front[2][2] == color1):
            return ([['Down', color2, 0, 2],['Right', color3, 2, 0]], ['Front', color1, 2, 2])
        elif (cub.Down[0][2] == color3 and cub.Right[2][0] == color1 and cub.Front[2][2] == color2):
            return ([['Down', color3, 0, 2],['Right', color1, 2, 0]], ['Front', color2, 2, 2])
#
        elif (cub.Down[2][2] == color1 and cub.Right[2][2] == color2 and cub.Back[2][0] == color3):
            return ([['Down', color1, 2, 2],['Right', color2, 2, 2]], ['Back', color3, 2, 0])
        elif (cub.Down[2][2] == color2 and cub.Right[2][2] == color3 and cub.Back[2][0] == color1):
            return ([['Down', color2, 2, 2],['Right', color3, 2, 2]], ['Back', color1, 2, 0])
        elif (cub.Down[2][2] == color3 and cub.Right[2][2] == color1 and cub.Back[2][0] == color2):
            return ([['Down', color3, 2, 2],['Right', color1, 2, 2]], ['Back', color2, 2, 0])
#
        elif (cub.Down[2][0] == color1 and cub.Left[2][0] == color2 and cub.Back[2][2] == color3):
            return ([['Down', color1, 2, 2],['Left', color2, 2, 0]], ['Back', color3, 2, 2])
        elif (cub.Down[2][0] == color2 and cub.Left[2][0] == color3 and cub.Back[2][2] == color1):
            return ([['Down', color2, 2, 2],['Left', color3, 2, 0]], ['Back', color1, 2, 2])
        elif (cub.Down[2][0] == color3 and cub.Left[2][0] == color1 and cub.Back[2][2] == color2):
            return ([['Down', color3, 2, 2],['Left', color1, 2, 0]], ['Back', color2, 2, 2])


cub = Cubik(3)


cub.printCubik()

checkerColors = CheckerColors()

print (checkerColors.three(cub, 'white', 'blue', 'red'))
cub.printCubik()

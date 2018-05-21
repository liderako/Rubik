import sys
from src.object.Cubik import Cubik

class CheckerColors:

    def two(self, cub, color1, color2):
        if (cub.upper[0][1] == color1 and cub.back[0][1] == color2):
            return ([['upper', color1, 0, 1],['back', color2, 0, 1]])
        elif (cub.upper[0][1] == color2 and cub.back[0][1] == color1):
            return ([['upper', color2, 0, 1],['back', color1, 0, 1]])
#
        elif (cub.upper[1][2] == color1 and cub.right[0][1] == color2):
            return ([['upper', color1, 1, 2],['right', color2, 0, 1]])
        elif (cub.upper[1][2] == color2 and cub.right[0][1] == color1):
            return ([['upper', color2, 1, 2],['right', color1, 0, 1]])
#
        elif (cub.upper[2][1] == color1 and cub.front[0][1] == color2):
            return ([['upper', color1, 2, 1],['front', color2, 0, 1]])
        elif (cub.upper[2][1] == color2 and cub.front[0][1] == color1):
            return ([['upper', color2, 2, 1],['front', color1, 0, 1]])
#
        elif (cub.upper[1][0] == color1 and cub.left[0][1] == color2):
            return ([['upper', color1, 1, 0],['left', color2, 0, 1]])
        elif (cub.upper[1][0] == color2 and cub.left[0][1] == color1):
            return ([['upper', color2, 1, 0],['left', color1, 0, 1]])
#
        elif (cub.left[1][2] == color1 and cub.front[1][0] == color2):
            return ([['left', color1, 1, 2],['front', color2, 1, 0]])
        elif (cub.left[1][2] == color2 and cub.front[1][0] == color1):
            return ([['left', color2, 1, 2],['front', color1, 1, 0]])
#
        elif (cub.left[1][0] == color1 and cub.back[1][2] == color2):
            return ([['left', color1, 1, 0],['back', color2, 1, 2]])
        elif (cub.left[1][0] == color2 and cub.back[1][2] == color1):
            return ([['left', color2, 1, 0],['back', color1, 1, 2]])
#
        elif (cub.front[1][2] == color1 and cub.right[0][1] == color2):
            return ([['front', color1, 1, 2],['right', color2, 0, 1]])
        elif (cub.front[1][2] == color2 and cub.right[0][1] == color1):
            return ([['front', color2, 1, 2],['right', color1, 0, 1]])
#
        elif (cub.right[1][2] == color1 and cub.back[1][0] == color2):
            return ([['right', color1, 1, 2],['back', color2, 1, 0]])
        elif (cub.right[1][2] == color2 and cub.back[1][0] == color1):
            return ([['right', color2, 1, 2],['back', color1, 1, 0]])
#
        elif (cub.down[0][1] == color1 and cub.front[2][1] == color2):
            return ([['down', color1, 0, 1],['front', color2, 2, 1]])
        elif (cub.down[0][1] == color2 and cub.front[2][1] == color1):
            return ([['down', color2, 0, 1],['front', color1, 2, 1]])
#
        elif (cub.down[1][2] == color1 and cub.right[2][1] == color2):
            return ([['down', color1, 1, 2],['right', color2, 2, 1]])
        elif (cub.down[1][2] == color1 and cub.right[2][1] == color2):
            return ([['down', color1, 1, 2],['right', color2, 2, 1]])
#
        elif (cub.down[2][1] == color1 and cub.back[2][1] == color2):
            return ([['down', color1, 2, 1],['back', color2, 2, 1]])
        elif (cub.down[2][1] == color2 and cub.back[2][1] == color1):
            return ([['down', color2, 2, 1],['back', color1, 2, 1]])
#
        elif (cub.down[1][0] == color1 and cub.left[2][1] == color2):
            return ([['down', color1, 1, 0],['left', color2, 2, 1]])
        elif (cub.down[1][0] == color2 and cub.left[2][1] == color1):
            return ([['down', color2, 1, 0],['left', color1, 2, 1]])
        return (False)

    def three(self, cub, color1, color2, color3):
        if (cub.upper[0][0] == color1 and cub.left[0][0] == color2 and cub.back[0][2] == color3):
            return ([['upper', color1, 0, 0],['left', color2, 0, 0]], ['back', color3, 0, 2])
        elif (cub.upper[0][0] == color1 and cub.left[0][0] == color3 and cub.back[0][2] == color2):
            return ([['upper', color1, 0, 0],['left', color3, 0, 0]], ['back', color2, 0, 2])
        elif (cub.upper[0][0] == color2 and cub.left[0][0] == color3 and cub.back[0][2] == color1):
            return ([['upper', color2, 0, 0],['left', color3, 0, 0]], ['back', color1, 0, 2])
        elif (cub.upper[0][0] == color2 and cub.left[0][0] == color1 and cub.back[0][2] == color3):
            return ([['upper', color2, 0, 0],['left', color1, 0, 0]], ['back', color3, 0, 2])
        elif (cub.upper[0][0] == color3 and cub.left[0][0] == color1 and cub.back[0][2] == color2):
            return ([['upper', color3, 0, 0],['left', color1, 0, 0]], ['back', color2, 0, 2])
        elif (cub.upper[0][0] == color3 and cub.left[0][0] == color2 and cub.back[0][2] == color1):
            return ([['upper', color3, 0, 0],['left', color2, 0, 0]], ['back', color1, 0, 2])
#f
        elif (cub.upper[0][2] == color1 and cub.right[0][2] == color2 and cub.back[0][0] == color3):
            return ([['upper', color1, 0, 2],['right', color2, 0, 2]], ['back', color3, 0, 0])
        elif (cub.upper[0][2] == color1 and cub.right[0][2] == color3 and cub.back[0][0] == color2):
            return ([['upper', color1, 0, 2],['right', color3, 0, 2]], ['back', color2, 0, 0])
        elif (cub.upper[0][2] == color2 and cub.right[0][2] == color3 and cub.back[0][0] == color1):
            return ([['upper', color2, 0, 2],['right', color3, 0, 2]], ['back', color1, 0, 0])
        elif (cub.upper[0][2] == color2 and cub.right[0][2] == color1 and cub.back[0][0] == color3):
            return ([['upper', color2, 0, 2],['right', color1, 0, 2]], ['back', color3, 0, 0])
        elif (cub.upper[0][2] == color3 and cub.right[0][2] == color1 and cub.back[0][0] == color2):
            return ([['upper', color3, 0, 2],['right', color1, 0, 2]], ['back', color2, 0, 0])
        elif (cub.upper[0][2] == color3 and cub.right[0][2] == color2 and cub.back[0][0] == color1):
            return ([['upper', color3, 0, 2],['right', color2, 0, 2]], ['back', color1, 0, 0])
#f
        elif (cub.upper[2][2] == color1 and cub.right[0][0] == color2 and cub.front[0][2] == color3):
            return ([['upper', color1, 2, 2],['right', color2, 0, 0]], ['front', color3, 0, 2])
        elif (cub.upper[2][2] == color1 and cub.right[0][0] == color3 and cub.front[0][2] == color2):
            return ([['upper', color1, 2, 2],['right', color3, 0, 0]], ['front', color2, 0, 2])
        elif (cub.upper[2][2] == color2 and cub.right[0][0] == color3 and cub.front[0][2] == color1):
            return ([['upper', color2, 2, 2],['right', color3, 0, 0]], ['front', color1, 0, 2])
        elif (cub.upper[2][2] == color2 and cub.right[0][0] == color1 and cub.front[0][2] == color3):
            return ([['upper', color2, 2, 2],['right', color1, 0, 0]], ['front', color3, 0, 2])
        elif (cub.upper[2][2] == color3 and cub.right[0][0] == color1 and cub.front[0][2] == color2):
            return ([['upper', color3, 2, 2],['right', color1, 0, 0]], ['front', color2, 0, 2])
        elif (cub.upper[2][2] == color3 and cub.right[0][0] == color2 and cub.front[0][2] == color1):
            return ([['upper', color3, 2, 2],['right', color2, 0, 0]], ['front', color1, 0, 2])
#f
        elif (cub.upper[2][0] == color1 and cub.left[0][2] == color2 and cub.front[0][0] == color3):
            return ([['upper', color1, 2, 0],['left', color2, 0, 2]], ['front', color3, 0, 0])
        elif (cub.upper[2][0] == color1 and cub.left[0][2] == color3 and cub.front[0][0] == color2):
            return ([['upper', color1, 2, 0],['left', color3, 0, 2]], ['front', color2, 0, 0])
        elif (cub.upper[2][0] == color2 and cub.left[0][2] == color3 and cub.front[0][0] == color1):
            return ([['upper', color2, 2, 0],['left', color3, 0, 2]], ['front', color1, 0, 0])
        elif (cub.upper[2][0] == color2 and cub.left[0][2] == color1 and cub.front[0][0] == color3):
            return ([['upper', color2, 2, 0],['left', color1, 0, 2]], ['front', color3, 0, 0])
        elif (cub.upper[2][0] == color3 and cub.left[0][2] == color1 and cub.front[0][0] == color2):
            return ([['upper', color3, 2, 0],['left', color1, 0, 2]], ['front', color2, 0, 0])
        elif (cub.upper[2][0] == color3 and cub.left[0][2] == color2 and cub.front[0][0] == color1):
            return ([['upper', color3, 2, 0],['left', color2, 0, 2]], ['front', color1, 0, 0])
#f
        elif (cub.down[0][0] == color1 and cub.left[2][2] == color2 and cub.front[2][0] == color3):
            return ([['down', color1, 0, 0],['left', color2, 2, 2]], ['front', color3, 2, 0])
        elif (cub.down[0][0] == color1 and cub.left[2][2] == color3 and cub.front[2][0] == color2):
            return ([['down', color1, 0, 0],['left', color3, 2, 2]], ['front', color2, 2, 0])
        elif (cub.down[0][0] == color2 and cub.left[2][2] == color3 and cub.front[2][0] == color1):
            return ([['down', color2, 0, 0],['left', color3, 2, 2]], ['front', color1, 2, 0])
        elif (cub.down[0][0] == color2 and cub.left[2][2] == color1 and cub.front[2][0] == color3):
            return ([['down', color2, 0, 0],['left', color1, 2, 2]], ['front', color3, 2, 0])
        elif (cub.down[0][0] == color3 and cub.left[2][2] == color1 and cub.front[2][0] == color2):
            return ([['down', color3, 0, 0],['left', color1, 2, 2]], ['front', color2, 2, 0])
        elif (cub.down[0][0] == color3 and cub.left[2][2] == color2 and cub.front[2][0] == color1):
            return ([['down', color3, 0, 0],['left', color2, 2, 2]], ['front', color1, 2, 0])
#f
        elif (cub.down[0][2] == color1 and cub.right[2][0] == color2 and cub.front[2][2] == color3):
            return ([['down', color1, 0, 2],['right', color2, 2, 0]], ['front', color3, 2, 2])
        elif (cub.down[0][2] == color1 and cub.right[2][0] == color3 and cub.front[2][2] == color2):
            return ([['down', color1, 0, 2],['right', color3, 2, 0]], ['front', color2, 2, 2])
        elif (cub.down[0][2] == color2 and cub.right[2][0] == color3 and cub.front[2][2] == color1):
            return ([['down', color2, 0, 2],['right', color3, 2, 0]], ['front', color1, 2, 2])
        elif (cub.down[0][2] == color2 and cub.right[2][0] == color1 and cub.front[2][2] == color3):
            return ([['down', color2, 0, 2],['right', color1, 2, 0]], ['front', color3, 2, 2])
        elif (cub.down[0][2] == color3 and cub.right[2][0] == color1 and cub.front[2][2] == color2):
            return ([['down', color3, 0, 2],['right', color1, 2, 0]], ['front', color2, 2, 2])
        elif (cub.down[0][2] == color3 and cub.right[2][0] == color2 and cub.front[2][2] == color1):
            return ([['down', color3, 0, 2],['right', color2, 2, 0]], ['front', color1, 2, 2])
#f
        elif (cub.down[2][2] == color1 and cub.right[2][2] == color2 and cub.back[2][0] == color3):
            return ([['down', color1, 2, 2],['right', color2, 2, 2]], ['back', color3, 2, 0])
        elif (cub.down[2][2] == color1 and cub.right[2][2] == color3 and cub.back[2][0] == color2):
            return ([['down', color1, 2, 2],['right', color3, 2, 2]], ['back', color2, 2, 0])
        elif (cub.down[2][2] == color2 and cub.right[2][2] == color3 and cub.back[2][0] == color1):
            return ([['down', color2, 2, 2],['right', color3, 2, 2]], ['back', color1, 2, 0])
        elif (cub.down[2][2] == color2 and cub.right[2][2] == color1 and cub.back[2][0] == color3):
            return ([['down', color2, 2, 2],['right', color1, 2, 2]], ['back', color3, 2, 0])
        elif (cub.down[2][2] == color3 and cub.right[2][2] == color1 and cub.back[2][0] == color2):
            return ([['down', color3, 2, 2],['right', color1, 2, 2]], ['back', color2, 2, 0])
        elif (cub.down[2][2] == color3 and cub.right[2][2] == color2 and cub.back[2][0] == color1):
            return ([['down', color3, 2, 2],['right', color2, 2, 2]], ['back', color1, 2, 0])
#
        elif (cub.down[2][0] == color1 and cub.left[2][0] == color2 and cub.back[2][2] == color3):
            return ([['down', color1, 2, 2],['left', color2, 2, 0]], ['back', color3, 2, 2])
        elif (cub.down[2][0] == color1 and cub.left[2][0] == color3 and cub.back[2][2] == color2):
            return ([['down', color1, 2, 2],['left', color3, 2, 0]], ['back', color2, 2, 2])
        elif (cub.down[2][0] == color2 and cub.left[2][0] == color3 and cub.back[2][2] == color1):
            return ([['down', color2, 2, 2],['left', color3, 2, 0]], ['back', color1, 2, 2])
        elif (cub.down[2][0] == color2 and cub.left[2][0] == color1 and cub.back[2][2] == color3):
            return ([['down', color2, 2, 2],['left', color1, 2, 0]], ['back', color3, 2, 2])
        elif (cub.down[2][0] == color3 and cub.left[2][0] == color1 and cub.back[2][2] == color2):
            return ([['down', color3, 2, 2],['left', color1, 2, 0]], ['back', color2, 2, 2])
        elif (cub.down[2][0] == color3 and cub.left[2][0] == color2 and cub.back[2][2] == color1):
            return ([['down', color3, 2, 2],['left', color2, 2, 0]], ['back', color1, 2, 2])
        return (False)
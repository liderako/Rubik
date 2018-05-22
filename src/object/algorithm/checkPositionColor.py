import sys
from src.object.Cubik import *
from src.object.CheckerColors import *

def 	checkPositionColor(cubOrigin, cubCurrent, colorOne, colorTwo, colorThree="null"):
	checkerManager = CheckerColors()
	if (colorThree == "null"):
		listPositionCubCurrent = checkerManager.two(cubCurrent, colorOne, colorTwo)
		listPositionCubOrigin = checkerManager.two(cubOrigin, colorOne, colorTwo)
		i = 0
		while (i < len(listPositionCubOrigin)):
			if (listPositionCubOrigin[i] != listPositionCubCurrent[i]):
				return (False)
			i += 1
		return True
	else:
		listPositionCubCurrent = checkerManager.three(cubCurrent, colorOne, colorTwo, colorThree)
		listPositionCubOrigin = checkerManager.three(cubOrigin, colorOne, colorTwo, colorThree)
		i = 0
		listOne = listPositionCubOrigin[1]
		while (i < len(listPositionCubOrigin)):
			j = 0
			while (j < len(listPositionCubOrigin[0])):
				if (listPositionCubOrigin[i][j] != listPositionCubCurrent[i][j]):
					return (False)
				j += 1
			i += 1
		return True
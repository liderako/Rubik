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
		# three colors functions
		pass
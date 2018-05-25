
import sys
from Cubik import Cubik
from CheckerColors import *

def finHorizontalMove(cubOrigin, cubCurrent, moveList):
	checkerManager = CheckerColors()
	colors = ["green", "blue", "red", "orange", "white", "yellow"]
	i = 0
	while (i == 0):
		if cubCurrent.front[0][2] == 'orange' and cubCurrent.front[1][2] == 'orange' and cubCurrent.front[2][2] == 'green':
			moveList.append("U")
			break
		if cubCurrent.front[0][2] == 'red' and cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'green':
			moveList.append("D")
			break
		if cubCurrent.front[0][2] == 'blue' and cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'green':
			moveList.append("D2")
			break
		if cubCurrent.front[0][2] == 'orange':
			moveList.append("U")
		elif cubCurrent.front[0][2] == 'red':
			moveList.append("U'")
		elif cubCurrent.front[0][2] == 'blue':
			moveList.append("U'")
			moveList.append("U'")
		if cubCurrent.front[1][2] == 'orange' and cubCurrent.front[2][2] == 'green':
			moveList.append("D")
			moveList.append("U'")
			break
		if cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'green':
			moveList.append("D'")
			moveList.append("U")
			break
		if cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'green':
			moveList.append("U2")
			moveList.append("D'")
			moveList.append("D'")
			break
		if cubCurrent.front[1][2] == 'orange' and cubCurrent.front[2][2] == 'red':
			moveList.append("U'")
			moveList.append("D2")
			break
		if cubCurrent.front[1][2] == 'orange' and cubCurrent.front[2][2] == 'blue':
			moveList.append("D'")
			moveList.append("D'")
			break
		if cubCurrent.front[1][2] == 'orange' and cubCurrent.front[2][2] == 'orange':
			moveList.append("U'")
			break
		if cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'blue':
			moveList.append("D")
			moveList.append("D")
			break
		if cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'orange':
			moveList.append("U")
			moveList.append("D2")
			break
		if cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'red':
			moveList.append("U")
			break
		if cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'orange':
			moveList.append("U")
			break
		if cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'red':
			moveList.append("U2", "D'")
			break
		if cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'blue':
			moveList.append("U2")
			break
		if cubCurrent.front[2][2] == 'orange':
			moveList.append("D'")
		if cubCurrent.front[2][2] == 'red':
			moveList.append("D")
		if cubCurrent.front[2][2] == 'blue':
			moveList.append("D2")
		i += 1

	return moveList

#for test
#cub = Cubik(3)

#cubmove = Cubik(3)
#cubmove.moveDoubleD()
#cubmove.moveBackU()
#cubmove.moveDoubleU()
#cubmove.moveU()
#cubmove.moveBackD()
#cubmove.moveDoubleD()


#moveList = ["0"]

#print (finHorizontalMove(cub, cubmove, moveList))


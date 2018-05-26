
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
			cubmove.moveU()
			break
		if cubCurrent.front[0][2] == 'red' and cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'green':
			moveList.append("D")
			cubmove.moveD()
			break
		if cubCurrent.front[0][2] == 'blue' and cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'green':
			moveList.append("D2")
			cubmove.moveDoubleD()
			break
		if cubCurrent.front[0][2] == 'orange':
			moveList.append("U")
			cubmove.moveU()
		elif cubCurrent.front[0][2] == 'red':
			moveList.append("U'")
			cubmove.moveBackU()
		elif cubCurrent.front[0][2] == 'blue':
			moveList.append("U'")
			moveList.append("U'")
			cubmove.moveBackU()
			cubmove.moveBackU()
		if cubCurrent.front[1][2] == 'orange' and cubCurrent.front[2][2] == 'green':
			moveList.append("D")
			moveList.append("U'")
			cubmove.moveD()
			cubmove.moveBackU()
			break
		if cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'green':
			moveList.append("D'")
			moveList.append("U")
			cubmove.moveBackD()
			cubmove.moveU()
			break
		if cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'green':
			moveList.append("U2")
			moveList.append("D'")
			moveList.append("D'")
			cubmove.moveDoubleU()
			cubmove.moveBackD()
			cubmove.moveBackD()
			break
		if cubCurrent.front[1][2] == 'orange' and cubCurrent.front[2][2] == 'red':
			moveList.append("U'")
			moveList.append("D2")
			cubmove.moveBackU()
			cubmove.moveDoubleD()
			break
		if cubCurrent.front[1][2] == 'orange' and cubCurrent.front[2][2] == 'blue':
			moveList.append("D'")
			moveList.append("D'")
			cubmove.moveBackD()
			cubmove.moveBackD()
			break
		if cubCurrent.front[1][2] == 'orange' and cubCurrent.front[2][2] == 'orange':
			moveList.append("U'")
			cubmove.moveBackU()
			break
		if cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'blue':
			moveList.append("D2")
			cubmove.moveDoubleD()
			break
		if cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'orange':
			moveList.append("U")
			moveList.append("D2")
			cubmove.moveU()
			cubmove.moveDoubleD()
			break
		if cubCurrent.front[1][2] == 'red' and cubCurrent.front[2][2] == 'red':
			moveList.append("U")
			cubmove.moveU()
			break
		if cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'orange':
			moveList.append("U")
			cubmove.moveU()
			break
		if cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'red':
			moveList.append("U2", "D'")
			cubmove.moveDoubleU()
			cubmove.moveD()
			break
		if cubCurrent.front[1][2] == 'blue' and cubCurrent.front[2][2] == 'blue':
			moveList.append("U2")
			cubmove.moveDoubleU()
			break
		if cubCurrent.front[2][2] == 'orange':
			moveList.append("D'")
			cubmove.moveBackD()
		if cubCurrent.front[2][2] == 'red':
			moveList.append("D")
			cubmove.moveD()
		if cubCurrent.front[2][2] == 'blue':
			moveList.append("D2")
			cubmove.moveDoubleD()
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


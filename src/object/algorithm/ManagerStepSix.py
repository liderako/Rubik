import sys
from src.object.Cubik import *
from src.object.algorithm.checkPositionColor import *
from src.object.managers.MixManager import *
from src.appendListInList import appendListInList

class ManagerStepSix:

	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.listPositionCubCurrent = list()
		self.checkerManager = CheckerColors()

	def 	run(self, cubCurrent, solveMoveList):
		res = self.checkCorner(cubCurrent)
		if (res == 4):
			return True
		else:
			res = self.checkTryPosition(cubCurrent)
			if (res == 4):
				return True
			else:
				if res == 0:
					self.moveOneCornernToTryPosition(cubCurrent, solveMoveList)
				pass
	def 	checkCorner(self, cubCurrent):
		count = 0
		if ((self.finishedThreeColorPosition(cubCurrent, ["yellow", "green", "red"])) == True):
			count += 1
		if ((self.finishedThreeColorPosition(cubCurrent, ["yellow", "blue", "orange"])) == True):
			count += 1
		if ((self.finishedThreeColorPosition(cubCurrent, ["yellow", "red", "blue"])) == True):
			count += 1
		if ((self.finishedThreeColorPosition(cubCurrent, ["yellow", "orange", "green"])) == True):
			count += 1
		return (count)

	def 	updatePositionList(self, cub, colors):
		return (self.checkerManager.three(cub, colors[0], colors[1], colors[2]))

	def 	checkTryPosition(self, cubCurrent):
		count = 0
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, ["yellow", "green", "red"])
		if ((self.checkSide(cubCurrent, "front"))) == True:
			count += 1
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, ["yellow", "blue", "red"])
		if ((self.checkSide(cubCurrent, "right"))) == True:
			count += 1
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, ["yellow", "blue", "orange"])
		if ((self.checkSide(cubCurrent, "back"))) == True: 
			count += 1
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, ["yellow", "green", "orange"])
		if ((self.checkSide(cubCurrent, "left"))) == True:
			count += 1
		return (count)

	def finishedThreeColorPosition(self, cubCurrent, colorsList):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorsList[0], colorsList[1], colorsList[2])

	def 	checkSide(self, cubCurrent, face):
		if (face == "front"):
			return (self.checkDoubleSide(face, "right"))
		elif (face == "right"):
			return (self.checkDoubleSide(face, "back"))
		elif (face == "back"):
			return (self.checkDoubleSide(face, "left"))
		elif (face == "left"):
			return (self.checkDoubleSide(face, "front"))
		return False

	def 	checkDoubleSide(self, face, subFace):
		count = 0
		i = 0
		while (i < len(self.listPositionCubCurrent)):
			if (((self.listPositionCubCurrent[i][0]) == face) or ((self.listPositionCubCurrent[i][0]) == subFace)):
				count += 1
			i += 1
		return (count == 2)

	def 	moveOneCornernToTryPosition(self, cubCurrent, solveMoveList):
		mixManager = MixManager()
		mixManager.mixRun(["D", "L", "D'", "R'", "D", "L'", "D'", "R"], cubCurrent)
		appendListInList(solveMoveList, ["D", "L", "D'", "R'", "D", "L'", "D'", "R"])



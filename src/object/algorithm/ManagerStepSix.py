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
			if (res[0] == 4):
				return True
			else:
				if res[0] == 0:
					self.moveToTryPosition(cubCurrent, solveMoveList, ["D", "L", "D'", "R'", "D", "L'", "D'", "R"])
				res = self.checkTryPosition(cubCurrent)
				colorsList = res[1]
				patternList = self.getPattern(cubCurrent, colorsList)
				self.moveDownFace(cubCurrent, solveMoveList, patternList)

	def 	moveDownFace(self, cubCurrent, solveMoveList, patternList):
		face = patternList[1]
		if (face == "frontFace"):
			if (patternList[0] == "right"):
				self.moveToTryPosition(cubCurrent, solveMoveList, ["D", "L", "D'", "R'", "D", "L'", "D'", "R"])
			else:
				self.moveToTryPosition(cubCurrent, solveMoveList, ["D'", "R'", "D", "L", "D'", "R", "D", "L'"])
		elif (face == "backFace"):
			if (patternList[0] == "right"):
				self.moveToTryPosition(cubCurrent, solveMoveList, ["D", "R", "D'", "L'", "D", "R'", "D'", "L"])
			else:
				self.moveToTryPosition(cubCurrent, solveMoveList, ["D'", "L'", "D", "R", "D'", "L", "D", "R'"])
		elif (face == "rightFace"):
			if (patternList[0] == "right"):
				self.moveToTryPosition(cubCurrent, solveMoveList, ["D", "F", "D'", "B'", "D", "F'", "D'", "B"])
			else:
				self.moveToTryPosition(cubCurrent, solveMoveList, ["D'", "B'", "D", "F", "D'", "B", "D", "F'"])
		elif (face == "leftFace"):
			if (patternList[0] == "right"):
				self.moveToTryPosition(cubCurrent, solveMoveList, ["D", "B", "D'", "F'", "D", "B'", "D'", "F"])
			else:
				self.moveToTryPosition(cubCurrent, solveMoveList, ["D'", "F'", "D", "B", "D'", "F", "D", "B'"])
	
	def 	getPattern(self, cubCurrent, colorsList):
		patternList = list()
		if (["yellow", "green", "red"] == colorsList):
			patternList.append(self.getDirection(cubCurrent))
			if (patternList[0] == "left"):
				patternList.append("frontFace")
			else:
				patternList.append("rightFace")
		elif (["yellow", "blue", "orange"] == colorsList):
			patternList.append(self.getDirection(cubCurrent))
			if (patternList[0] == "left"):
				patternList.append("backFace")
			else:
				patternList.append("leftFace")
		elif (["yellow", "blue", "red"] == colorsList):
			patternList.append(self.getDirection(cubCurrent))
			if (patternList[0] == "left"):
				patternList.append("rightFace")
			else:
				patternList.append("backFace")
		elif (["yellow", "green", "orange"] == colorsList):
			patternList.append(self.getDirection(cubCurrent))
			if (patternList[0] == "left"):
				patternList.append("leftFace")
			else:
				patternList.append("frontFace")
		return patternList

	def 	getDirection(self, cubCurrent):
		cubCurrent.moveD()
		res = self.checkTryPosition(cubCurrent)
		direction = "left"
		if (res[0] == 0):
			direction = "right"
		cubCurrent.moveBackD()
		return (direction)

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
		correctCorner = list()
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, ["yellow", "green", "red"])
		if ((self.checkSide(cubCurrent, "front"))) == True:
			count += 1
			correctCorner = ["yellow", "green", "red"]
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, ["yellow", "blue", "red"])
		if ((self.checkSide(cubCurrent, "right"))) == True:
			count += 1
			correctCorner = ["yellow", "blue", "red"]
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, ["yellow", "blue", "orange"])
		if ((self.checkSide(cubCurrent, "back"))) == True: 
			count += 1
			correctCorner = ["yellow", "blue", "orange"]
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, ["yellow", "green", "orange"])
		if ((self.checkSide(cubCurrent, "left"))) == True:
			count += 1
			correctCorner = ["yellow", "green", "orange"]
		return (count, correctCorner)

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

	def 	moveToTryPosition(self, cubCurrent, solveMoveList, listMix):
		mixManager = MixManager()
		mixManager.mixRun(listMix, cubCurrent)
		appendListInList(solveMoveList, listMix)



import sys
from src.object.Cubik import *
from src.checkPositionColor import *
from src.object.managers.MixManager import *
from src.appendListInList import appendListInList

class ManagerStepFive:

	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.checkerManager = CheckerColors()

	def 	run(self, cubCurrent, solveMoveList):
		res = self.moveDown(cubCurrent, solveMoveList)
		if (res == 4):
			return True
		elif (res == 2):
			self.moveFace(cubCurrent, solveMoveList)

	def 	moveDown(self, cubCurrent, solveMoveList):
		count = 0
		while (count < 2):
			if ((self.finishedTwoColorPosition(cubCurrent, ["yellow", "green"])) == True):
				count += 1
			if ((self.finishedTwoColorPosition(cubCurrent, ["yellow", "blue"])) == True):
				count += 1
			if ((self.finishedTwoColorPosition(cubCurrent, ["yellow", "red"])) == True):
				count += 1
			if ((self.finishedTwoColorPosition(cubCurrent, ["yellow", "orange"])) == True):
				count += 1
			if (count == 4):
				return 4
			if (count < 2):
				count = 0
				cubCurrent.moveD()
				solveMoveList.append("D")
		return 2

	def 	finishedTwoColorPosition(self, cubCurrent, colorsList):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorsList[0], colorsList[1])


	def 	moveFace(self, cubCurrent, solveMoveList):
		res = 2
		if ((self.finishedTwoColorPosition(cubCurrent, ["yellow", "green"])) == True):
			if ((self.finishedTwoColorPosition(cubCurrent, ["yellow", "blue"])) == True):
				res = self.moveOppositeRibs(cubCurrent, solveMoveList, "right")
		if ((self.finishedTwoColorPosition(cubCurrent, ["yellow", "red"])) == True):
			if ((self.finishedTwoColorPosition(cubCurrent, ["yellow", "orange"])) == True):
				res = self.moveOppositeRibs(cubCurrent, solveMoveList, "front")
		if (res == 2):
			self.cornerChange(cubCurrent, solveMoveList, self.getIncorectCornern(cubCurrent))

	def 	moveOppositeRibs(self, cubCurrent, solveMoveList, face):
		mixManager = MixManager()
		if (face == "front"):
			mixManager.mixRun(["L", "D", "L'", "D", "L", "D2", "L'"], cubCurrent)
			appendListInList(solveMoveList, ["L", "D", "L'", "D", "L", "D2", "L'"])
		if (face == "right"):
			mixManager.mixRun(["F", "D", "F'", "D", "F", "D2", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["F", "D", "F'", "D", "F", "D2", "F'"])
		return self.moveDown(cubCurrent, solveMoveList)

	def 	getIncorectCornern(self, cubCurrent):
		isFalseBlue = self.finishedTwoColorPosition(cubCurrent, ["yellow", "blue"])
		isFalseGreen = self.finishedTwoColorPosition(cubCurrent, ["yellow", "green"])
		isFalseRed = self.finishedTwoColorPosition(cubCurrent, ["yellow", "red"])
		isFalseOrange = self.finishedTwoColorPosition(cubCurrent, ["yellow", "orange"])
		if (isFalseBlue == True and isFalseOrange == True):
			return ("front")
		elif (isFalseGreen == True and isFalseOrange == True):
			return ("right")
		elif (isFalseGreen == True and isFalseRed == True):
			return ("back")
		elif (isFalseRed  == True and isFalseBlue == True):
			return ("left")

	def 	cornerChange(self, cubCurrent, solveMoveList, face):
		mixManager = MixManager()
		if (face == "front"):
			mixManager.mixRun(["L", "D", "L'", "D", "L", "D2", "L'", "D"], cubCurrent)
			appendListInList(solveMoveList, ["L", "D", "L'", "D", "L", "D2", "L'", "D"])
		elif (face == "back"):
			mixManager.mixRun(["R", "D", "R'", "D", "R", "D2", "R'", "D"], cubCurrent)
			appendListInList(solveMoveList, ["R", "D", "R'", "D", "R", "D2", "R'", "D"])
		elif (face == "right"):
			mixManager.mixRun(["F", "D", "F'", "D", "F", "D2", "F'", "D"], cubCurrent)
			appendListInList(solveMoveList, ["F", "D", "F'", "D", "F", "D2", "F'", "D"])
		elif (face == "left"):
			mixManager.mixRun(["B", "D", "B'", "D", "B", "D2", "B'", "D"], cubCurrent)
			appendListInList(solveMoveList, ["B", "D", "B'", "D", "B", "D2", "B'", "D"])

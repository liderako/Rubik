import sys
from src.object.Cubik import *
from src.checkPositionColor import *
from src.object.managers.MixManager import *
from src.appendListInList import appendListInList

class ManagerStepSeven:

	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.listPositionCubCurrent = list()
		self.checkerManager = CheckerColors()
		self.cornerThree = ["yellow", "blue", "red"]
		self.cornerFour = ["yellow", "red", "green"]
		self.cornerOne = ["yellow", "green", "orange"]
		self.cornerTwo = ["yellow", "blue", "orange"]


	def 	run(self, cubCurrent, solveMoveList):
		self.moveSide(cubCurrent, solveMoveList, self.cornerOne)
		self.moveDown(cubCurrent, solveMoveList)	
		self.moveSide(cubCurrent, solveMoveList, self.cornerTwo)
		self.moveDown(cubCurrent, solveMoveList)
		self.moveSide(cubCurrent, solveMoveList, self.cornerThree)
		self.moveDown(cubCurrent, solveMoveList)
		self.moveSide(cubCurrent, solveMoveList, self.cornerFour)
		self.moveDown(cubCurrent, solveMoveList)
	
	def 	moveDown(self, cubCurrent, solveMoveList):
		cubCurrent.moveD ()
		solveMoveList.append("D")

	def 	moveSide(self, cubCurrent, solveMoveList, colorsList):
		mixManager = MixManager()
		while (self.finishedThreeColorPosition(cubCurrent, colorsList)) == False:
			mixManager.mixRun(["L'", "U'", "L", "U"], cubCurrent)
			appendListInList(solveMoveList, ["L'", "U'", "L", "U"])

	def finishedThreeColorPosition(self, cubCurrent, colorsList):
		listPos = self.checkerManager.three(cubCurrent, colorsList[0], colorsList[1], colorsList[2])
		listPosOrigin = self.checkerManager.three(self.cubOrigin, colorsList[0], colorsList[1], colorsList[2])
		if (listPos[0][0] == "down" and listPos[0][1] == "yellow"):
			return True
		return False
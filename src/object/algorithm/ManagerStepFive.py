import sys
from src.object.Cubik import *
from src.object.checkBackState import *
from src.object.managers.MixManager import *
from src.appendListInList import appendListInList

class ManagerStepFour:

	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.listPositionCubCurrent = list()
		self.listPositionCubOrigin = list()
		self.checkerManager = CheckerColors()

	def 	run(self, cubCurrent, solveMoveList):
		count = 0
		while (count < 2):
			if ((self.finishedTwoColorPosition(cubCurrent, "yellow", "green")) == True):
				count += 1
			if ((self.finishedTwoColorPosition(cubCurrent, "yellow", "blue")) == True):
				count += 1
			if ((self.finishedTwoColorPosition(cubCurrent, "yellow", "red")) == True):
				count += 1
			if ((self.finishedTwoColorPosition(cubCurrent, "yellow", "orange")) == True):
				count += 1

			if (count < 2):
				count = 0
				cubCurrent.moveD()
				solveMoveList.append("D")
		cubCurrent.printCubik()

	def finishedTwoColorPosition(self, cubCurrent, colorsList):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorsList[0], colorsList[1])
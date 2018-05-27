import sys
from src.object.Cubik import *
from src.object.algorithm.checkPositionColor import *
from src.appendListInList import *
from src.object.managers.MixManager import *

class ManagerStepTwo:
	
	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.listPositionCubCurrent = list()
		self.listPositionCubOrigin = list()
		self.checkerManager = CheckerColors()

	def 	run(self, cubCurrent, solveMoveList):
		if ((self.finishedThreeColorPosition(cubCurrent, "white", "green", "red")) == False):
			self.moving(cubCurrent, solveMoveList, "white", "green", "red", "front")
		if ((self.finishedThreeColorPosition(cubCurrent, "white", "red", "blue")) == False):
			self.moving(cubCurrent, solveMoveList, "white", "red", "blue", "right")
		if ((self.finishedThreeColorPosition(cubCurrent, "white", "blue", "orange")) == False):
			self.moving(cubCurrent, solveMoveList, "white", "blue", "orange", "back")
		if ((self.finishedThreeColorPosition(cubCurrent, "white", "orange", "green")) == False):
			self.moving(cubCurrent, solveMoveList, "white", "orange", "green", "left")

	def finishedThreeColorPosition(self, cubCurrent, colorOne, colorTwo, colorThree):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorOne, colorTwo, colorThree)

	def 	updatePositionList(self, cub, colorOne, colorTwo, colorThree):
		return (self.checkerManager.three(cub, colorOne, colorTwo, colorThree))

	def 	moving(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
		self.listPositionCubOrigin = self.updatePositionList(self.cubOrigin, colorOne, colorTwo, colorThree)
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)
		
		if (self.checkSide(cubCurrent, face)) == False:	
			if (self.listPositionCubCurrent[0][0] == "upper"):			
				self.moveEdgeDown(cubCurrent, solveMoveList, colorOne, colorTwo, colorThree)
			if 	(self.listPositionCubCurrent[0][0] == "down"):
				self.moveEdgeDownToTryPosition(cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face)
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)
		if (self.checkSide(cubCurrent, face)) == True:
			self.moveSide(cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face)

	def 	moveEdgeDown(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree):
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)
		mixManager = MixManager()
		if ((self.listPositionCubCurrent[1][0] == "right" and self.listPositionCubCurrent[2][0] == "front")):
			mixManager.mixRun(["F", "D'", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["F", "D'", "F'"])
		elif ((self.listPositionCubCurrent[1][0] == "left" and self.listPositionCubCurrent[2][0] == "front")):
			mixManager.mixRun(["F'", "D", "F"], cubCurrent)
			appendListInList(solveMoveList, ["F'", "D", "F"])
		elif ((self.listPositionCubCurrent[1][0] == "right" and self.listPositionCubCurrent[2][0] == "back")):
			mixManager.mixRun(["B'", "D", "B"], cubCurrent)
			appendListInList(solveMoveList, ["B'", "D", "B"])
		elif ((self.listPositionCubCurrent[1][0] == "left" and self.listPositionCubCurrent[2][0] == "back")):
			mixManager.mixRun(["B", "D'", "B'"], cubCurrent)
			appendListInList(solveMoveList, ["B", "D'", "B'"])
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)

	def 	moveEdgeDownToTryPosition(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
		while (self.checkSide(cubCurrent, face)) == False:
			cubCurrent.moveD()
			solveMoveList.append("D")
			self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)

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

	def 	moveSide(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
		mixManager = MixManager()
		while ((self.finishedThreeColorPosition(cubCurrent, colorOne, colorTwo, colorThree)) == False):
			if (face == "front"):
				mixManager.mixRun(["R'", "D'", "R", "D"], cubCurrent)
				appendListInList(solveMoveList, ["R'", "D'", "R", "D"])
			elif (face == "right"):
				mixManager.mixRun(["B'", "D'", "B", "D"], cubCurrent)
				appendListInList(solveMoveList, ["B'", "D'", "B", "D"])
			elif (face == "back"):
				mixManager.mixRun(["L'", "D'", "L", "D"], cubCurrent)
				appendListInList(solveMoveList, ["L'", "D'", "L", "D"])
			elif (face == "left"):
				mixManager.mixRun(["F'", "D'", "F", "D"], cubCurrent)
				appendListInList(solveMoveList, ["F'", "D'", "F", "D"])
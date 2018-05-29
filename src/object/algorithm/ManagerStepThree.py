import sys
from src.object.Cubik import *
from src.checkPositionColor import *
from src.appendListInList import *
from src.object.managers.MixManager import *

class ManagerStepThree:

	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.listPositionCubCurrent = list()
		self.listPositionCubOrigin = list()
		self.checkerManager = CheckerColors()
	
	def run(self, cubCurrent, solveMoveList):
		if ((self.finishedThreeColorPosition(cubCurrent, ["green", "orange"])) == False):
			self.moving(cubCurrent, solveMoveList, ["green", "orange"], "front")
		
		if ((self.finishedThreeColorPosition(cubCurrent, ["orange", "blue"])) == False):
			self.moving(cubCurrent, solveMoveList, ["orange", "blue"], "left")
		
		if ((self.finishedThreeColorPosition(cubCurrent, ["blue", "red"])) == False):
			self.moving(cubCurrent, solveMoveList, ["blue", "red"], "back")
		if ((self.finishedThreeColorPosition(cubCurrent, ["red", "green"])) == False):
			self.moving(cubCurrent, solveMoveList, ["red", "green"], "right")

	def finishedThreeColorPosition(self, cubCurrent, colorsList):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorsList[0], colorsList[1])

	def 	updatePositionList(self, cub, colorsList):
		return (self.checkerManager.two(cub, colorsList[0], colorsList[1]))

	def 	moving(self, cubCurrent, solveMoveList, colorsList, face):
		self.listPositionCubOrigin = self.updatePositionList(self.cubOrigin, colorsList)
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorsList)

		checkSideList = self.checkSide(cubCurrent, colorsList)
		
		if (checkSideList[0] == True):
			self.moveToTryPosition(cubCurrent, solveMoveList, colorsList)
		else:
			if (self.listPositionCubCurrent[0][0] != "down"):
				self.pushDown(cubCurrent, solveMoveList, colorsList)
				self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorsList)
			if (self.listPositionCubCurrent[0][0] != "down"):
				print ("ERROR DOWN IS NOT")
				sys.exit(-1)
			self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorsList)
			if (self.listPositionCubCurrent[0][0] == "down"):
				self.moveToCente(cubCurrent, solveMoveList, colorsList, face)
				self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorsList)
				self.moveToTryPosition(cubCurrent, solveMoveList, colorsList)
	def 	moveToCente(self, cubCurrent, solveMoveList, colorsList, face):
		checkSideList = self.checkSide(cubCurrent, colorsList)
		while (checkSideList[0] == False):
			cubCurrent.moveD()
			solveMoveList.append("D")
			checkSideList = self.checkSide(cubCurrent, colorsList)

	def 	pushDown(self, cubCurrent, solveMoveList, colorsList):
		faceOne, faceTwo, colorOne, colorTwo = self.getSideParams(cubCurrent, colorsList)
		pattern = self.getPatternPushDown(faceOne, faceTwo)
		if (pattern == "rightPattern"):
			self.moveFormulaRight(cubCurrent, solveMoveList, faceOne)
		elif (pattern == "leftPattern"):
			self.moveFormulaLeft(cubCurrent, solveMoveList, faceOne)

	def 	getPatternPushDown(self, faceOne, faceTwo):
		if (faceOne == "left"):
			if (faceTwo == "front"):
				return ("rightPattern")
			elif (faceTwo == "back"):
				return ("leftPattern")

		elif (faceOne == "front" and faceTwo == "right"):
				return ("rightPattern")
		elif (faceOne == "right" and faceTwo == "back"):
			return ("rightPattern")

	def 	getSideParams(self, cubCurrent, colorsList):
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorsList)
		down = self.listPositionCubCurrent[0][0]
		colorDown = self.listPositionCubCurrent[0][1]
		colorFace = self.listPositionCubCurrent[1][1]
		face = self.listPositionCubCurrent[1][0]
		return down, face, colorDown, colorFace

	def 	checkSide(self, cubCurrent, colorsList):
		down, face, colorDown, colorFace = self.getSideParams(cubCurrent, colorsList)
		if (down != "down"):
			return [False, "null"]
		if (face == "front"):
			if (colorDown == "orange" and colorFace == "green"):
				return [True, "leftPattern"] 
			elif (colorDown == "red" and colorFace == "green"):
				return [True, "rightPattern"] 
		if (face == "back"):
			if (colorDown == "orange" and colorFace == "blue"):
				return [True, "leftPattern"] 
			elif (colorDown == "red" and colorFace == "blue"):
				return [True, "rightPattern"]
		if (face == "right"):
			if (colorDown == "blue" and colorFace == "red"):
				return [True, "rightPattern"]
			elif (colorDown == "green" and colorFace == "red"):
				return [True, "leftPattern"] 
		if (face == "left"):
			if (colorDown == "green" and colorFace == "orange"):
				return [True, "rightPattern"] 
			elif (colorDown == "blue" and colorFace == "orange"):
				return [True, "leftPattern"]
		return [False, "null"]

	def 	moveToTryPosition(self, cubCurrent, solveMoveList, colorsList):
		down, face, colorDown, colorFace = self.getSideParams(cubCurrent, colorsList)
		checkSideList = self.checkSide(cubCurrent, colorsList)
		if (checkSideList[1] == "rightPattern"):
			self.moveFormulaRight(cubCurrent, solveMoveList, face)
		elif (checkSideList[1] == "leftPattern"):
			self.moveFormulaLeft(cubCurrent, solveMoveList, face)

	def 	moveFormulaLeft(self, cubCurrent, solveMoveList, face):
		mixManager = MixManager()

		if (face == "front"):
			mixManager.mixRun([ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ], cubCurrent)
			appendListInList(solveMoveList, [ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ])
		elif (face == "left"):
			mixManager.mixRun([ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ], cubCurrent)
			appendListInList(solveMoveList, [ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ])
		elif (face == "back"):
			mixManager.mixRun([ "D'", "L'", "D", "L", "D", "B", "D'", "B'" ], cubCurrent)
			appendListInList(solveMoveList, [ "D'", "L'", "D", "L", "D", "B", "D'", "B'" ])
		elif (face == "right"):
			mixManager.mixRun([ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ], cubCurrent)
			appendListInList(solveMoveList, [ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ])

	def 	moveFormulaRight(self, cubCurrent, solveMoveList, face):
		mixManager = MixManager()
		if (face == "front"):
			mixManager.mixRun([ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ], cubCurrent)
			appendListInList(solveMoveList, [ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ])
		elif (face == "left"):
			mixManager.mixRun([ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ], cubCurrent)
			appendListInList(solveMoveList, [ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ])
		elif (face == "right"):
			mixManager.mixRun([ "D'", "B'", "D", "B", "D", "R", "D'", "R'"], cubCurrent)
			appendListInList(solveMoveList, [ "D'", "B'", "D", "B", "D", "R", "D'", "R'"])
		elif (face == "back"):
			mixManager.mixRun([ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ], cubCurrent)
			appendListInList(solveMoveList, [ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ])
import sys
from src.object.Cubik import *
from src.object.algorithm.checkPositionColor import *

class ManagerStepThree:
	
	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.listPositionCubCurrent = list()
		self.listPositionCubOrigin = list()
		self.checkerManager = CheckerColors()

	def run(self, cubCurrent, solveMoveList):
		if ((self.finishedThreeColorPosition(cubCurrent, ["green", "orange"])) == False):
			moving(cubCurrent, solveMoveList, ["green", "orange"], "front")
		
		# if ((self.finishedThreeColorPosition(cubCurrent, ["orange", "blue"])) == False):
			# moving(cubCurrent, solveMoveList, ["orange", "blue"], "left")
		
		# if ((self.finishedThreeColorPosition(cubCurrent, ["blue", "red"])) == False):
			# moving(cubCurrent, solveMoveList, ["blue", "red"], "back")
		
		# if ((self.finishedThreeColorPosition(cubCurrent, ["red", "green"])) == False):
			# moving(cubCurrent, solveMoveList, ["red", "green"], "right")
	
	def finishedThreeColorPosition(self, cubCurrent, colorsList):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorsList[0], colorsList[1])

	def 	updatePositionList(self, cub, colorsList):
		return (self.checkerManager.two(cub, colorsList[0], colorsList[1]))

	def 	moving(self, cubCurrent, solveMoveList, colorsList, face):
		self.listPositionCubOrigin = self.updatePositionList(self.cubOrigin, colorsList)
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorsList)

		if (self.listPositionCubCurrent[0][0] == "upper"):
			self.moveToCente(cubCurrent, solveMoveList, colorsList, face)

	def 	moveToCente(self, cubCurrent, solveMoveList, colorsList, face):
		# while ()
		pass

	def 	checkSide(self, cubCurrent, colorsList):
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorsList)

		upper = self.listPositionCubCurrent[0][0]
		colorDown = self.listPositionCubCurrent[0][1]
		colorFace = self.listPositionCubCurrent[1][1]
		face = self.listPositionCubCurrent[1][0]
		if (upper != "down"):
			return False
		if (colorDown == "green" and colorFace == "orange" and face == "right"):
			return True
		elif (colorDown == "orange" and colorFace == "green" and face == "front"):
			return True
		elif (colorDown == "blue" and colorFace == "orange" and face == "right"):
			return True
		elif (colorDown == "orange" and colorFace == "blue" and face == "back"):
			return True
		elif (colorDown == "red" and colorFace == "blue" and face == "back"):
			return True
		elif (colorDown == "blue" and colorFace == "red" and face == "left"):
			return True
		elif (colorDown == "red" and colorFace == "green" and face == "front"):
			return True
		elif (colorDown == "green" and colorFace == "red" and face == "left"):
			return True
		return False
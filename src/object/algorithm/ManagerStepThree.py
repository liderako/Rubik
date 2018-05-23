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
		print ("______________________START___________________________")
		cubCurrent.printCubik()
		print ("______________________________________________________")
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
			print ("CheckSide true")
			print ("ColorsList", colorsList)
			print ("End")
		# if (self.listPositionCubCurrent[0][0] == "upper"):
			# self.moveToCente(cubCurrent, solveMoveList, colorsList, face)

	# def 	moveToCente(self, cubCurrent, solveMoveList, colorsList, face):
	# 	# while ()
	# 	pass

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

		if (colorDown == "green" and colorFace == "orange" and face == "left"):
			return [True,"left"]
		elif (colorDown == "orange" and colorFace == "green" and face == "front"):
			return [True,"right"]
		elif (colorDown == "blue" and colorFace == "orange" and face == "left"):
			return [True,"right"]
		elif (colorDown == "orange" and colorFace == "blue" and face == "back"):
			return [True,"left"]
		elif (colorDown == "red" and colorFace == "blue" and face == "back"):
			return [True,"right"]
		elif (colorDown == "blue" and colorFace == "red" and face == "right"):
			return [True,"left"]
		elif (colorDown == "red" and colorFace == "green" and face == "front"):
			return [True,"left"]
		elif (colorDown == "green" and colorFace == "red" and face == "right"):
			return [True,"right"]
		return [False, "null"]

	def 	moveToTryPosition(self, cubCurrent, solveMoveList, colorsList):
		down, face, colorDown, colorFace = self.getSideParams(cubCurrent, colorsList)

		checkSideList = self.checkSide(cubCurrent, ColorsList)
		if (checkSideList[1] == "right"):
			self.moveFormulaRight(cubCurrent, solveMoveList, face)
		elif (checkSideList[1] == "left"):
			self.moveFormulaRight()
		else:
			print ("WTF??! move to try position")
			sys.exit(-1)

	def 	moveFormulaLeft(self, cubCurrent, solveMoveList, face):
		if (face == "front"):
			cubCurrent.moveD()
			# cubCurrent.moveBackR()
			# cubCurrent.moveBackD()
		elif (face == "left"):
			pass
		elif (face == "back"):
			pass
		elif (face == "right"):
			pass

	def 	moveFormulaRight(self, cubCurrent, solveMoveList, face):
		if (face == "front"):
			pass
		elif (face == "left"):
			pass
		elif (face == "back"):
			pass
		elif (face == "right"):
			pass

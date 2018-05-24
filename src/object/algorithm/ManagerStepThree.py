import sys
from src.object.Cubik import *
from src.object.algorithm.checkPositionColor import *
from src.appendListInList import *
from src.object.managers.MixManager import *

class ManagerStepThree:

	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.listPositionCubCurrent = list()
		self.listPositionCubOrigin = list()
		self.checkerManager = CheckerColors()
	
	def run(self, cubCurrent, solveMoveList):
		print ("______________________START___________________________") #################################################### delelte delete line
		cubCurrent.printCubik() #################################################### delelte delete line
		print ("______________________________________________________") #################################################### delelte delete line

		if ((self.finishedThreeColorPosition(cubCurrent, ["green", "orange"])) == False):
			self.moving(cubCurrent, solveMoveList, ["green", "orange"], "front")
		
		if ((self.finishedThreeColorPosition(cubCurrent, ["orange", "blue"])) == False):
			self.moving(cubCurrent, solveMoveList, ["orange", "blue"], "left")
		
		if ((self.finishedThreeColorPosition(cubCurrent, ["blue", "red"])) == False):
			self.moving(cubCurrent, solveMoveList, ["blue", "red"], "back")
		# 
		if ((self.finishedThreeColorPosition(cubCurrent, ["red", "green"])) == False):
			self.moving(cubCurrent, solveMoveList, ["red", "green"], "right")
		print ("______________________END___________________________") #################################################### delelte delete line
		cubCurrent.printCubik() #################################################### delelte delete line
		print ("Solve Move") ######################################################
		for x in solveMoveList: ######################################################
			print (x, end=" ") ############################# #########################
		print("") ######################################################
		######################################################
		print ("______________________________________________________") #################################################### delelte delete line
	
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
		print ("PATTERN ", checkSideList[1])
		if (checkSideList[1] == "rightPattern"):
			self.moveFormulaRight(cubCurrent, solveMoveList, face)
		elif (checkSideList[1] == "leftPattern"):
			self.moveFormulaLeft(cubCurrent, solveMoveList, face)
		else: #################################################### delelte delete line
			print ("WTF??! move to try position") #################################################### delelte delete line
			sys.exit(-1) #################################################### delelte delete line

	def 	moveFormulaLeft(self, cubCurrent, solveMoveList, face):
		mixManager = MixManager()

		if (face == "front"): # [ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ]
			mixManager.mixRun([ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ], cubCurrent)
			appendListInList(solveMoveList, [ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ])
		elif (face == "left"): # [ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ]
			mixManager.mixRun([ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ], cubCurrent)
			appendListInList(solveMoveList, [ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ])
			print ("FACE left- RIGHT BUG")
		elif (face == "back"): # D' L' D L D B D' B'
			mixManager.mixRun([ "D'", "L'", "D", "L", "D", "B", "D'", "B'" ], cubCurrent)
			appendListInList(solveMoveList, [ "D'", "L'", "D", "L", "D", "B", "D'", "B'" ])
		elif (face == "right"): # [ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ]
			mixManager.mixRun([ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ], cubCurrent)
			appendListInList(solveMoveList, [ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ])

	def 	moveFormulaRight(self, cubCurrent, solveMoveList, face):
		mixManager = MixManager()
		if (face == "front"): # [ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ]
			mixManager.mixRun([ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ], cubCurrent)
			appendListInList(solveMoveList, [ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ])
		elif (face == "left"): # [ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ]
			print ("FACE left- RIGHT BUG")
			mixManager.mixRun([ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ], cubCurrent)
			appendListInList(solveMoveList, [ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ])
		elif (face == "right"): # [ "D'", "B'", "D", "B", "D", "R", "D'", "R'"]
			mixManager.mixRun([ "D'", "B'", "D", "B", "D", "R", "D'", "R'"], cubCurrent)
			appendListInList(solveMoveList, [ "D'", "B'", "D", "B", "D", "R", "D'", "R'"])
		elif (face == "back"): # [ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ]
			mixManager.mixRun([ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ], cubCurrent)
			appendListInList(solveMoveList, [ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ])
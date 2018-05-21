import sys
from src.object.Cubik import *
from src.object.algorithm.checkPositionColor import *

class ManagerStepOne:
	
	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.listPositionCubCurrent = list()
		self.listPositionCubOrigin = list()
		self.checkerManager = CheckerColors()

	def run(self, cubCurrent, solveMoveList):
		if ((self.finishedTwoColorPosition(cubCurrent, "white", "green")) == False):
			self.edgeMoveTwoColor(cubCurrent, solveMoveList, "white", "green", "front")
		# if ((self.finishedTwoColorPosition(cubCurrent, "white", "blue")) == False):
		# 	self.edgeMoveTwoColor(cubCurrent, solveMoveList, "white", "blue", "back")
		# if ((self.finishedTwoColorPosition(cubCurrent, "white", "red")) == False):
		# 	self.edgeMoveTwoColor(cubCurrent, solveMoveList,  "white", "red", "right")
		# if ((self.finishedTwoColorPosition(cubCurrent, "white", "orange")) == False):
		# 	self.edgeMoveTwoColor(cubCurrent, solveMoveList, "white", "orange", "left")
		# cubCurrent.printCubik()
		# print (solveMoveList)

	def finishedTwoColorPosition(self, cubCurrent, colorOne, colorTwo):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorOne, colorTwo)

	def edgeMoveTwoColor(self, cubCurrent, solveMoveList, colorOne, colorTwo, face):
		self.listPositionCubCurrent = self.checkerManager.two(cubCurrent, colorOne, colorTwo)
		self.listPositionCubOrigin = self.checkerManager.two(self.cubOrigin, colorOne, colorTwo)
		print (self.listPositionCubCurrent)
		print (self.listPositionCubOrigin)
		if (face != self.listPositionCubCurrent[0][0] and face != self.listPositionCubCurrent[1][0]):
			print ("moveDOwn")
			print (self.listPositionCubCurrent)
			print (self.listPositionCubOrigin)
			self.moveDownTwoColor(cubCurrent, solveMoveList, colorOne, colorTwo)		
		# if (face == self.listPositionCubCurrent[0][0] or face == self.listPositionCubCurrent[1][0]):
		# 	self.moveCenter(cubCurrent, solveMoveList, face, colorOne, colorTwo)
		# 	if (self.listPositionCubCurrent[0][1] != self.listPositionCubOrigin[0][1]):
		# 		self.changeSide(cubCurrent, solveMoveList, face)
		# 		print ("changeSide") ### delete

	def 	moveCenter(self, cubCurrent, solveMoveList, face, colorOne, colorTwo):
		while (self.listPositionCubCurrent[1][2] != self.listPositionCubOrigin[1][2]):
			if (face == "front"):
				cubCurrent.moveBackF()
				solveMoveList.append("F'")
			if (face == "right"):
				cubCurrent.moveBackR()
				solveMoveList.append("R'")
			if (face == "left"):
				cubCurrent.moveBackL()
				solveMoveList.append("L'")
			if (face == "back"):
				cubCurrent.moveBackB()
				solveMoveList.append("B'")
			self.listPositionCubCurrent = self.checkerManager.two(cubCurrent, colorOne, colorTwo)
	
	def 	moveDownTwoColor(self, cubCurrent, solveMoveList, colorOne, colorTwo):
		faceOne = self.listPositionCubCurrent[0][0]
		faceTwo = self.listPositionCubCurrent[0][1]
		while (faceOne != "down" or faceTwo != "down"):
			# if (faceOne == "down" or faceTwo == "down"):
				# break ;
			if (faceOne == "front" or faceTwo == "front"):
				cubCurrent.moveF()
				solveMoveList.append("F")
			elif (faceOne == "left" or faceTwo == "left"):
				cubCurrent.moveL()
				solveMoveList.append("L")
			elif (faceOne == "right" or faceTwo == "right"):
				cubCurrent.moveR()
				solveMoveList.append("R")
			elif (faceOne == "back" or faceTwo == "back"):
				cubCurrent.moveB()
				solveMoveList.append("B")
			elif (faceOne == "upper" or faceTwo == "upper"):
				cubCurrent.moveB()
				solveMoveList.append("B")
			self.listPositionCubCurrent = self.checkerManager.two(cubCurrent, colorOne, colorTwo)
			faceOne = self.listPositionCubCurrent[0][0]
			faceTwo = self.listPositionCubCurrent[0][1]
			print (self.listPositionCubCurrent)
		print ("OK", self.listPositionCubCurrent)
		sys.exit(-1)
		# while (self.listPositionCubCurrent)

	def    changeSide(self, cubCurrent, solveMoveList, face):
		if (face == "front"):
			cubCurrent.moveF()
			cubCurrent.moveBackU()
			cubCurrent.moveR()
			cubCurrent.moveU()
			solveMoveList.append("F")
			solveMoveList.append("U'")
			solveMoveList.append("R")
			solveMoveList.append("U")
		elif (face == "right"):
			cubCurrent.moveR()
			cubCurrent.moveBackU()
			cubCurrent.moveB()
			cubCurrent.moveU()
			solveMoveList.append("R")
			solveMoveList.append("U'")
			solveMoveList.append("B")
			solveMoveList.append("U")
		elif (face == "left"):
			cubCurrent.moveL()
			cubCurrent.moveBackU()
			cubCurrent.moveF()
			cubCurrent.moveU()
			solveMoveList.append("L")
			solveMoveList.append("U'")
			solveMoveList.append("F")
			solveMoveList.append("U")
		elif (face == "back"):
			cubCurrent.moveB()
			cubCurrent.moveBackU()
			cubCurrent.moveL()
			cubCurrent.moveU()
			solveMoveList.append("B")
			solveMoveList.append("U'")
			solveMoveList.append("L")
			solveMoveList.append("U")
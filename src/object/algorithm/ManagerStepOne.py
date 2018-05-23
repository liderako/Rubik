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
		if ((self.finishedTwoColorPosition(cubCurrent, "white", "blue")) == False):
			self.edgeMoveTwoColor(cubCurrent, solveMoveList, "white", "blue", "back")
		if ((self.finishedTwoColorPosition(cubCurrent, "white", "red")) == False):
			self.edgeMoveTwoColor(cubCurrent, solveMoveList,  "white", "red", "right")
		if ((self.finishedTwoColorPosition(cubCurrent, "white", "orange")) == False):
			self.edgeMoveTwoColor(cubCurrent, solveMoveList, "white", "orange", "left")

	def finishedTwoColorPosition(self, cubCurrent, colorOne, colorTwo):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorOne, colorTwo)

	def edgeMoveTwoColor(self, cubCurrent, solveMoveList, colorOne, colorTwo, face):
		self.listPositionCubCurrent = self.checkerManager.two(cubCurrent, colorOne, colorTwo)
		self.listPositionCubOrigin = self.checkerManager.two(self.cubOrigin, colorOne, colorTwo)

		if (face != self.listPositionCubCurrent[0][0] and face != self.listPositionCubCurrent[1][0]):
			self.moveDownTwoColor(cubCurrent, solveMoveList, colorOne, colorTwo, face)
		
		if (face == self.listPositionCubCurrent[0][0] or face == self.listPositionCubCurrent[1][0]):
			self.moveCenter(cubCurrent, solveMoveList, face, colorOne, colorTwo)
			if (self.listPositionCubCurrent[0][1] != self.listPositionCubOrigin[0][1]):
				self.changeSide(cubCurrent, solveMoveList, face)

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

	
	def 	updateFaceColor(self, cubCurrent, colorOne, colorTwo):
		self.listPositionCubCurrent = self.checkerManager.two(cubCurrent, colorOne, colorTwo)
		return self.listPositionCubCurrent[0][0], self.listPositionCubCurrent[1][0]

	def 	moveDownTwoColor(self, cubCurrent, solveMoveList, colorOne, colorTwo, face):
		faceOne,faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)

		def 	moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face):
			faceOne,faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
			while (1):
				if (faceOne == face or faceTwo == face):
					break
				cubCurrent.moveD()
				solveMoveList.append("D")
				faceOne,faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
		
		def 	optimizationStep(count, solveMoveList, move):
			if (count == 3):
				count = 1
				solveMoveList.append(move + "'")
				return count, 1
			else:
				x = 0
				while (x != count):
					x += 1
					solveMoveList.append(move)
			return count, 0

		count = 0
		if (faceOne == "front" or faceTwo == "front"):
			while (1):
				if (faceOne == "down" or faceTwo == "down"):
					break
				count += 1
				cubCurrent.moveF()
				faceOne,faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
			count, flag = optimizationStep(count, solveMoveList, "F")
			moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face)
			while (count != 0):
				count -= 1
				if (flag == 0):
					cubCurrent.moveBackF()
					solveMoveList.append("F'")
				else:
					cubCurrent.moveF()
					solveMoveList.append("F")
		elif (faceOne == "left" or faceTwo == "left"):
			while (1):
				if (faceOne == "down" or faceTwo == "down"):
					break
				count += 1
				cubCurrent.moveL()
				faceOne,faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
			count,flag = optimizationStep(count, solveMoveList, "L")
			moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face)
			while (count != 0):
				count -= 1
				if (flag == 0):
					cubCurrent.moveBackL()
					solveMoveList.append("L'")
				else:
					cubCurrent.moveL()
					solveMoveList.append("L")
		
		elif (faceOne == "right" or faceTwo == "right"):
			while (1):
				if (faceOne == "down" or faceTwo == "down"):
					break
				count += 1
				cubCurrent.moveR()
				faceOne,faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
			count,flag = optimizationStep(count, solveMoveList, "R")
			moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face)
			while (count != 0):
				count -= 1
				if (flag == 0):
					cubCurrent.moveBackR()
					solveMoveList.append("R'")
				else:
					cubCurrent.moveR()
					solveMoveList.append("R")
		
		elif (faceOne == "back" or faceTwo == "back"):
			while (1):
				if (faceOne == "down" or faceTwo == "down"):
					break
				count += 1
				cubCurrent.moveB()
				faceOne,faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
			count,flag = optimizationStep(count, solveMoveList, "B")
			moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face)
			while (count != 0):
				count -= 1
				if (flag == 0):
					cubCurrent.moveBackB()
					solveMoveList.append("B'")
				else:
					cubCurrent.moveB()
					solveMoveList.append("B")

	@staticmethod
	def    changeSide(cubCurrent, solveMoveList, face):
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
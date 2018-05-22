import sys
from src.object.Cubik import *
from src.object.algorithm.checkPositionColor import *

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
		print ("End")
		cubCurrent.printCubik()
		for x in solveMoveList:
			print (x, end=" ")
		print("")
	def finishedThreeColorPosition(self, cubCurrent, colorOne, colorTwo, colorThree):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorOne, colorTwo, colorThree)

	def 	updatePositionList(self, cub, colorOne, colorTwo, colorThree):
		return (self.checkerManager.three(cub, colorOne, colorTwo, colorThree))

	def 	moving(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
		# print("Moving three") ################################## delete
		self.listPositionCubOrigin = self.updatePositionList(self.cubOrigin, colorOne, colorTwo, colorThree)
		self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)
		if (self.checkSide(cubCurrent, colorOne, colorTwo, colorThree, face)) == True:
			# print ("Need to changeSide") ################################### delete
			self.moveSide(cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face)

	def 	checkSide(self, cubCurrent, colorOne, colorTwo, colorThree, face):
		# print("Origin ",self.listPositionCubOrigin) ################################## delete
		# print("Current ",self.listPositionCubCurrent)  ################################## delete
		if (face == "front"):
			return (self.checkDoubleSide(colorOne, colorTwo, colorThree, face, "right"))
		elif (face == "right"):
			return (self.checkDoubleSide(colorOne, colorTwo, colorThree, face, "back"))
		elif (face == "back"):
			return (self.checkDoubleSide(colorOne, colorTwo, colorThree, face, "left"))
		elif (face == "left"):
			return (self.checkDoubleSide(colorOne, colorTwo, colorThree, face, "front"))
		return False

	def 	checkDoubleSide(self, colorOne, colorTwo, colorThree, face, subFace):
		count = 0
		i = 0
		while (i < len(self.listPositionCubCurrent)):
			if (((self.listPositionCubCurrent[i][0]) == face) or ((self.listPositionCubCurrent[i][0]) == subFace)):
				count += 1
			i += 1
		return (count == 2)

	def 	moveSide(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
		while ((self.finishedThreeColorPosition(cubCurrent, colorOne, colorTwo, colorThree)) == False):
			if (face == "front"):
				cubCurrent.moveBackR()
				cubCurrent.moveBackD()
				cubCurrent.moveR()
				cubCurrent.moveD()
				solveMoveList.append("R'")
				solveMoveList.append("D'")
				solveMoveList.append("R")
				solveMoveList.append("D")
				print ("Front")
			elif (face == "right"):
				print ("right")
				cubCurrent.moveBackB()
				cubCurrent.moveBackD()
				cubCurrent.moveB()
				cubCurrent.moveD()
				solveMoveList.append("B'")
				solveMoveList.append("D'")
				solveMoveList.append("B")
				solveMoveList.append("D")
			elif (face == "back"):
				print ("Back")
				cubCurrent.moveBackL()
				cubCurrent.moveBackD()
				cubCurrent.moveL()
				cubCurrent.moveD()
				solveMoveList.append("L'")
				solveMoveList.append("D'")
				solveMoveList.append("L")
				solveMoveList.append("D")
			elif (face == "left"):
				print ("left")
				cubCurrent.moveBackF()
				cubCurrent.moveBackD()
				cubCurrent.moveF()
				cubCurrent.moveD()
				solveMoveList.append("F'")
				solveMoveList.append("D'")
				solveMoveList.append("F")
				solveMoveList.append("D")
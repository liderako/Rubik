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
			print ("True", "white", "green", "red")
		# if ((self.finishedThreeColorPosition(cubCurrent, "white", "red", "blue")) == False):
		# 	print ("True", "white", "red", "blue")
		# if ((self.finishedThreeColorPosition(cubCurrent, "white", "blue", "orange")) == False):
		# 	print ("True", "white", "blue", "orange")
		# if ((self.finishedThreeColorPosition(cubCurrent, "white", "orange", "green")) == False):
		# 	print ("True","white", "orange", "green")

	def finishedThreeColorPosition(self, cubCurrent, colorOne, colorTwo, colorThree):
		return checkPositionColor(self.cubOrigin, cubCurrent, colorOne, colorTwo, colorThree)
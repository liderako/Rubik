import sys
from src.object.algorithm.ManagerStepOne import *
from src.object.algorithm.ManagerStepTwo import *
from src.object.Cubik import *


class Algorithm:
	def __init__(self, cub):
		self.cub = cub
		self.solveMoveList = list()

	def 	run(self):
		cubOrigin = Cubik(3)

		managerStepOne = ManagerStepOne(cubOrigin)
		managerStepTwo = ManagerStepTwo(cubOrigin)

		managerStepOne.run(self.cub, self.solveMoveList)
		
		###
		self.cub.printCubik()
		print ("Solve Move")
		for x in self.solveMoveList:
			print (x, end=" ")
		print("")
		###
		managerStepTwo.run(self.cub, self.solveMoveList)

		###
		self.cub.printCubik()
		print ("Solve Move")
		for x in self.solveMoveList:
			print (x, end=" ")
		print("")
		###
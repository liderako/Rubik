import sys
from src.object.algorithm.ManagerStepOne import *
from src.object.algorithm.ManagerStepTwo import *
from src.object.algorithm.ManagerStepThree import *
from src.object.algorithm.ManagerStepFour import *
from src.object.algorithm.ManagerStepFive import *

from src.object.Cubik import *

class Algorithm:
	def __init__(self, cub):
		self.cub = cub
		self.solveMoveList = list()

	def 	run(self):
		cubOrigin = Cubik(3)

		managerStepOne = ManagerStepOne(cubOrigin)
		managerStepTwo = ManagerStepTwo(cubOrigin)
		managerStepThree = ManagerStepThree(cubOrigin)
		managerStepFour = ManagerStepFour()
		# managerStepFive = ManagerStepFive(cubOrigin)

		managerStepOne.run(self.cub, self.solveMoveList)
		
		# ###
		# print ("STEP ONE")
		# self.cub.printCubik()
		# print ("Solve Move")
		# for x in self.solveMoveList:
		# 	print (x, end=" ")
		# print("")
		# ###
		managerStepTwo.run(self.cub, self.solveMoveList)

		# ###
		# print ("STEP TWO")
		# self.cub.printCubik()
		# print ("Solve Move")
		# for x in self.solveMoveList:
		# 	print (x, end=" ")
		# print("")
		# ###
		managerStepThree.run(self.cub, self.solveMoveList)
		# ###
		# print ("STEP THREE")
		# self.cub.printCubik()
		# print ("Solve Move")
		# for x in self.solveMoveList:
		# 	print (x, end=" ")
		# print("")
		# ###
		
		managerStepFour.run(self.cub, self.solveMoveList)
		###
		print ("STEP FOUR")
		self.cub.printCubik()
		print ("Solve Move")
		for x in self.solveMoveList:
			print (x, end=" ")
		print("")
		###
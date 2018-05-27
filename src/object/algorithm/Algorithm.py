import sys
from src.object.algorithm.ManagerStepOne import *
from src.object.algorithm.ManagerStepTwo import *
from src.object.algorithm.ManagerStepThree import *
from src.object.algorithm.ManagerStepFour import *
from src.object.algorithm.ManagerStepFive import *
from src.object.algorithm.ManagerStepSix import *
from src.object.algorithm.ManagerStepSeven import *

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
		managerStepFive = ManagerStepFive(cubOrigin)
		managerStepSix = ManagerStepSix(cubOrigin)
		managerStepSeven = ManagerStepSeven(cubOrigin)
		
		managerStepOne.run(self.cub, self.solveMoveList)
		managerStepTwo.run(self.cub, self.solveMoveList)
		managerStepThree.run(self.cub, self.solveMoveList)
		managerStepFour.run(self.cub, self.solveMoveList)
		managerStepFive.run(self.cub, self.solveMoveList)
		managerStepSix.run(self.cub, self.solveMoveList)
		managerStepSeven.run(self.cub, self.solveMoveList)
		return (self.solveMoveList)
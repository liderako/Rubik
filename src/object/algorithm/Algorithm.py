import sys
from src.object.algorithm.ManagerStepOne import *
from src.object.Cubik import *


class Algorithm:
	def __init__(self, cub):
		self.cub = cub
		self.solveMoveList = list()

	def 	run(self):
		cubOrigin = Cubik(3)

		managerStepOne = ManagerStepOne(cubOrigin)
		managerStepOne.run(self.cub, self.solveMoveList)
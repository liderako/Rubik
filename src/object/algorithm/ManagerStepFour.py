import sys
from src.object.Cubik import *
from src.object.checkBackState import *

class ManagerStepFour:

	def 	run(self, cubCurrent, solveMoveList):
		one,two = checkBackState(cubCurrent.down, "yellow")

		print (one,two)
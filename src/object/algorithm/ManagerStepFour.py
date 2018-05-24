import sys
from src.object.Cubik import *
from src.object.checkBackState import *
from src.object.managers.MixManager import *
from src.appendListInList import appendListInList

class ManagerStepFour:

	def 	run(self, cubCurrent, solveMoveList):
		mixManager = MixManager()
		moveList = ["F", "L", "D", "L'", "D'", "F'"]

		one = 1
		two = 4
		# one,two = checkBackState(cubCurrent.down, "yellow")
		if (one == 4):
			return True
		if (one == 1):
			mixManager.mixRun(moveList, cubCurrent)
			appendListInList(solveMoveList, moveList)
		# 	one,two = checkBackState(cubCurrent.down, "yellow")
		if (one == 2 and two == 0):
			mixManager.mixRun(moveList, cubCurrent)
			appendListInList(solveMoveList, moveList)
		elif (one == 2 and two == 1):
			mixManager.mixRun(["D'", "F", "L", "D", "L'", "D'", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["D'", "F", "L", "D", "L'", "D'", "F'"])
		elif (one == 2 and two == 2):
			mixManager.mixRun(["D'", "D'", "F", "L", "D", "L'", "D'", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["D'", "D'", "F", "L", "D", "L'", "D'", "F'"])
		elif (one == 2 and two == 3):
			mixManager.mixRun(["D", "F", "L", "D", "L'", "D'", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["D", "F", "L", "D", "L'", "D'", "F'"])
		# one,two = checkBackState(cubCurrent.down, "yellow")
		if (one == 3 and two == 0):
			mixManager.mixRun(moveList, cubCurrent)
			appendListInList(solveMoveList, moveList)
		elif (one == 3 and two == 1):
			mixManager.mixRun(["D", "F", "L", "D", "L'", "D'", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["D", "F", "L", "D", "L'", "D'", "F'"])
		# one,two = checkBackState(cubCurrent.down, "yellow")
		if (one == 4):
			return True
		else:
			print ("what's happened")
			sys.exit(-1)
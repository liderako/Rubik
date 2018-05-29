import sys

def optimizationMove(solution):
    len = len(solution)
    i = 0
    newlst = []
    while (i > len):
        if (i + 2 < len):
            if (solution[i] == solution[i + 1] and solution[i + 2]):
            	
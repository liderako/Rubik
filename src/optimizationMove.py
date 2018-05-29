import sys

def optimizationMove(solution):
    lenOne = len(solution)
    i = 0
    newlst = []
    while (i < lenOne):
        f = 0
        if (i + 2 < lenOne):
            if (solution[i] == solution[i + 1] and solution[i + 1] == solution[i + 2]):
                if solution[i] == "F":
                    newlst.append("F'")
                elif solution[i] == "F'":
                    newlst.append("F")
                elif solution[i] == "R":
                    newlst.append("R'")
                elif solution[i] == "R'":
                    newlst.append("R")
                elif solution[i] == "U":
                    newlst.append("U'")
                elif solution[i] == "U'":
                    newlst.append("U")
                elif solution[i] == "B":
                    newlst.append("B'")
                elif solution[i] == "B'":
                    newlst.append("B")
                elif solution[i] == "L":
                    newlst.append("L'")
                elif solution[i] == "L'":
                    newlst.append("L")
                elif solution[i] == "D":
                    newlst.append("D'")
                elif solution[i] == "D'":
                    newlst.append("D")
                f = 1
                i += 2
        if f == 0:
            newlst.append(solution[i])
        i += 1
    return (newlst)

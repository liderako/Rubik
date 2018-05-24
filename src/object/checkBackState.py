import sys

def checkBackState(cubFace, color):

	if cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][2] == color and cubFace[1][0] == color and cubFace[2][1] == color:
		return (4, 0)
	elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[1][2] == color:
		return (3, 0)
	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[2][1] == color:
		return (3, 1)
	elif cubFace[2][1] == color and cubFace[1][1] == color and cubFace[1][2] == color:
		return (2, 0)
	elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[2][1] == color:
		return (2, 1)
	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][0] == color:
		return (2, 2)
	elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[1][2] == color:
		return (2, 3)
	elif cubFace[1][1] == color:
		return (1, 0)
	return False, False

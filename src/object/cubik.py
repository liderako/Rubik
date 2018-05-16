from colored import fg, bg, attr
import sys

class Cubik:

    def __init__( self, _size ):
        # colors: G - green, O - orange, W - white, Y - yellow, R - red, B - blue
        # list of rubic faces: Front, Back, Right, Left, Upper, Down
        faces = ['Front', 'Back', 'Right', 'Left', 'Upper', 'Down']
        #colors = ['green', 'yellow', 'red', 'orange', 'white', 'blue']
        #colors = ['red', 'orange', 'blue', 'green', 'white', 'yellow']
        colors = ['green', 'blue', 'red', 'orange',  'white', 'yellow']  #tested color
        #colors = ['green', 'blue', 'red', 'orange_4a',  'white', 'yellow']
        self.size = _size
        self.Front = self.listFill( colors[0], self.size )
        self.Back = self.listFill( colors[1], self.size )
        self.Right = self.listFill( colors[2], self.size )        
        self.Left = self.listFill( colors[3], self.size )
        self.Upper = self.listFill( colors[4], self.size )
        self.Down = self.listFill( colors[5], self.size )
        #self.Test = [['1', '2', '3', 'a'], ['4', '5', '6', 'b'], ['7', '8', '9', 'c'], ['10', '11', '12', 'd']]
        self.Test = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
#self.Test = [['1', '2'], ['3', '4']]

    def listFill(self, color, size ):
        list = []
        for row in range(size):
            string = []
            for column in range(size):
                string.append(color)
            list.append(string)
        return (list)

    # Back - apostrophe
    def moveU(self):
        buflst = self.Right[0]
        self.Right[0] = self.Back[0]
        self.Back[0] = self.Left[0]
        self.Left[0] = self.Front[0]
        self.Front[0] = buflst
        self.moveFace(self.Upper, 'u')

    def moveBackU(self):
        buflst = self.Right[0]
        self.Right[0] = self.Front[0]
        self.Front[0] = self.Left[0]
        self.Left[0] = self.Back[0]
        self.Back[0] = buflst
        self.moveFaceBack(self.Upper, 'u')

    def moveD(self):
        buflst = self.Right[self.size - 1]
        self.Right[self.size - 1] = self.Front[self.size - 1]
        self.Front[self.size - 1] = self.Left[self.size - 1]
        self.Left[self.size - 1] = self.Back[self.size - 1]
        self.Back[self.size - 1] = buflst
        self.moveFace(self.Down, 'd')

    def moveBackD(self):
        buflst = self.Right[self.size - 1]
        self.Right[self.size - 1] = self.Back[self.size - 1]
        self.Back[self.size - 1] = self.Left[self.size - 1]
        self.Left[self.size - 1] = self.Front[self.size - 1]
        self.Front[self.size - 1] = buflst
        self.moveFaceBack(self.Down, 'd')

    def moveR(self):
        for i in range(self.size):
            buflst = self.Down[i][self.size - 1]
            self.Down[i][self.size - 1] = self.Back[self.size - 1 - i][0]
            self.Back[self.size - 1 - i][0] = self.Upper[i][self.size - 1]
            self.Upper[i][self.size - 1] = self.Front[i][self.size - 1]
            self.Front[i][self.size - 1] = buflst
        self.moveFace(self.Right, 'r')

    def moveBackR(self):
        for i in range(self.size):
            buflst = self.Down[i][self.size - 1]
            self.Down[i][self.size - 1] = self.Front[i][self.size - 1]
            self.Front[i][self.size - 1] = self.Upper[i][self.size - 1]
            self.Upper[i][self.size - 1] = self.Back[self.size - 1 - i][0]
            self.Back[self.size - 1 - i][0] = buflst
        self.moveFaceBack(self.Right, 'r')

    def moveL(self):
        for i in range(self.size):
            buflst = self.Down[i][self.size - 1]
            self.Down[i][0] = self.Front[i][0]
            self.Front[i][0] = self.Upper[i][0]
            self.Upper[i][0] = self.Back[self.size - 1 - i][self.size - 1]
            self.Back[self.size - 1 - i][self.size - 1] = buflst
        self.moveFace(self.Left, 'l')

    def moveBackL(self):
        for i in range(self.size):
            buflst = self.Down[i][0]
            self.Down[i][0] = self.Back[self.size - 1 - i][self.size - 1]
            self.Back[self.size - 1 - i][self.size - 1] = self.Upper[i][0]
            self.Upper[i][0] = self.Front[i][0]
            self.Front[i][0] = buflst
        self.moveFaceBack(self.Left, 'l')

    def moveF(self):
        for i in range(self.size):
            buflst = self.Upper[self.size - 1][self.size - 1 - i]
            self.Upper[self.size - 1][self.size - 1 - i] = self.Left[i][self.size - 1]
            self.Left[i][self.size - 1] = self.Down[0][i]
            self.Down[0][i] = self.Right[self.size - 1 - i][0]
            self.Right[self.size - 1 - i][0] = buflst
        self.moveFace(self.Front, 'f')

    def moveBackF(self):
        for i in range(self.size):
            buflst = self.Upper[self.size - 1][i]
            self.Upper[self.size - 1][i] = self.Right[i][0]
            self.Right[i][0] = self.Down[0][self.size - 1 - i]
            self.Down[0][self.size - 1 - i] = self.Left[self.size - 1 - i][self.size - 1]
            self.Left[self.size - 1 - i][self.size - 1] = buflst
        self.moveFaceBack(self.Front, 'f')

    def moveB(self):
        for i in range(self.size):
            buflst = self.Upper[0][i]
            self.Upper[0][i] = self.Right[i][self.size - 1]
            self.Right[i][self.size - 1] = self.Down[self.size - 1][self.size - 1 - i]
            self.Down[self.size - 1][self.size - 1 - i] = self.Left[self.size - 1 - i][0]
            self.Left[self.size - 1 - i][0] = buflst
        self.moveFace(self.Back, 'b')

    def moveBackB(self):
        for i in range(self.size):
            buflst = self.Upper[0][self.size - 1 - i]
            self.Upper[0][self.size - 1 - i] = self.Left[i][0]
            self.Left[i][0] = self.Down[self.size - 1][i]
            self.Down[self.size - 1][i] = self.Right[self.size - 1 - i][self.size - 1]
            self.Right[self.size - 1 - i][self.size - 1] = buflst
        self.moveFaceBack(self.Back, 'b')

    def moveFace(self, face, g):
        nlist = [[x[i] for x in face] for i in range(len(face[0]))]
        for row in range(self.size):
            for col in range(self.size):
                if col >= int((self.size)/2):
                    break
                else:
                    buf = nlist[row][col]
                    nlist[row][col] = nlist[row][self.size - 1 - col]
                    nlist[row][self.size - 1 - col] = buf
        print ("Nl", nlist)
        if g == 'f':
            self.Front = nlist
        elif g == 'u':
            self.Upper = nlist
        elif g == 'd':
            self.Down = nlist
        elif g == 'l':
            self.Left = nlist
        elif g == 'r':
            self.Right = nlist
        elif g == 'b':
            self.Back = nlist

    def moveFaceBack(self, face, g):
        self.moveFace(face, g)
        if g == 'f':
            self.moveFace(self.Face, g)
            self.moveFace(self.Face, g)
        elif g == 'u':
            self.moveFace(self.Upper, g)
            self.moveFace(self.Upper, g)
        elif g == 'd':
            self.moveFace(self.Down, g)
            self.moveFace(self.Down, g)
        elif g == 'l':
            self.moveFace(self.Left, g)
            self.moveFace(self.Left, g)
        elif g == 'r':
            self.moveFace(self.Right, g)
            self.moveFace(self.Right, g)
        elif g == 'b':
            self.moveFace(self.Back, g)
            self.moveFace(self.Back, g)

 
    def getColor(self, color):
        if color == 'green':
            return 2
        if color == 'blue':
            return 4
        if color == 'red':
            return 1
        if color == 'orange':
            return 58
        if color == 'white':
            return 15
        if color == 'yellow':
            return 3


    def printCubik(self):
        for row in range(self.size):
            print ('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print ('     ', end='')
                print ('%s%s ### %s' % (fg(self.getColor(cub.Upper[row][col])), bg(0), attr('reset')), end='')
                space = False
        for row in range(self.size):
            print ('\n')
            for col in range(self.size):
                print ('%s%s ### %s' % (fg(self.getColor(cub.Left[row][col])), bg(0), attr('reset')), end='')
            for col in range(self.size):
                print ('%s%s ### %s' % (fg(self.getColor(cub.Front[row][col])), bg(0), attr('reset')), end='')
            for col in range(self.size):
                print ('%s%s ### %s' % (fg(self.getColor(cub.Right[row][col])), bg(0), attr('reset')), end='')
            for col in range(self.size):
                print ('%s%s ### %s' % (fg(self.getColor(cub.Back[row][col])), bg(0), attr('reset')), end='')
        for row in range(self.size):
            print ('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print ('     ', end='')
                print ('%s%s ### %s' % (fg(self.getColor(cub.Down[row][col])), bg(0), attr('reset')), end='')
                space = False
        print ('\n')

    def printCubikText(self):
        for row in range(self.size):
            print ('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print ('          ', end='')
                print ('[',cub.Upper[row][col],']', end='')
                space = False
        for row in range(self.size):
            print ('\n')
            for col in range(self.size):
                print ('[',cub.Left[row][col],']', end='')
            for col in range(self.size):
                print ('[',cub.Front[row][col],']', end='')
            for col in range(self.size):
                print ('[',cub.Right[row][col],']', end='')
            for col in range(self.size):
                print ('[',cub.Back[row][col],']', end='')
        for row in range(self.size):
            print ('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print ('          ', end='')
                print ('[',cub.Down[row][col],']', end='')
                space = False
        print ('\n')

cub = Cubik(3)
#cub.moveU()
#cub.moveR()
#cub.moveR()
cub.moveBackL()
#cub.moveL()
#cub.moveBackR()
#cub.moveBackD()
#cub.moveBackU()
#cub.moveU()
#cub.moveF()
cub.moveBackB()
#cub.moveBackF()
#cub.moveB()
cub.printCubik()
#cub.printCubikText()
#cub.moveFaceBack(cub.Test, 'b')
#print (cub.Back)
# !!!Problem Rback + Bback

# for i in range(3):
#     print ('%s%s ### %s' % (fg(1), bg(0), attr('reset')), end='')




#print ("Front ", cub.Front)
#print ("Upper ", cub.Upper)
#print ("Left ", cub.Left)
#print ("Back ", cub.Back)
#print ("Right ", cub.Right)
#print ("Down ", cub.Down)


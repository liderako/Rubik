from colored import fg, bg, attr
import hashlib
import sys

class Cubik:
    def __init__(self, _size):
        faces = ['Front', 'Back', 'Right', 'Left', 'Upper', 'Down']
        colors = ["green", "blue", "red", "orange", "white", "yellow"]
        self.colors = colors
        self.size = _size
        self.Front = self.listFill(colors[0], self.size)
        self.Back = self.listFill(colors[1], self.size)
        self.Right = self.listFill(colors[2], self.size)
        self.Left = self.listFill(colors[3], self.size)
        self.Upper = self.listFill(colors[4], self.size)
        self.Down = self.listFill(colors[5], self.size)
        self.Test = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.hash = ""
        self.mathHash()

    def mathHash(self):
        hashObj = hashlib.md5()
        string = ""
        i = 0
        while (i < self.size):
            j = 0
            while (j < self.size):
                string = string + self.Front[i][j]
                string = string + self.Back[i][j]
                string = string + self.Right[i][j]
                string = string + self.Left[i][j]
                string = string + self.Upper[i][j]
                string = string + self.Down[i][j]
                j += 1
            i += 1;
        hashObj.update(string.encode('utf-8'))
        self.hash = hashObj.hexdigest()

    def listFill(self, color, size):
        list = []
        for row in range(size):
            string = []
            for column in range(size):
                string.append(color)
            list.append(string)
        return (list)

    def moveU(self):
        buflst = self.Right[0]
        self.Right[0] = self.Back[0]
        self.Back[0] = self.Left[0]
        self.Left[0] = self.Front[0]
        self.Front[0] = buflst
        self.moveFront(self.Upper, 'u')

    def moveBackU(self):
        buflst = self.Right[0]
        self.Right[0] = self.Front[0]
        self.Front[0] = self.Left[0]
        self.Left[0] = self.Back[0]
        self.Back[0] = buflst
        self.moveFrontBack(self.Upper, 'u')

    def moveD(self):
        buflst = self.Right[self.size - 1]
        self.Right[self.size - 1] = self.Front[self.size - 1]
        self.Front[self.size - 1] = self.Left[self.size - 1]
        self.Left[self.size - 1] = self.Back[self.size - 1]
        self.Back[self.size - 1] = buflst
        self.moveFront(self.Down, 'd')

    def moveBackD(self):
        buflst = self.Right[self.size - 1]
        self.Right[self.size - 1] = self.Back[self.size - 1]
        self.Back[self.size - 1] = self.Left[self.size - 1]
        self.Left[self.size - 1] = self.Front[self.size - 1]
        self.Front[self.size - 1] = buflst
        self.moveFrontBack(self.Down, 'd')

    def moveR(self):
        for i in range(self.size):
            buflst = self.Down[i][self.size - 1]
            self.Down[i][self.size - 1] = self.Back[self.size - 1 - i][0]
            self.Back[self.size - 1 - i][0] = self.Upper[i][self.size - 1]
            self.Upper[i][self.size - 1] = self.Front[i][self.size - 1]
            self.Front[i][self.size - 1] = buflst
        self.moveFront(self.Right, 'r')

    def moveBackR(self):
        for i in range(self.size):
            buflst = self.Down[i][self.size - 1]
            self.Down[i][self.size - 1] = self.Front[i][self.size - 1]
            self.Front[i][self.size - 1] = self.Upper[i][self.size - 1]
            self.Upper[i][self.size - 1] = self.Back[self.size - 1 - i][0]
            self.Back[self.size - 1 - i][0] = buflst
        self.moveFrontBack(self.Right, 'r')

    def moveL(self):
        for i in range(self.size):
            buflst = self.Down[i][self.size - 1]
            self.Down[i][0] = self.Front[i][0]
            self.Front[i][0] = self.Upper[i][0]
            self.Upper[i][0] = self.Back[self.size - 1 - i][self.size - 1]
            self.Back[self.size - 1 - i][self.size - 1] = buflst
        self.moveFront(self.Left, 'l')

    def moveBackL(self):
        for i in range(self.size):
            buflst = self.Down[i][0]
            self.Down[i][0] = self.Back[self.size - 1 - i][self.size - 1]
            self.Back[self.size - 1 - i][self.size - 1] = self.Upper[i][0]
            self.Upper[i][0] = self.Front[i][0]
            self.Front[i][0] = buflst
        self.moveFrontBack(self.Left, 'l')

    def moveF(self):
        for i in range(self.size):
            buflst = self.Upper[self.size - 1][self.size - 1 - i]
            self.Upper[self.size - 1][self.size - 1 - i] = self.Left[i][self.size - 1]
            self.Left[i][self.size - 1] = self.Down[0][i]
            self.Down[0][i] = self.Right[self.size - 1 - i][0]
            self.Right[self.size - 1 - i][0] = buflst
        self.moveFront(self.Front, 'f')

    def moveBackF(self):
        for i in range(self.size):
            buflst = self.Upper[self.size - 1][i]
            self.Upper[self.size - 1][i] = self.Right[i][0]
            self.Right[i][0] = self.Down[0][self.size - 1 - i]
            self.Down[0][self.size - 1 - i] = self.Left[self.size - 1 - i][self.size - 1]
            self.Left[self.size - 1 - i][self.size - 1] = buflst
        self.moveFrontBack(self.Front, 'f')

    def moveB(self):
        for i in range(self.size):
            buflst = self.Upper[0][i]
            self.Upper[0][i] = self.Right[i][self.size - 1]
            self.Right[i][self.size - 1] = self.Down[self.size - 1][self.size - 1 - i]
            self.Down[self.size - 1][self.size - 1 - i] = self.Left[self.size - 1 - i][0]
            self.Left[self.size - 1 - i][0] = buflst
        self.moveFront(self.Back, 'b')

    def moveBackB(self):
        for i in range(self.size):
            buflst = self.Upper[0][self.size - 1 - i]
            self.Upper[0][self.size - 1 - i] = self.Left[i][0]
            self.Left[i][0] = self.Down[self.size - 1][i]
            self.Down[self.size - 1][i] = self.Right[self.size - 1 - i][self.size - 1]
            self.Right[self.size - 1 - i][self.size - 1] = buflst
        self.moveFrontBack(self.Back, 'b')

    def moveFront(self, Front, g):
        nlist = [[x[i] for x in Front] for i in range(len(Front[0]))]
        for row in range(self.size):
            for col in range(self.size):
                if col >= int((self.size) / 2):
                    break
                else:
                    buf = nlist[row][col]
                    nlist[row][col] = nlist[row][self.size - 1 - col]
                    nlist[row][self.size - 1 - col] = buf
        # print ("Nl", nlist)
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

    def moveFrontBack(self, Front, g):
        self.moveFront(Front, g)
        if g == 'f':
            self.moveFront(self.Front, g)
            self.moveFront(self.Front, g)
        elif g == 'u':
            self.moveFront(self.Upper, g)
            self.moveFront(self.Upper, g)
        elif g == 'd':
            self.moveFront(self.Down, g)
            self.moveFront(self.Down, g)
        elif g == 'l':
            self.moveFront(self.Left, g)
            self.moveFront(self.Left, g)
        elif g == 'r':
            self.moveFront(self.Right, g)
            self.moveFront(self.Right, g)
        elif g == 'b':
            self.moveFront(self.Back, g)
            self.moveFront(self.Back, g)

    def moveDoubleF(self):
        self.moveF()
        self.moveF()

    def moveDoubleB(self):
        self.moveB()
        self.moveB()

    def moveDoubleD(self):
        self.moveD()
        self.moveD()

    def moveDoubleR(self):
        self.moveR()
        self.moveR()

    def moveDoubleB(self):
        self.moveB()
        self.moveB()

    def moveDoubleL(self):
        self.moveL()
        self.moveL()

    def moveDoubleU(self):
        self.moveU()
        self.moveU()

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
            print('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print('     ', end='')
                print('%s%s ### %s' % (fg(self.getColor(self.Upper[row][col])), bg(0), attr('reset')), end='')
                space = False
        for row in range(self.size):
            print('\n')
            for col in range(self.size):
                print('%s%s ### %s' % (fg(self.getColor(self.Left[row][col])), bg(0), attr('reset')), end='')
            for col in range(self.size):
                print('%s%s ### %s' % (fg(self.getColor(self.Front[row][col])), bg(0), attr('reset')), end='')
            for col in range(self.size):
                print('%s%s ### %s' % (fg(self.getColor(self.Right[row][col])), bg(0), attr('reset')), end='')
            for col in range(self.size):
                print('%s%s ### %s' % (fg(self.getColor(self.Back[row][col])), bg(0), attr('reset')), end='')
        for row in range(self.size):
            print('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print('     ', end='')
                print('%s%s ### %s' % (fg(self.getColor(self.Down[row][col])), bg(0), attr('reset')), end='')
                space = False
        print('\n')

    def printCubikText(self):
        for row in range(self.size):
            print('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print('          ', end='')
                print('[', self.Upper[row][col], ']', end='')
                space = False
        for row in range(self.size):
            print('\n')
            for col in range(self.size):
                print('[', self.Left[row][col], ']', end='')
            for col in range(self.size):
                print('[', self.Front[row][col], ']', end='')
            for col in range(self.size):
                print('[', self.Right[row][col], ']', end='')
            for col in range(self.size):
                print('[', self.Back[row][col], ']', end='')
        for row in range(self.size):
            print('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print('          ', end='')
                print('[', self.Down[row][col], ']', end='')
                space = False
        print('\n')
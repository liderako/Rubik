from colored import fg, bg, attr
import sys
import hashlib

class Cubik:
    def __init__(self, size):
        faces = ['front', 'back', 'right', 'left', 'upper', 'down']
        colors = ["green", "blue", "red", "orange", "white", "yellow"]
        self.colors = colors
        self.size = size
        self.front = self.listFill(colors[0], self.size)
        self.back = self.listFill(colors[1], self.size)
        self.right = self.listFill(colors[2], self.size)
        self.left = self.listFill(colors[3], self.size)
        self.upper = self.listFill(colors[4], self.size)
        self.down = self.listFill(colors[5], self.size)
        self.hash = ""
        self.mathHash()

    def mathHash(self):
        hashObj = hashlib.md5()
        string = ""
        i = 0
        while (i < self.size):
            j = 0
            while (j < self.size):
                string = string + self.front[i][j]
                string = string + self.back[i][j]
                string = string + self.right[i][j]
                string = string + self.left[i][j]
                string = string + self.upper[i][j]
                string = string + self.down[i][j]
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
        buflst = self.right[0]
        self.right[0] = self.back[0]
        self.back[0] = self.left[0]
        self.left[0] = self.front[0]
        self.front[0] = buflst
        self.moveFront(self.upper, 'u')

    def moveBackU(self):
        buflst = self.right[0]
        self.right[0] = self.front[0]
        self.front[0] = self.left[0]
        self.left[0] = self.back[0]
        self.back[0] = buflst
        self.moveFrontBack(self.upper, 'u')

    def moveD(self):
        buflst = self.right[self.size - 1]
        self.right[self.size - 1] = self.front[self.size - 1]
        self.front[self.size - 1] = self.left[self.size - 1]
        self.left[self.size - 1] = self.back[self.size - 1]
        self.back[self.size - 1] = buflst
        self.moveFront(self.down, 'd')

    def moveBackD(self):
        buflst = self.right[self.size - 1]
        self.right[self.size - 1] = self.back[self.size - 1]
        self.back[self.size - 1] = self.left[self.size - 1]
        self.left[self.size - 1] = self.front[self.size - 1]
        self.front[self.size - 1] = buflst
        self.moveFrontBack(self.down, 'd')

    def moveR(self):
        for i in range(self.size):
            buflst = self.down[i][self.size - 1]
            self.down[i][self.size - 1] = self.back[self.size - 1 - i][0]
            self.back[self.size - 1 - i][0] = self.upper[i][self.size - 1]
            self.upper[i][self.size - 1] = self.front[i][self.size - 1]
            self.front[i][self.size - 1] = buflst
        self.moveFront(self.right, 'r')

    def moveBackR(self):
        for i in range(self.size):
            buflst = self.down[i][self.size - 1]
            self.down[i][self.size - 1] = self.front[i][self.size - 1]
            self.front[i][self.size - 1] = self.upper[i][self.size - 1]
            self.upper[i][self.size - 1] = self.back[self.size - 1 - i][0]
            self.back[self.size - 1 - i][0] = buflst
        self.moveFrontBack(self.right, 'r')

    def moveL(self):
        for i in range(self.size):
            buflst = self.down[i][0]
            self.down[i][0] = self.front[i][0]
            self.front[i][0] = self.upper[i][0]
            self.upper[i][0] = self.back[self.size - 1 - i][self.size - 1]
            self.back[self.size - 1 - i][self.size - 1] = buflst
        self.moveFront(self.left, 'l')

    def moveBackL(self):
        for i in range(self.size):
            buflst = self.down[i][0]
            self.down[i][0] = self.back[self.size - 1 - i][self.size - 1]
            self.back[self.size - 1 - i][self.size - 1] = self.upper[i][0]
            self.upper[i][0] = self.front[i][0]
            self.front[i][0] = buflst
        self.moveFrontBack(self.left, 'l')

    def moveF(self):
        for i in range(self.size):
            buflst = self.upper[self.size - 1][self.size - 1 - i]
            self.upper[self.size - 1][self.size - 1 - i] = self.left[i][self.size - 1]
            self.left[i][self.size - 1] = self.down[0][i]
            self.down[0][i] = self.right[self.size - 1 - i][0]
            self.right[self.size - 1 - i][0] = buflst
        self.moveFront(self.front, 'f')

    def moveBackF(self):
        for i in range(self.size):
            buflst = self.upper[self.size - 1][i]
            self.upper[self.size - 1][i] = self.right[i][0]
            self.right[i][0] = self.down[0][self.size - 1 - i]
            self.down[0][self.size - 1 - i] = self.left[self.size - 1 - i][self.size - 1]
            self.left[self.size - 1 - i][self.size - 1] = buflst
        self.moveFrontBack(self.front, 'f')

    def moveB(self):
        for i in range(self.size):
            buflst = self.upper[0][i]
            self.upper[0][i] = self.right[i][self.size - 1]
            self.right[i][self.size - 1] = self.down[self.size - 1][self.size - 1 - i]
            self.down[self.size - 1][self.size - 1 - i] = self.left[self.size - 1 - i][0]
            self.left[self.size - 1 - i][0] = buflst
        self.moveFront(self.back, 'b')

    def moveBackB(self):
        for i in range(self.size):
            buflst = self.upper[0][self.size - 1 - i]
            self.upper[0][self.size - 1 - i] = self.left[i][0]
            self.left[i][0] = self.down[self.size - 1][i]
            self.down[self.size - 1][i] = self.right[self.size - 1 - i][self.size - 1]
            self.right[self.size - 1 - i][self.size - 1] = buflst
        self.moveFrontBack(self.back, 'b')

    def moveFront(self, front, g):
        nlist = [[x[i] for x in front] for i in range(len(front[0]))]
        for row in range(self.size):
            for col in range(self.size):
                if col >= int((self.size) / 2):
                    break
                else:
                    buf = nlist[row][col]
                    nlist[row][col] = nlist[row][self.size - 1 - col]
                    nlist[row][self.size - 1 - col] = buf
        if g == 'f':
            self.front = nlist
        elif g == 'u':
            self.upper = nlist
        elif g == 'd':
            self.down = nlist
        elif g == 'l':
            self.left = nlist
        elif g == 'r':
            self.right = nlist
        elif g == 'b':
            self.back = nlist

    def moveFrontBack(self, front, g):
        self.moveFront(front, g)
        if g == 'f':
            self.moveFront(self.front, g)
            self.moveFront(self.front, g)
        elif g == 'u':
            self.moveFront(self.upper, g)
            self.moveFront(self.upper, g)
        elif g == 'd':
            self.moveFront(self.down, g)
            self.moveFront(self.down, g)
        elif g == 'l':
            self.moveFront(self.left, g)
            self.moveFront(self.left, g)
        elif g == 'r':
            self.moveFront(self.right, g)
            self.moveFront(self.right, g)
        elif g == 'b':
            self.moveFront(self.back, g)
            self.moveFront(self.back, g)

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

    def moveDoubleL(self):
        self.moveL()
        self.moveL()

    def moveDoubleU(self):
        self.moveU()
        self.moveU()

    @staticmethod
    def getColor(color):
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
                print('%s%s ### %s' % (fg(self.getColor(self.upper[row][col])), bg(0), attr('reset')), end='')
                space = False
        for row in range(self.size):
            print('\n')
            for col in range(self.size):
                print('%s%s ### %s' % (fg(self.getColor(self.left[row][col])), bg(0), attr('reset')), end='')
            for col in range(self.size):
                print('%s%s ### %s' % (fg(self.getColor(self.front[row][col])), bg(0), attr('reset')), end='')
            for col in range(self.size):
                print('%s%s ### %s' % (fg(self.getColor(self.right[row][col])), bg(0), attr('reset')), end='')
            for col in range(self.size):
                print('%s%s ### %s' % (fg(self.getColor(self.back[row][col])), bg(0), attr('reset')), end='')
        for row in range(self.size):
            print('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print('     ', end='')
                print('%s%s ### %s' % (fg(self.getColor(self.down[row][col])), bg(0), attr('reset')), end='')
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
                print('[', self.upper[row][col], ']', end='')
                space = False
        for row in range(self.size):
            print('\n')
            for col in range(self.size):
                print('[', self.left[row][col], ']', end='')
            for col in range(self.size):
                print('[', self.front[row][col], ']', end='')
            for col in range(self.size):
                print('[', self.right[row][col], ']', end='')
            for col in range(self.size):
                print('[', self.back[row][col], ']', end='')
        for row in range(self.size):
            print('\n')
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print('          ', end='')
                print('[', self.down[row][col], ']', end='')
                space = False
        print('\n')

import numpy as np
import pandas as pd
from termcolor import colored
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
        #size.Front = fill_list( colors[0], _size )
        self.Front = self.fill_list( colors[0], self.size )
        self.Back = self.fill_list( colors[1], self.size )
        self.Right = self.fill_list( colors[2], self.size )        
        self.Left = self.fill_list( colors[3], self.size )
        self.Upper = self.fill_list( colors[4], self.size )
        self.Down = self.fill_list( colors[5], self.size )
        #print (self.Front[1][1])

    def fill_list(self, color, size ):
        list = []
        for row in range(size):
            string = []
            for column in range(size):
                string.append(color)
            list.append(string)
        return (list)

    #apostrophe
    def moveU(self):
        buflst = self.Right[0]
        self.Right[0] = self.Back[0]
        self.Back[0] = self.Left[0]
        self.Left[0] = self.Front[0]
        self.Front[0] = buflst

    def moveUapostrophe(self):
        buflst = self.Right[0]
        self.Right[0] = self.Front[0]
        self.Front[0] = self.Left[0]
        self.Left[0] = self.Back[0]
        self.Back[0] = buflst

    def moveD(self):
        buflst = self.Right[self.size - 1]
        self.Right[self.size - 1] = self.Front[self.size - 1]
        self.Front[self.size - 1] = self.Left[self.size - 1]
        self.Left[self.size - 1] = self.Back[self.size - 1]
        self.Back[self.size - 1] = buflst

    def moveDapostrophe(self):
        buflst = self.Right[self.size - 1]
        self.Right[self.size - 1] = self.Back[self.size - 1]
        self.Back[self.size - 1] = self.Left[self.size - 1]
        self.Left[self.size - 1] = self.Front[self.size - 1]
        self.Front[self.size - 1] = buflst

    def moveR(self):
        for i in range(self.size):
            buflst = self.Down[i][self.size - 1]
            self.Down[i][self.size - 1] = self.Back[self.size - 1 - i][0]
            self.Back[self.size - 1 - i][0] = self.Upper[i][self.size - 1]
            self.Upper[i][self.size - 1] = self.Front[i][self.size - 1]
            self.Front[i][self.size - 1] = buflst

    def moveRapostrophe(self):
        for i in range(self.size):
            buflst = self.Down[i][self.size - 1]
            self.Down[i][self.size - 1] = self.Front[i][self.size - 1]
            self.Front[i][self.size - 1] = self.Upper[i][self.size - 1]
            self.Upper[i][self.size - 1] = self.Back[self.size - 1 - i][0]
            self.Back[self.size - 1 - i][0] = buflst

    def moveL(self):
        for i in range(self.size):
            buflst = self.Down[i][self.size - 1]
            self.Down[i][0] = self.Front[i][0]
            self.Front[i][0] = self.Upper[i][0]
            self.Upper[i][0] = self.Back[self.size - 1 - i][self.size - 1]
            self.Back[self.size - 1 - i][self.size - 1] = buflst

    def moveLapostrophe(self):
        for i in range(self.size):
            buflst = self.Down[i][0]
            self.Down[i][0] = self.Back[self.size - 1 - i][self.size - 1]
            self.Back[self.size - 1 - i][self.size - 1] = self.Upper[i][0]
            self.Upper[i][0] = self.Front[i][0]
            self.Front[i][0] = buflst

    def moveF(self):
        for i in range(self.size):
            buflst = self.Upper[self.size - 1][self.size - 1 - i]
            self.Upper[self.size - 1][self.size - 1 - i] = self.Left[i][self.size - 1]
            self.Left[i][self.size - 1] = self.Down[0][i]
            self.Down[0][i] = self.Right[self.size - 1 - i][0]
            self.Right[self.size - 1 - i][0] = buflst

    def moveFapostrophe(self):
        for i in range(self.size):
            buflst = self.Upper[self.size - 1][i]
            self.Upper[self.size - 1][i] = self.Right[i][0]
            self.Right[i][0] = self.Down[0][self.size - 1 - i]
            self.Down[0][self.size - 1 - i] = self.Left[self.size - 1 - i][self.size - 1]
            self.Left[self.size - 1 - i][self.size - 1] = buflst

    def moveB(self):
        for i in range(self.size):
            buflst = self.Upper[0][i]
            self.Upper[0][i] = self.Right[i][self.size - 1]
            self.Right[i][self.size - 1] = self.Down[self.size - 1][self.size - 1 - i]
            self.Down[self.size - 1][self.size - 1 - i] = self.Left[self.size - 1 - i][0]
            self.Left[self.size - 1 - i][0] = buflst

    def moveBapostrophe(self):
        for i in range(self.size):
            buflst = self.Upper[0][self.size - 1 - i]
            self.Upper[0][self.size - 1 - i] = self.Left[i][0]
            self.Left[i][0] = self.Down[self.size - 1][i]
            self.Down[self.size - 1][i] = self.Right[self.size - 1 - i][self.size - 1]
            self.Right[self.size - 1 - i][self.size - 1] = buflst

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
            print '\n'
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print ('     '),
                print ('%s%s ### %s' % (fg(self.getColor(cub.Upper[row][col])), bg(0), attr('reset'))),
                space = False
        for row in range(self.size):
            print '\n'
            for col in range(self.size):
                print ('%s%s ### %s' % (fg(self.getColor(cub.Left[row][col])), bg(0), attr('reset'))),
            for col in range(self.size):
                print ('%s%s ### %s' % (fg(self.getColor(cub.Front[row][col])), bg(0), attr('reset'))),
            for col in range(self.size):
                print ('%s%s ### %s' % (fg(self.getColor(cub.Right[row][col])), bg(0), attr('reset'))),
            for col in range(self.size):
                print ('%s%s ### %s' % (fg(self.getColor(cub.Back[row][col])), bg(0), attr('reset'))),
        for row in range(self.size):
            print '\n'
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print ('     '),
                print ('%s%s ### %s' % (fg(self.getColor(cub.Down[row][col])), bg(0), attr('reset'))),
                space = False

cub = Cubik(3)
#cub.moveU()
#cub.moveR()
#cub.moveR()
#cub.moveLapostrophe()
#cub.moveRapostrophe()
#cub.moveDapostrophe()
#cub.moveUapostrophe()
#cub.moveF()
#cub.moveBapostrophe()
#cub.moveFapostrophe()
#cub.moveB()
cub.printCubik()
# for i in range(3):
#      print colored(' ### ', '#C0C0C0'),


#print colorsBack.G + "###" + colorsBack.ENDC
#print cub.Front[0][0]
#print colored('hello', cub.Front[0][0]), colored('world', cub.Front[0][0])


#print "Front ", cub.Front
#print "Upper ", cub.Upper
#print "Left ", cub.Left
#print "Back ", cub.Back
#print "Right ", cub.Right
#print "Down ", cub.Down

    # def printCubik(self):
    #     for row in range(self.size):
    #         print '\n'
    #         space = True
    #         for col in range(self.size):
    #             if space:
    #                 for i in range(self.size):
    #                     print ('     '),
    #             print ('%s%s ### %s' % (fg(getColor(cub.Upper[row][col])), bg(0), attr('reset'))),
    #             space = False
    #     for row in range(self.size):
    #         print '\n'
    #         for col in range(self.size):
    #             print colored(' ### ', cub.Left[row][col]),
    #         for col in range(self.size):
    #             print colored(' ### ', cub.Front[row][col]),
    #         for col in range(self.size):
    #             print colored(' ### ', cub.Right[row][col]),
    #         for col in range(self.size):
    #             print colored(' ### ', cub.Back[row][col]),
    #     for row in range(self.size):
    #         print '\n'
    #         space = True
    #         for col in range(self.size):
    #             if space:
    #                 for i in range(self.size):
    #                     print ('     '),
    #             print colored(' ### ', cub.Down[row][col]),
    #             space = False

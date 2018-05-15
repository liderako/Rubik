import sys
import re

from src.errorExit import *

class   ValidationManager:

    def __init__(self, readBuffer):
        self.readBuffer = readBuffer


    def run(self):
        self.validationSizeContainer()
        self.validationLen()
        self.validationSymbol()
        self.validationSizeSymbol()

    def     validationLen(self):
        string = self.readBuffer.split('\n')
        if (len(string) != 1):
            error("need one line")

    def     validationSizeContainer(self):
        string = self.readBuffer.split(' ')
        for x in string:
            if (len(x) == 0):
                error("Invalid space")
            if (len(x) > 2):
                error("Invalid container too much symbol")

    def validationSymbol(self):
        string = self.readBuffer.split(' ')
        for x in string:
            match = re.search(r'[^FBRLUD2\']', x)
            if (match):
                error("Unknow symbol")

    def validationSizeSymbol(self):
        string = self.readBuffer.split(' ')
        for x in string:
            match = re.search(r'[A-Z]+', x)
            if (match == None):
                error("Need one char")
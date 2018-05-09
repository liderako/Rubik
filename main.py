import sys
from src import *

if (len(sys.argv) != 2):
    print "Usage: main.py filename"
    sys.exit(1)
else:
    print readFile(argv[1])


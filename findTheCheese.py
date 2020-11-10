"""

The main algorithm for the mouse in the maze should be written in this file

"""
# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')
from logic import *
from graphics import moveForward, turnLeft, turnRight, lookAhead, lookLeft, lookRight, eatCheese, mazeDebugOn, mazeDebugOff


# Take at most one "moveForward" step, and in any case always do _something_ that might be useful
def oneStepToCheese():
    if (lookAhead()==""):
	moveForward()
    else:
	turnRight()

# Repeatedly use the above function to get the mouse to move around the maze,
#   and, when possible (i.e. when lookAhead() is "c") eat the cheese.

def moveToCheese():
    print "You need to replace this print statement in moveToCheese" 

def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()

"""

The main algorithm for the mouse in the maze should be written in this file.

We don't have a good way to

"""
from Logic import *
from graphics import moveForward, turnLeft, turnRight, lookAhead, lookLeft, lookRight, eatCheese, mazeDebugOn, mazeDebugOff


# Take at most one "moveForward" step, and in any case always do _something_ that might be useful
def oneStepToCheese():
    if lookAhead()=="":
        moveForward()
    else:
        turnRight()


# Repeatedly use the above function to get the mouse to move around the maze,
#   and, when possible (i.e. when lookAhead() is "c") eat the cheese.
def moveToCheese():
    print("You need to replace this print statement in moveToCheese")


"""

Common doctest stuff for a fresh cs105 project.

Typically this file would be renamed via "git mv" to be the main test of the project.

>>> 6*7
42

>>> times(6, 7)
42

"""

from Logic import *

def times(x: float, y: float) -> float:
    precondition(x==6)
    return x*y


#############################################################################################
# The following gets the DocTest system to check test cases in the documentation comments.  #
# In most Haverford CS course, you won't need to modify the stuff below.                    #
#############################################################################################

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Congratulations! You have passed all "+str(result[1])+" tests"))
    else:
        print("Rats!")

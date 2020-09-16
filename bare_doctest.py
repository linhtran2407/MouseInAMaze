"""

Common doctest stuff for a fresh cs105 project.

Typically this file would be renamed via "git mv" to be the main test of the project.

>>> 6*7
42

"""

# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print("*** Can't find logic.py in /home/courses/python, resorting to basic logic_basic.py in the project")
    print("*** If this happens in the CS teaching lab, tell your instructor")
    try:
        from logic_basic import *
    except:
        print("Can't find logic.py in /home/courses/python, and missing logic_basic.py")
        print("   This shouldn't happen in CS projects; if it does, and you need to keep working")
        print("   You could add a logic_basic and define, e.g., a function 'precondition' that does nothing")
        sys.exit(1)




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

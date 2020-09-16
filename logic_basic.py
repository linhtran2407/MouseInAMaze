"""

This file is designed to let the Haverford CS projects that use the core features
 of the Haverford logic.py, namely 'precondition' and 'postcondition',
 work in a basic way, even if the full logic.py is not available.

"""

def precondition(value_of_precondition):
	if (value_of_precondition != True):
		raise "Precondition failed"

def postcondition(value_of_postcondition):
	if (value_of_postcondition != True):
		raise "Postcondition failed"

def assertion(value_of_assertion):
	if (value_of_assertion != True):
		raise "Assertion failed"

def loopInvariant(value_of_loop_invariant):
	if value_of_loop_invariant != True:
		raise "Loop Invariant Failed"




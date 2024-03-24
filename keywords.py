
from util import *

ALL_KEYWORDS = ["PRINT", "GOTO"]

#KEYWORD_FUNCTIONS = [PRINT, GOTO]

def attach_keywords(program): # This adds all of the handlers to the program "program".




	#setattr(Foo, 'print_v', my_new_method)
	setattr(program, "PRINT", PRINT) # Add the method.
	# Add the string to keyword_handlers
	program.keyword_handlers["PRINT"] = program.PRINT # Add the function to the keword handler stuff.


def PRINT(self, tokens):

	argument_string = " ".join(tokens)
	# Parse the arguments to this function.
	print("Here is the argument string: "+str(argument_string))
	arguments = parse_args(argument_string)
	# Print the values.
	for arg in arguments:
		if arg[0]: # Variable
			if arg[1] not in self.variables:
				# Undefined variable
				fail("Undefined variable: "+str(arg))
			# Get variable value and stringify it.
			str_value = stringify(self.variables[arg[1]])
			# Actually print it.
			print(str_value, end="")
		else: # Just a raw string.
			print(arg[1], end="")
	# Print newline.
	print("\n", end="")
	return

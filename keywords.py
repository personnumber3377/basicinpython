
from util import *

ALL_KEYWORDS = ["PRINT", "GOTO"]

#KEYWORD_FUNCTIONS = [PRINT, GOTO]

def attach_keywords(program): # This adds all of the handlers to the program "program".




	#setattr(Foo, 'print_v', my_new_method)
	setattr(program, "PRINT", PRINT) # Add the method.
	# Add the string to keyword_handlers
	program.keyword_handlers["PRINT"] = program.PRINT # Add the function to the keword handler stuff.

	setattr(program, "GOTO", GOTO)

	program.keyword_handlers["GOTO"] = program.GOTO

def PRINT(self, tokens):

	argument_string = " ".join(tokens)
	# Parse the arguments to this function.
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

def GOTO(self, tokens):
	if len(tokens) != 1:
		fail("GOTO takes only one argument. The line number")
	# Check that the argument is actually an integer.
	line_num = tokens[0]
	if not line_num.isnumeric():
		fail("Line number passed to GOTO must actually be a number, not variable or something else.")
	# Convert to an actual python integer
	line_num = int(line_num)
	# The line number must be in the program line numbers.
	if line_num not in self.linenums:
		fail("GOTO line number isn't a line number of the program.")
	# Set line number and set the variable, which specifies if we have jumped
	self.jumped = True
	# This is quite a wonky way of doing things. Maybe we should refactor this to be a bit better
	self.cur_line_num_index = self.line_num_to_index[line_num]
	return

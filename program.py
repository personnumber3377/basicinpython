
from util import * # needed for the fail function.

# Implements the main program class

class BasicProgram:
	def __init__(self):
		self.lines = {} # line num as key and the program line as value.
		self.linenums = [] # List of valid program line numbers.
	def load(self, filename) -> None:
		# Loads program from file
		fh = open(filename, "r")
		lines = fh.readlines()
		fh.close()
		self.parse_lines(lines)
	def parse_lines(self, lines) -> None: # Parses all of the program lines.
		for line in lines:
			# Split on spaces
			tokens = line.split(" ")
			linenum = tokens[0]
			program_line = ''.join(tokens[1:])
			# The line number should actually be a number
			if not linenum.isnumeric():
				fail("The line number must actually be number: "+str(line))
			linenum = int(linenum)




from util import * # needed for the fail function.

# Implements the main program class

class BasicProgram:
	def __init__(self):
		self.lines = {} # line num as key and the program line as value.
		self.linenums = set() # List of valid program line numbers.
		self.prev_line_num = None
		# This is made a lot more complex, because the line numbers can be almost anything, as long as they are increasing in order.
		self.linenums_as_list = [] # We iterate over this line when running the program. We iterate over this list, because then we do not need to search the linenums set for the next line.
		self.cur_line_num_index = 0 # Index into the linenums_as_list array which specifies the current line.
	def load(self, filename) -> None:
		# Loads program from file
		fh = open(filename, "r")
		lines = fh.readlines()
		fh.close()
		self.parse_lines(lines)
	def load_string(self, program_string) -> None: # Load program as string.
		lines = program_string.split("\n")
		self.parse_lines(lines)
	def parse_lines(self, lines) -> None: # Parses all of the program lines.
		for line in lines:
			# Split on spaces
			tokens = line.split(" ")
			linenum = tokens[0]
			program_line = ' '.join(tokens[1:])
			# The line number should actually be a number
			if not linenum.isnumeric():
				fail("The line number must actually be number: "+str(line))
			linenum = int(linenum)
			# The next number must be greater than the previous line number.
			if self.prev_line_num and linenum < self.prev_line_num:
				fail("Line numbers must be in increasing order!")
			self.linenums.add(linenum)
			self.linenums_as_list.append(linenum)
			self.lines[linenum] = program_line
	def parse_line(self, line: str) -> tuple: # This returns a tuple of the form (LINE_TYPE, OPERATOR, arguments...) (all line types are defined in expressions.py)

		# Check the keyword first.
		return # Stub for now

	def run_program(self) -> None: # Run the program.

		#program_line = self.linenums_as_list[0] # Get the first line.

		while True: # Main program loop.
			# Get tokens from current line.
			cur_line = self.lines[self.linenums_as_list[self.cur_line_num_index]]
			print(cur_line)

# Infinite hello world source code.
example_source = """10 PRINT \"HELLO WORLD\"
20 GOTO 10"""

def main() -> int: # Driver code.
	prog = BasicProgram()
	# Open program
	prog.load_string(example_source)
	# Run the program
	prog.run_program()

	return 0

if __name__=="__main__":
	exit(main())



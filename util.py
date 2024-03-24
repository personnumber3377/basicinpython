


STRING_DEF_CHAR = "\""

ARG_SEP_CHARS = [",", ";"] # These characters can be used to split arguments to PRINT for example.

def fail(string: str) -> None: # Failure
	print("[ERROR] "+str(string))
	exit(1)

def parse_args(string: str) -> list: # Parses the string to tokens and variables. (This is used by the PRINT function in keywords.py)

	out_list = [] # A list of tuples. the first value in each tuple is if it is a variable (1 means it is a variable) and the second value is the actual value.
	currently_in_string = False # If we are inside a string statement.
	currently_in_variable_name = False
	string_start_index = None
	var_start_index = None
	skip = None # Skip forward by this amount of characters

	for i, char in enumerate(string):
		# Check if we are currently skipping characters
		if skip:
			skip -= 1
			continue

		if char == STRING_DEF_CHAR: # Start or end of string found.
			if currently_in_string:
				# We closed a string. append this string to the list
				out_list.append((0, string[string_start_index:i])) # zero means that the the value is a string literal
				
				# The character after the string must be "," or ";"
				if i == len(string)-1: # The line ends in a double quote character
					currently_in_string = False
					continue
				if string[i+1] not in ARG_SEP_CHARS:
					fail("Must separate arguments with \",\" or \";\" !")

				skip = 1 # Skip atleast the next character. ("," or ";")
				# Count the whitespaces after the "," or ";" character.

				while string[skip+i+1] == " ": # Skip whitespace
					skip += 1
				# We are no longer in string
				currently_in_string = False
				continue
			else:
				# Start of string.
				currently_in_string = True
				string_start_index = i+1 # The current character is a double quote character, skip over it.
				continue

		if currently_in_string: # Just a part of string.
			continue

		if char == " ":
			if currently_in_variable_name:
				# End of variable without "," or ";" character. Invalid.
				fail("Must separate arguments with \",\" or \";\" !")
			# Skip over whitespace
			continue

		# Part of variable name.
		if not currently_in_variable_name: # Start of new variable.
			var_start_index = i
			currently_in_variable_name = True
			continue
		else:
			# end of variable name (also check for end of line)
			if char in ARG_SEP_CHARS or i == len(string)-1:
				currently_in_variable_name = False
				variable_name = string[var_start_index:i]
				out_list.append((1, variable_name)) # 1 means variable name
				skip = 0
				while string[i+1+skip] == " ": # Skip over whitespace
					skip += 1
	# Check for end of variable too.
	if currently_in_variable_name:
		out_list.append((1, string[var_start_index:]))
	# String wasn't closed properly
	if currently_in_string:
		fail("Unclosed string!")
	return out_list

VALUE_FLOAT_DETERMINING = 0.01

def stringify(value) -> str: # Returns the string representation of a value.
	# Check for normal integer.
	if isinstance(value, float) and value % 1.0 <= VALUE_FLOAT_DETERMINING:
		# Return as integer
		actual_val = round(value)
		return str(actual_val)
	if isinstance(value, str): # If value is actually a string, just return that string.
		return value


def test_argument_parser() -> None:
	example_string = "\"VALUE OF X: \"; X" # Example program line: PRINT "VALUE OF X: "; X
	res = parse_args(example_string)
	assert res == [(0, "VALUE OF X: "), (1, "X")] # Tokens.
	example_string = "X; Y; Z" # Test multiple variables in a row.
	res = parse_args(example_string)
	assert res == [(1, "X"), (1, "Y"), (1, "Z")]
	# Test just a simple string.
	example_string = "\"SAMPLETEXT\""
	res = parse_args(example_string)
	assert res == [(0, "SAMPLETEXT")]
	print("test_argument_parser passed!")
	return

def main() -> int:
	# Run tests.
	test_argument_parser()
	print("All tests passed!")
	return 0

if __name__=="__main__":
	exit(main())

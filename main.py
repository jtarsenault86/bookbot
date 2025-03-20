# mandatory imports
import sys
from stats import *

# take filepath as input and returns text of file
def get_book_test(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

# the program's main function
def main():

	if (len(sys.argv) < 2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	# initial variable declarations
	file_path = sys.argv[1]
	file_contents = ""
	words = 0
	char_dict = {}

	# retrieving a text and relevant info gathering
	file_contents = get_book_test(file_path)
	words = word_count(file_contents)
	char_dict = char_count(file_contents)

	# printing text information
	print("============ BOOKBOT ============\n")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print(f"Found {words} total words\n")
	print("--------- Character Count -------")
	thing = sort_dict(char_dict)
	for t in thing:
		print(f"{t[0]}: {t[1]}")
	print("============= END ===============")

# program commences here
main()

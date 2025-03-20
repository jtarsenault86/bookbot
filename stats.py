#takes string input and returns integer number of words in string
def word_count(file_contents):
        list_words = []
        count = 0
        list_words = file_contents.split()
        for word in list_words:
                count += 1
        return count

# returns number of times each character appears in a text
def char_count(file_contents):

	alphabet = "abcdefghijklmnopqrstuvwxyzæâêëô"
	working_string = ""
	char= ''
	count = 0
	char_dict = {char:count}
	working_string = file_contents.lower()

	for char in alphabet:
		count = 0
		for c in working_string:
			if (c==char):
				count += 1
		char_dict.update({char:count})

	return char_dict

# sorts the dictionary

def sort_dict(dict):
	sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
	return sorted_dict

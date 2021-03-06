# my git changed Unix line end \n with Windows line end \r\n
# script cleans pickle file


import pickle



words_file = "../tools/word_data.pkl"
authors_file="../tools/email_authors.pkl"



original = "../tools/word_data.pkl"
destination = "../tools/word_data_unix.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
	content = infile.read()
with open(destination, 'wb') as output:
	for line in content.splitlines(): # adding \n to every line
		outsize += len(line) + 1
		output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content)-outsize))


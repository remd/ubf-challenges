#! /usr/bin/python
# remd
# 6/23/12
#
# file.py
#
# Reads a languages file, does some parsing, writes an output file.
# Numbers the output file starting from 0. i.e. 0, 1, 2, etc.
# Then adds more text to source languages file.
# 
# Targets src.txt to hide 'working' file from git repository.

def main():
	try:
		f = open('src.txt', 'r')
	except IOError:
		print "Could not open \"src.txt\"."

	try:
		newFile = open('out.txt', 'w')
	except IOError:
		print "Could not open \"out.txt\"."
		
	lineNumber = 0
	totalLines = 0
	for line in f:
		totalLines += 1
		language = line.split('.')[1].strip()
		if language[0] == "H" or language[0] == "S":
			# print "Appending language to output file: %s" % language
			newFile.write("%d %s\n" % (lineNumber, language))
			lineNumber += 1
	
	f.close()
	newFile.close()

	# let's do a one liner to append to the original source file
	# re: slavik -- yes, what IS the point of this? 
	# appending a language that won't affect repeated executions of the program?
	# todo? -- reference a list of H/S languages and append a *new* one to src lang. list
	open('src.txt', 'a').write("%d. English\n" % (totalLines+1))

if __name__ == "__main__":
	main()
	print "Done!"

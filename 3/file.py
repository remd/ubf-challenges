#! /usr/bin/python
# remd
# 6/23/12
#
# file.py
#
# Reads a languages file, does some parsing, writes an output file.
# Then adds more text to source languages file.

def main():
	try:
		f = open('bhaarat.txt', 'r')
	except IOError:
		print "Could not open \"bhaarat.txt\"."

	try:
		newFile = open('out.txt', 'w')
	except IOError:
		print "Could not open \"out.txt\"."
		
	lineNumber = 0
	for line in f:
		language = line.split('.')[1].strip()
		if language[0] == "H" or language[0] == "S":
			print "Appending language to output file: %s" % language
			lineNumber += 1
			newFile.write("%d %s" % lineNumber, language)

if __name__ == "__main__":
	main()

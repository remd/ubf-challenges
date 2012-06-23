#! /usr/bin/python
# remd
# 6/21/2012
# bottles.py
#
# Prints the lyrics of 99 Bottles of Beer(http://99-bottles-of-beer.net/lyrics.html) to the terminal.

def bottles(bottles):
	original = bottles
	while (bottles > 1):
		print "%d bottles of beer on the wall, %d bottles of beer." % (bottles, bottles)
		oneLess = bottles - 1
		print "Take one down and pass it around, %d bottles of beer on the wall.\n" % (oneLess)
		bottles = bottles - 1
	print "%d bottle of beer on the wall, %d bottle of beer." % (bottles, bottles)
	print "Take one down and pass it around, no more bottles of beer on the wall.\n"
	print "No more bottles of beer on the wall, no more bottles of beer."
	print "Go to the store and buy some more, %d bottles of beer on the wall." % (original)

if __name__ == '__main__':
	bottles(99)


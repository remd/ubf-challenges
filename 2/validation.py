#! /usr/bin/python
# remd
# 6/22/2012
#
# validation.py
# Prints a statement about forum name's based on (sanitized) user input.

import sys

class User():
	def __init__(self):
		self.username = ""
		self.age = 0
		self.uid = 0

	def checkQuit(self, inpt):
		if (inpt.lower() == "exit" or
			inpt.lower() == "quit" or
			inpt.lower () == "q"):
				sys.exit(0)
	
	def getUsername(self):
		while True:
			inpt = raw_input("Please enter your username: ")

			if len(inpt) > 20:
				inpt = inpt[0:20]
				assert len(inpt) == 20
				# try and display the truncated named even though the user is being silly
				try:
					print "Name was too long. Truncating to 20 characters: %s" % str(inpt)
				except ValueError:
					print "Name was too long. Truncating to 20 characters. %s" % inpt

			try:
				int(float(inpt))
			except:
				pass
			else:
				print "Username cannot be entirely numbers."
				# we got an int/float
				# reloop
				continue

			# convert odd characters to displayable characters
			inpt = str(inpt)

			self.checkQuit(inpt)

			if self.validateUsername(inpt):
				self.username = inpt
				break

	def validateUsername(self, inpt):
		flag = True

		if inpt.strip() == "":
			flag = False
			print "Username must contain characters."
		elif inpt[0] == " ":
			flag = False
			print "Username cannot begin with a space."
		else:
			pass

		return flag
		
	def getAge(self):
		while True:
			inpt = raw_input("Please enter your age: ")

			self.checkQuit(inpt)

			try:
				inpt = int(float(inpt))
			except ValueError:
				print "Age cannot contain non-numbers."
				# reloop
				continue

			if self.validateAge(inpt):
				self.age = int(inpt)
				break

	def validateAge(self, inpt):
		flag = True

		if inpt == 0:
			flag = False
			print "Age cannot be zero."
		elif inpt < 0:
			flag = False
			print "Age cannot be negative."
		elif inpt > 120:
			flag = False
			print "Too old!"
		else:
			pass

		return flag
	
	def getUid(self):
		while True:
			inpt = raw_input("Please enter your User ID: ")

			self.checkQuit(inpt)

			try:
				inpt = int(float(inpt))
			except ValueError:
				print "User ID cannot contain non-numbers."
				# reloop
				continue

			if self.validateUid(inpt):
				self.uid = int(inpt)
				break

	def validateUid(self, inpt):
		flag = True

		if inpt == 0:
			flag = False
			print "User ID cannot be zero."
		elif inpt < 0:
			flag = False
			print "User ID cannot be negative."
		elif inpt > 999999:
			flag = False
			print "User ID cannot be above 999999."
		else:
			pass

		return flag
				
	def __str__(self):
		return ("You are %s, aged %d. Next year you will be %d.\nYou have user ID %d, the next user is ID %d."
				% (self.username, self.age, self.age+1, self.uid, self.uid+1))

if __name__ == "__main__":
	user = User()
	user.getUsername()
	user.getAge()
	user.getUid()
	print "================"
	print user

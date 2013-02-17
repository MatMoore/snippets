from string import *
from sys import argv
import re

def printAll(l=[], s=""):
	'''printAll(l,s)
	Prints all combinations of a list of lists
	l = a list of lists of words
	s = words to put in front
	'''
	if l:
		newlist = l[1:] #chop off the first list
		for i in l[0]:  #printall the combinations for each value of the first list
			if s:
				printAll(newlist, s + " " + i)
			else:
				printAll(newlist, s + i)
	else:
		print(s)

def getMistxts(sentence):
	'''Find sentances that are typed with the same buttons on a phone.'''
	words = sentence.split()
	otherwords = [getHomonums(word) for word in words]
	printAll(otherwords)

def getHomonums(word):
	'''Find words that are typed with the same buttons on a phone. Returns a list of matches.'''
	matches = []
	if not word:
		return matches
	
	wordlist = open("/usr/share/dict/british-english")

	parts = {2:"[abc]", 3:"[def]", 4:"[ghi]", 5:"[jkl]", 6:"[mno]", 7:"[pqrs]", 8:"[tuv]", 9:"[wxyz]"} #the regex for each button
	buttons = {'a':2, 'b':2, 'c':2, \
	'd':3, 'e':3, 'f':3, \
	'g':4, 'h':4, 'i':4, \
	'j':5, 'k':5, 'l':5, \
	'm':6, 'n':6, 'o':6, \
	'p':7, 'q':7, 'r':7, 's':7, \
	't':8, 'u':8, 'v':8, \
	'w':9, 'x':9, 'y':9, 'z':9} #button each character is on

	word = [buttons[char] for char in lower(word)] #convert to a list of numbers

	#make the regular expression
	regex = ""
	for button in word:
		regex += parts[button]
	r = re.compile("^"+regex+"$")

	#find matches
	for line in wordlist:
		line = line.strip() #remove whitespace
		if r.match(line) != None:
			matches.append(line)
	return matches	

if len(argv) > 1:
	sentence = argv[1:]
	sentence = " ".join(sentence)
	print "sentence = "+sentence
	getMistxts(sentence)
else:
	print "Usage: predictive.py sentence"

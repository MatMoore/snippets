#!/usr/bin/python
import string
import sys

def printPalindromes(line):
	line = line.strip() #remove whitespace from either side
	if len(line) > 0:
		forwards = [i for i in line.lower() if i in string.ascii_lowercase] #strip punctuation and convert to lowercase
		backwards = forwards[::-1]
		if forwards == backwards:
			print(line);

if len(sys.argv) > 1: #read from file
	try:
		textfile = open(sys.argv[1])
		for line in textfile:
			printPalindromes(line)
	except:
		print("%s is not a valid text file" % sys.argv[1])
else: #read from stdin
	while(True):
		try:
			line = input()
			printPalindromes(line)
		except EOFError:
			break;	
	

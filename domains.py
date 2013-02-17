from string import ascii_lowercase as lowercase
import re, random
wordlist = open("/usr/share/dict/british-english")
words = [i.strip() for i in wordlist if not i.isspace()]
regex = "[aeiou]{0,2}([bcdfghjklmnpqrstvwxyz]{1,2}[aeiou]{1,2})+[bcdfghjklmnpqrstvwxyz]{0,2}"
r = re.compile(regex)

def randomWord(n=5):
	letters = []
	while len(letters) < n:
		letters.append(random.choice(lowercase))
	return "".join(letters)

def printRand(n=1):
	acceptable = 0
	while acceptable < n:
		word = randomWord(5)
		if r.match(word) and word not in words:
			acceptable += 1
			print(word)

printRand(50)

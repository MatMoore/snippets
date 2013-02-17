wordlist = open("/usr/share/dict/british-english")
words = [i.strip() for i in wordlist if not i.isspace()]

def rot13(word):
	return "".join([chr((ord(c)-ord('a')+13) % 26 + ord('a')) for c in word.lower()])
		
result = [i for i in words if rot13(i)==i[::-1]]
for i in result:
	print(i)

import random
import re
import string

MARKOV_LENGTH = 2

def normalize(s):
	return s.lower().translate(None,string.punctuation) # strip punctuation

def punctuate(words):
	result=''
	for i in words:
		if result and i not in string.punctuation:
			result += ' '
		result += i
	return result

class Tommy:

	def __init__(self):
		self.nouns = ('Mark', 'Johnny', 'Lisa','Denny','doggy', 'girl', 'princess')
		self.responses = {
			'^how was':'Oh pretty good. We got a new client... at the bank. We make a lot of money.',
			'^what .+':'I can not tell you, its confidential.',
			'why not':'No I can\'t. Anyway, how is your sex life?',
			'girl':'I used to know a girl, she had a dozen guys. One of them found out about it... beat her up so bad she ended up at a hospital on Guerrero Street.',
			'what are you talking about':'I told him that to make it interesting',
			'ready\??$':'How do you mean that? I\'m always ready... for you.',
			'here you go':'You\'re my favourite customer!'
		}

		self.phrases = [
			'That\'s the idea!',
			'Anything for my princess!',
			'Leave your *stupid* comments in your pocket!'
		]

		# Link words together for the Markov Chain algorithm
		text = open('phrases.txt','r')

		self.words = {}
		self.analyseText(text)

	def analyseText(self,text):

		# Start a new sequence of words to use as the key
		words = ['' for i in range(MARKOV_LENGTH)]

		for line in text:
			words = self.analyseLine(line,words)

	# Parse a line into tokens.
	# Tokens can be either a word, punctuation (to be appended to the last word)
	# or an empty string, indicating the end of a sentence
	def parseLine(self,line):
		tokens = []
		if not line return (,)
		return

	def analyseLine(self,line,prevWords):
		if not line: return prevWords

		words = prevWords

		for word in line.split(): # first split on whitespace
			if not word: continue

			# now cut off trailing punctuation
			end = len(word)
			punctuation = ''
			while word[end-1] in string.punctuation and end>0:
				end -= 1
			punctuation = ''.join(word[end:])
			word = ''.join(word[:end])

			# treat all these as just marking the end of the sentence (signified by empty string)
			# other punctuation following a word is ignored for now
			tokens = [word]
			if punctuation in ('.','!'):
				tokens.append('')

			for token in tokens:
				# add the token to the dictionary, indexed by the tokens that came before it
				token = normalize(token)
				self.words.setdefault(tuple(words),[]).append(token)

				# rotate the sequence of words used as the dictionary key
				words = words[1:]
				words.append(token)

		# Add the end of sentence marker at the end of the line, if it wasn't terminated by '.' or anything
		if words[-1]:
			self.words.setdefault(tuple(words),[]).append('')
			# rotate the sequence of words used as the dictionary key
			words = words[1:]
			words.append('')
		return words

	def chain(self, message):
		response = []
		while True:
			word = random.choice(self.words[message])
			response += word
			print word
			if not word: #empty strings mark the end of sentences
				return response
			message = tuple(list(message[1:])+[word])

	def randomChain(self):
		'''Create a random response'''
		keys = self.words.keys()
		while True:
			key = random.choice(keys)
			if key[-1] in ('.','','!','?'):
				return self.chain(key)

	def mangledResponse(self,message,name='Mark'):
		'''Markov chain generated response'''
		message = message[-MARKOV_LENGTH:]
		if len(message) < MARKOV_LENGTH:
			# Prefix with empty strings
			message = ['' for i in MAKOV_LENGTH-len(message)]+message.split('')
			print 'Responding to '+str(message)
		message = tuple(message)
		print 'Responding to '+str(message)
		if message in self.words:
			return punctuate(self.chain(message))
		else:
			return punctuate(self.randomChain())

	def keywordResponse(self,name,message):
		'''React to keywords in the message'''
		pass

	def greet(self,name):
		greetings = ['hi '+name, 'oh hi '+name]
		return random.choice(greetings)
	
	def sayBye(self,name):
		farewells = ['bye bye', 'bye '+name]
		return random.choice(farewells)

	def respond(self, name, message):
		pass

	def spoon(self):
		return '''
-------------
|      ..    |
|     (  )   |
|     \  /   |
|      ||    |
|      ||    |
|      ||    |
|      []    |
|____________|
'''

MARKOV_LENGTH = 2
tommy = Tommy()
print tommy.words
print tommy.mangledResponse('oh hi mark')

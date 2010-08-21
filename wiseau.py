import random
import re
import string

def normalize(s):
	return s.lower().translate(None,string.punctuation) # strip punctuation

def punctuate(words):
	result=''
	for i in words:
		if result and i not in string.punctuation:
			result += ' '
		result += i
	return string.upper(result)

class Tommy:

	def __init__(self):
		self.nouns = ('Mark', 'Johnny', 'Lisa','Denny','doggy', 'girl', 'princess')
		self.responses = [
			('^how was','Oh pretty good. We got a new client... at the bank. We make a lot of money.'),
			('^what .+','I can not tell you, its confidential.'),
			('why not','No I can\'t. Anyway, how is your sex life?'),
			('girl','I used to know a girl, she had a dozen guys. One of them found out about it... beat her up so bad she ended up at a hospital on Guerrero Street.'),
			('what are you talking about','I told him that to make it interesting'),
			('ready\??$','How do you mean that? I\'m always ready... for you.'),
			('here you go','You\'re my favourite customer!')
		]

		self.favouriteCustomer = [] # List of people who have accepted the lord Tommy Wiseau into their heart

		# Link words together for the Markov Chain algorithm
		text = open('phrases.txt','r')

		self.words = {}
		self.analyseText(text)

	def analyseText(self,text):

		# Start a new sequence of words to use as the key
		words = ['' for i in range(MARKOV_LENGTH)]

		for line in text:
			words = self.analyseLine(line,words)

	def parseSentence(self,sentence):
		'''# Parse a sentence into tokens.
Tokens can be either a word, punctuation (to be appended to the last word)
or an empty string, indicating the end of a sentence'''
		tokens = []
		if not sentence: return tuple(tokens)

		for word in sentence.strip().split(): # first split on whitespace

			# now cut off trailing punctuation
			end = len(word)
			punctuation = ''
			while word[end-1] in string.punctuation and end>0:
				end -= 1
			punctuation = ''.join(word[end:])
			word = ''.join(word[:end])

			# Remove punctuation within the word
			word = normalize(word)
			tokens.append(word)

			# treat all these as just marking the end of the sentence (signified by empty string)
			# other punctuation following a word is ignored for now
			if punctuation in ('.','!'):
				tokens.append('')

		# Mark the end of the sentence if it hasn't already been done
		if tokens and tokens[-1]:
			tokens.append('')

		return tuple(tokens)

	def analyseLine(self,line,prevWords):
		'''Analyse a line of the input text. It is assumed that sentences are not split up over multiple lines. Returns the last few words after processing the line.'''

		 # reset the previous words list after encountering an empty line
		if not line.strip(): return ['' for i in range(MARKOV_LENGTH)]

		words = prevWords

		for token in self.parseSentence(line):
			# add the token to the dictionary, indexed by the tokens that came before it
			self.words.setdefault(tuple(words),[]).append(token)

			# rotate the sequence of words used as the dictionary key
			words = words[1:]
			words.append(token)

		return words

	def chain(self, message):
		'''Pick a random response to the message'''
		response = []
		while True:
			word = random.choice(self.words[message])
			response.append(word)
			if not word: #empty strings mark the end of sentences
				return response
			message = tuple(list(message[1:])+[word])

	def randomChain(self):
		'''Pick a random response'''
		keys = self.words.keys()
		while True:
			key = random.choice(keys)
			if key[-1] in ('.','','!','?'):
				return self.chain(key)

	def mangledResponse(self,message,name='Mark'):
		'''Markov chain generated response'''
		message = self.parseSentence(message) # tokenize
		message = message[-MARKOV_LENGTH:] # truncate

		# Prefix with empty strings if neccessary
		if len(message) < MARKOV_LENGTH:
			message = ['' for i in range(len(message),MARKOV_LENGTH)]+list(message)

		message = tuple(message)
		print 'Responding to '+str(message)

		if message in self.words:
			return punctuate(self.chain(message))
		else:
			return punctuate(self.randomChain())

	def keywordResponse(self,name,message):
		'''React to keywords in the message'''
		positive = []
		negative = []
		unhappy = [
			'Leave your *stupid* comments in your pocket!'
		]
		happy = [
			'That\'s the idea!',
			'Anything for my princess!'
		]
		return None

	def greet(self,name):
		greetings = ['hi '+name, 'oh hi '+name]
		return random.choice(greetings)
	
	def sayBye(self,name):
		farewells = ['bye bye', 'bye '+name]
		return random.choice(farewells)

	def respond(self, name, message):
		keyword = self.keywordResponse(name, message)
		if keyword:
			return keyword
		if random.random()*100 < RESPOND_PERCENT:
			if random.random()*100 < SPOON_PERCENT:
				return self.spoon()
			else:
				return self.mangledResponse(self,message,name)

		return None

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

MARKOV_LENGTH = 3
RESPOND_PERCENT = 20
SPOON_PERCENT = 5

if __name__ == '__main__':
	tommy = Tommy()
	print tommy.words
	print tommy.mangledResponse('you are just chicken')
	print tommy.mangledResponse('!!!!')

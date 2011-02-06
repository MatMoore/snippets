#!/usr/bin/python
# coding=UTF-8
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

class Tommy(object):

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self,value=None):
		self._name = value
		self.nickRegex = re.compile(value,flags=re.IGNORECASE)

	def __init__(self,name='Tommy Wiseau',filenames=('phrases.txt',),):
		object.__init__(self)
		self.name = name

		# Words which could be substituted for usernames
		self.nouns = ('Mark', 'Johnny','Tommy Wiseau','Tommy','Lisa','Denny','doggy', 'girl', 'princess')
		nameRegex = '|'.join(self.nouns)
		self.nameRegex = re.compile(nameRegex,flags=re.IGNORECASE)

		# Response which match a specific pattern
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
		self.memory = ['' for i in range(MARKOV_LENGTH)] # Store the last few words analysed
		self.words = {}

		for filename in filenames:
			text = open(filename,'r')
			self.analyseText(text)
		log = open('chatlog.log','r')
		self.analyseText(log)
		self.log = 'chatlog.log'

	def remember(self,token):
		'''Remember the word'''
		# add the token to the dictionary, indexed by the tokens that came before it
		self.words.setdefault(tuple(self.memory),[]).append(token)

		# rotate the sequence of words used as the dictionary key
		self.memory = self.memory[1:]
		self.memory.append(token)


	def analyseText(self,text):
		'''Analyse a text file'''
		for line in text:
			words = self.analyseLine(line)

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

	def analyseLine(self,line):
		'''Analyse a line of the input text. It is assumed that sentences are not split up over multiple lines.'''

		 # reset the previous words list after encountering an empty line
		if not line.strip():
			self.memory = ['' for i in range(MARKOV_LENGTH)]

		for token in self.parseSentence(line):
			self.remember(token)

	def chain(self, message):
		'''Pick a random response to the message'''
		response = []

		while True:
			possibilities = self.words[message]

			# If theres only one choice, sometimes combine the response with another one
			if response and len(possibilities) == 1 and possibilities[0] and random.random()*100 < MIXUP_PERCENT:
				return response + self.randomChain(start=False)

			word = random.choice(possibilities)
			response.append(word)
			if not word: #empty strings mark the end of sentences
				return response
			message = tuple(list(message[1:])+[word])

	def randomChain(self,start=True):
		'''Pick a random response'''
		keys = self.words.keys()
		while True:
			key = random.choice(keys)

			# Only accept the end of a sentence as a key
			if (key[-1] in ('.','','!','?') and start) or (key[-1] not in ('.','','!','?') and not start):
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
		greetings = (('hi',name), ('oh', 'hi', name))
		if name.lower() == 'stealthcopter':
			return 'BOOOO'

		return punctuate(random.choice(greetings))
	
	def sayBye(self,name):
		farewells=(('bye', 'bye'), ('bye',name))
		return punctuate(random.choice(farewells))

	def respond(self, name, message, mustRespond=False):
		if name != self.name:
			self.analyseLine(message)
			with open(self.log, 'a') as f:
				f.write(message+'\n')

		keyword = self.keywordResponse(name, message)
		if keyword:
			return keyword

		# Always respond to your own name
		if mustRespond or random.random()*100 < RESPOND_PERCENT or (name != self.name and message.lower().find(self.name.lower()) != -1):
			if random.random()*100 < SPOON_PERCENT:
				return self.spoon()
			else:
				response = self.mangledResponse(message,name)

				# Replace names with the name of whoever spoke last
				response = re.sub(self.nickRegex,name.upper(),response) # substitute Nick
				response = re.sub(self.nameRegex,name.upper(),response) # substitute other names
				return response

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

class SenorWiseau(Tommy):
	def __init__(self,name='Tommy Wiseau'):
		Tommy.__init__(self,name,filenames=('spanish.txt',))

	def greet(self,name):
		greetings = (('Hola',u'señor',name), ('oh', 'hola',u'señor', name))

		return punctuate(random.choice(greetings))
	
	def sayBye(self,name):
		farewells=(('adios',u'señor',name))
		return punctuate(random.choice(farewells))


MARKOV_LENGTH = 2
RESPOND_PERCENT = 40
SPOON_PERCENT = 3
MIXUP_PERCENT = 0

if __name__ == '__main__':
	RESPOND_PERCENT = 100

	tommy = SenorWiseau()
	print tommy.greet('User')
	try:
		while True:
			i = raw_input('> ')
			o = tommy.respond('Mark',i)
			print o
	except EOFError:
			pass
#	print tommy.words
#	print tommy.mangledResponse('you are just chicken')
#	print tommy.mangledResponse('!!!!')

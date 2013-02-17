import wiseau
import asyncore
import socket

class IrcBot(asyncore.dispatcher):
	def __init__(self,host,channel,bot,nick='TommyWiseau',port=6667):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect((host,port))
		self.channel = channel
		self.nick = nick
		self.bot = bot
		self.bot.name = nick
		self.host = host
		self.buffer = ''
		self.responses = []
		self.inChannel = False

	def handle_connect(self):
		pass

	def parse(self,message):
		"""Breaks a message from an IRC server into its prefix, command, and arguments. Thanks stack overflow!"""
		prefix = ''
		trailing = []
		if not message:
			return '','',''
		if message[0] == ':':
		    prefix, message = message[1:].split(' ', 1)
		if message.find(' :') != -1:
		    message, trailing = message.split(' :', 1)
		    args = message.split()
		    args.append(trailing)
		else:
		    args = message.split()
		command = args.pop(0)
		return prefix, command, args

	def handle_close(self):
		self.close()

	def readable(self):
		return True

	def handle_read(self):
		self.buffer += self.recv(8192)
		messages = self.buffer.split('\n')

		self.buffer = messages.pop() # put non terminated lines back in the buffer

		for line in messages:
			line = line.rstrip()
			print line
			prefix,command,args = self.parse(line)

			if command == 'PING':
				# Handle ping messages
				self.responses.append('PONG')
			elif command == 'PRIVMSG':
				# Handle normal messages
				channel = None
				respond = True # Always respond to pms
				if args and args[0] and args[0][0] == '#':
					channel = args[0]
					respond = False
				args = args[1:] # First arg is the name/channel
				message = ' '.join(args)

				print message
				if message.lower() == '\x01version\x01'.lower():
					continue

				name = prefix.split('!')[0]
				if name[0] == '~':
					name = name[1:]

				response = self.bot.respond(name,message,mustRespond=respond)
				if response:
					for line in response.split('\n'):
						if not line.strip(): continue
						if channel:
							response = 'PRIVMSG '+self.channel+' :'+line
						else:
							response = 'PRIVMSG '+name+' :'+line
						self.responses.append(response)
			elif command == 'JOIN':
				name = prefix.split('!')[0]
				if name[0] == '~':
					name = name[1:]
				if name.lower() == self.nick.lower():
					continue
				response = self.bot.greet(name)
				response = 'PRIVMSG '+self.channel+' :'+response
				self.responses.append(response)

			elif command in ('PART','QUIT'):
				name = prefix.split('!')[0]
				if name[0] == '~':
					name = name[1:]
				response = self.bot.sayBye(name)
				response = 'PRIVMSG '+self.channel+' :'+response
				self.responses.append(response)

	def writable(self):
		return (not self.inChannel) or self.responses

	def handle_write(self):
		print 'handle write'
		print str(self.connected)
		if not self.inChannel:
			print 'Connecting...'
			self.send("NICK %s\r\n" % self.nick)
			self.send("USER %s %s bla :%s\r\n" % ('WiseauBot', self.host, 'Tommy Wiseau'))
			self.send('JOIN %s\r\n' % self.channel)
			self.inChannel = True
			return

		response = self.responses[0]
		self.responses = self.responses[1:]
		print response
		if response:
			self.send(response+'\r\n')

if __name__=='__main__':
	tommy = wiseau.Tommy(filenames=('phrases.txt',))
	host = 'irc.freenode.net'
	channel = '#doomcentral'
	bot = IrcBot(host,channel,tommy,nick='TommyWiseau')
	asyncore.loop()

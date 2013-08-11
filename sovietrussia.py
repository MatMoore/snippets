from text.blob import TextBlob

def soviet_russia(text):
  text = TextBlob(text)
  verb = None
  noun = None
  for tag in text.tags:
    if verb and noun:
      break
    if tag[1] in ('VBP', 'VBZ') and tag[0] not in ('is',):
      verb = tag[0]
    elif verb and tag[1] == 'NN':
      noun = tag[0]
  if verb and noun:
    return 'In Soviet Russia, {noun} {verb} you!'.format(verb=verb, noun=noun)

if __name__ == '__main__':
  while True:
    resp = soviet_russia(input('> '))
    if resp:
      print(resp)

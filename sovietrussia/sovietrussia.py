import fileinput
from textblob import TextBlob


def soviet_russia(text):
  text = TextBlob(text)
  verb = None
  noun = None
  for word, meaning in text.tags[1:]:
    if verb and noun:
      break
    if meaning.startswith('VB') and meaning != 'VBD' and word not in ('is',):
      verb = word
    elif verb and meaning.startswith('NN'):
      noun = word
  if verb and noun:
    return 'In Soviet Russia, {noun} {verb} you!'.format(verb=verb, noun=noun)


if __name__ == '__main__':
    for line in fileinput.input():
        result = soviet_russia(line)
        if result:
            print(result)

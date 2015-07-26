from __future__ import print_function
from sys import argv
import re
from itertools import product


def get_mistxts(sentence):
    '''Find sentances that are typed with the same buttons on a phone.'''
    sentence = sentence.lower()
    sentence = re.sub('\W+', ' ', sentence)
    words = sentence.split()
    otherwords = [set(get_homonums(word)) | set((word,)) for word in words]
    for new_words in product(*otherwords):
        new_sentence = ' '.join(new_words)
        if new_sentence != sentence:
            print(new_sentence)


def get_homonums(word):
    '''
    Find words that are typed with the same buttons on a phone.
    Returns a list of matches.
    '''
    matches = []
    if not word:
        return matches

    wordlist = open("/usr/share/dict/words")

    # the regex for each button
    parts = {
        2: "[abc]",
        3: "[def]",
        4: "[ghi]",
        5: "[jkl]",
        6: "[mno]",
        7: "[pqrs]",
        8: "[tuv]",
        9: "[wxyz]"
    }

    # button each character is on
    buttons = {
        'a': 2, 'b': 2, 'c': 2,
        'd': 3, 'e': 3, 'f': 3,
        'g': 4, 'h': 4, 'i': 4,
        'j': 5, 'k': 5, 'l': 5,
        'm': 6, 'n': 6, 'o': 6,
        'p': 7, 'q': 7, 'r': 7, 's': 7,
        't': 8, 'u': 8, 'v': 8,
        'w': 9, 'x': 9, 'y': 9, 'z': 9
    }

    # convert to a list of numbers
    word = [buttons[char] for char in word.lower()]

    # make the regular expression
    regex = ""
    for button in word:
        regex += parts[button]
    r = re.compile("^"+regex+"$")

    for line in wordlist:
        line = line.strip()
        if r.match(line):
            matches.append(line)
    return matches

if __name__ == '__main__':
    if len(argv) > 1:
        sentence = argv[1:]
        sentence = " ".join(sentence)
        print("sentence = " + sentence)
        get_mistxts(sentence)
    else:
        print("Usage: predictive.py sentence")

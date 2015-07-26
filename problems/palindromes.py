#!/usr/bin/python
from __future__ import print_function
import string
import fileinput


def is_palindrome(line):
    "Line reads the same forwards and backwards"
    line = line.lower()
    line = [i for i in line if i in string.ascii_lowercase]
    return line and line == line[::-1]


if __name__ == '__main__':
    for line in fileinput.input():
        line = line.strip()
        if is_palindrome(line):
            print(line)

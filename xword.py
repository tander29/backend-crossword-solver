#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program tander29"""

__author__ = "tander29"


# YOUR HELPER FUNCTION GOES HERE
def match_words(test_word, words):
    known_letters = {}
    for letter in test_word:
        if letter != "?":
            known_letters[test_word.find(letter)] = letter

    for dict_word in words:
        if len(dict_word) == len(test_word):
            matching_cases = True
            for index, letter in known_letters.iteritems():
                if dict_word[index] != letter:
                    matching_cases = False
            if matching_cases:
                print (dict_word)
    # print known_letters
    # print test_word


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse "?" to signify unknown letters: ')
    test_word.lower()

    # YOUR ADDITIONAL CODE HERE
    match_words(test_word, words)
    # raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""Generate random story using trigrams."""
import io
import random
import string


def read_file():
    """Open and read file input."""
    f = io.open('sherlock_small.txt', 'r')
    lines = ''.join(f.readlines())
    lines = lines.replace('--', ' ')
    lines = lines.replace('\n', ' ')
    return lines


def strip_punct(text):
    """Return string without punctuation."""
    for c in string.punctuation:
        text = text.replace(c, '')
    return text


def create_list(text):
    """Return list of words."""
    text = text.split(' ')
    return text


def create_dict(text):
    """Return dictionary from list"""
    word_dict = {}
    for i in range(0, len(text) - 2):
        dict_key = (text[i], text[i + 1])
        word_dict.setdefault(dict_key, []).append(text[i + 2])
    return word_dict


def make_a_damn_story(text, n):
    """Make a damn story."""
    primer = random.choice(list(text.keys()))
    story = '{} {}'.format(primer[0], primer[1])
    for i in range(0, n - 2):
        pass


# creat empty list.
# assign value i and i + 1 as values equal to tuples in keys
# append i+2 as value at key.

# append i+3 as value of key made by i+1 and i+2
# etc

# smash story list into a string


text = read_file()
text = strip_punct(text)
text = create_list(text)
text = create_dict(text)
print(text)


# io.close

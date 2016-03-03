# -*- coding: utf-8 -*-
"""Generate random story using trigrams."""
import io
import string


def read_file():
    """Open and read file input."""
    f = io.open('sherlock_small.txt', 'r')
    lines = ''.join(f.readlines())
    lines = lines.replace('--', ' ')
    lines = lines.replace('\n', '')
    return lines


def strip_punct(text):
    """Return string without punctuation."""
    for c in string.punctuation:
        text = text.replace(c, '')
    return text


def create_list(text):
    text = text.split(' ')
    return text


def create_dict(text):
    word_dict = {}
    for i in range(0, len(text) - 2):
        word_dict[(text[i], text[i + 1])] = text[i + 2]
    return word_dict


text = read_file()
text = strip_punct(text)
text = create_list(text)
text = create_dict(text)
print(text)

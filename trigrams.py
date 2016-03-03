# -*- coding: utf-8 -*-
"""Generate random story using trigrams."""
import io
import string


def read_file():
    """Open and read file input."""
    f = io.open('sherlock_small.txt', 'r')
    lines = ''.join(f.readlines())
    lines = lines.replace('--', ' ')
    return lines


def strip_punct(text):
    """Return string without punctuation."""
    for c in string.punctuation:
        text = text.replace(c, '')
    return text


def create_list(text):
    text = text.split(' ')
    return text


# def create_dict():
    #


text = read_file()
text = strip_punct(text)
text = create_list(text)

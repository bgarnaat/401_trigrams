# -*- coding: utf-8 -*-
"""Generate random story using trigrams."""
import io


def read_file():
    """Open and read file input."""
    f = io.open('sherlock_small.txt', 'r')
    lines = ''.join(f.readlines())
    print(lines)
    return lines


def strip_punct(text):
    """Do stuff."""
    # strip punct from text


read_file()

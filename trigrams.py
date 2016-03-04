# -*- coding: utf-8 -*-
"""Generate random story using trigrams."""
import io
import random
import string
import sys


def read_file(file):
    """Open and read file input."""
    f = io.open(file, 'r', encoding='utf-8')
    lines = ''.join(f.readlines())  # chane to read and  remove replace(\n)
    lines = lines.replace('--', ' ')    # MOVE TO strip_punct
    lines = lines.replace('\n', ' ')    # MOVE TO strip_punct
    f.close()
    return lines


def strip_punct(text):
    """Return string without punctuation."""
    for c in string.punctuation:
        text = text.replace(c, '')
    return text


def create_list(text):
    """Return list of words."""
    text = text.split(' ')  # NOTE:  split() with no arg!  split on any space!!
    return text


def create_dict(text):
    """Return dictionary from list."""
    word_dict = {}
    for i in range(0, len(text) - 2):
        dict_key = (text[i], text[i + 1])   # try out slice[:] here
        # dict_key = (text[i:i+2])  # slice method
        value = text[i + 2]
        word_dict.setdefault(dict_key, []).append(value)
    return word_dict


def make_a_damn_story_list(text, n):
    """Make a damn story list."""
    primer = random.choice(list(text.keys()))
    story_list = []
    story_list.append(primer[0])
    story_list.append(primer[1])
    key = (story_list[0], story_list[1])
    while text[key]:
        story_list.append(random.choice(text[key]))
        if story_list[-1] == '':
            break
        key = story_list[-2], story_list[-1]
    story_list = story_list[:(n - 1)]
    # story_list = story_list[:int(n) - 2]

    # TODO:  add else block to reseed if dead end.

    # story = story[0:n]    # PREVENT STORY FROM EXEEDING LIMIT IF RESEED
    return story_list


def make_a_damn_story(text):
    """Make a damn story."""
    story = ' '.join(text)
    return story


def write_a_damn_story(text, file):
    """Write a damn story."""
    file_out = open(file, 'w')
    file_out.write(text)
    file_out.close()


def main(file_in, n, file_out):
    """Main module."""
    text = read_file(file_in)
    text = create_list(text)
    text = create_dict(text)
    text = make_a_damn_story_list(text, n)
    text = make_a_damn_story(text)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

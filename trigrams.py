# -*- coding: utf-8 -*-
"""Generate random story using trigrams."""
import io
import random
import string
import sys


def read_file(file):
    """Open and read file input."""
    f = io.open(file, 'r')
    lines = ''.join(f.readlines())
    lines = lines.replace('--', ' ')
    lines = lines.replace('\n', ' ')
    f.close()
    return lines


def strip_punct(text):
    """Return string without punctuation."""
    for c in string.punctuation:
        text = text.replace(c, '')
    return text


def create_list(text):
    """Return list of words."""
    text = text.split(' ')
    # print(text)
    # text.pop()
    # print(text)
    return text


def create_dict(text):
    """Return dictionary from list."""
    word_dict = {}
    for i in range(0, len(text) - 2):
        dict_key = (text[i], text[i + 1])
        word_dict.setdefault(dict_key, []).append(text[i + 2])
        # if text[i + 2] != '':
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
    story_list = story_list[:int(n) - 2]
    return story_list


def make_a_damn_story(text):
    """Make a damn story."""
    story = ' '.join(text)
    return story


def main(file, n):
    """Main module."""
    text = read_file('sherlock_small.txt')
    text = create_list(text)
    text = create_dict(text)
    text = make_a_damn_story_list(text, n)
    text = make_a_damn_story(text)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

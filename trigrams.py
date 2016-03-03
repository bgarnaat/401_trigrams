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
    story_list = story_list[:(n - 1)]
    return story_list


def make_a_damn_story(text):
    """Make a damn story."""
    story = ' '.join(text)
    return story


text = read_file()
text = create_list(text)
text = create_dict(text)
text = make_a_damn_story_list(text, 200)
text = make_a_damn_story(text)
print(text)

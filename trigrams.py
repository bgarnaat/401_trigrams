# -*- coding: utf-8 -*-
"""Generate random story using trigrams."""
import io
import random
import sys


def read_file(file):
    """Open and read file input."""
    f = io.open(file, 'r', encoding='utf-8')
    lines = ''.join(f.readlines())
    f.close()
    return lines


def strip_punct(text):
    """Return string without punctuation."""
    text = text.replace('--', ' ').replace('\n', ' ')
    return text


def create_list(text):
    """Return list of words."""
    text = text.split(' ')
    return text


def create_dict(text):
    """Return dictionary from list."""
    word_dict = {}
    for i in range(0, len(text) - 2):
        dict_key = tuple(text[i:i+2])
        value = text[i + 2]
        word_dict.setdefault(dict_key, []).append(value)
    return word_dict


def make_a_damn_story_list(text, n):
    """Make a damn story list."""
    key = random.choice(list(text.keys()))
    story_list = list(key)

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
    print(story)


def main(file_in, n):
    """Main module."""
    text = read_file(file_in)
    text = strip_punct(text)
    text = create_list(text)
    text = create_dict(text)
    text = make_a_damn_story_list(text, n)
    text = make_a_damn_story(text)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

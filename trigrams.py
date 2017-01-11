# -*- coding: utf-8 -*-
"""Generate rnadom story using trigrams from a text file specified by user."""
import io
import random
import sys


def read_file(file):
    """Open and read file input."""
    f = io.open(file, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text


def strip_d_hyphen(text):
    """Return string without double hyphens.  Keep other punctuation."""
    return text.replace('--', ' ')


def create_list(text):
    """Create and return a list of the words present in story."""
    return text.split()


def create_dict(text_list):
    """Create and return a dict of trigrams present in story."""
    text_dict = {}
    {text_dict.setdefault(tuple(text_list[i:i + 2]), []).append(text_list[i + 2]) for i in range(0, len(text_list) - 2)}
    return text_dict


def create_story_list(text_dict, n):
    """Create and return a story as a list."""
    story_list = list(seed_story(text_dict))
    while len(story_list) < n:
        dict_key = (story_list[-2], story_list[-1])
        try:
            story_list.append(random.choice(text_dict[dict_key]))
        except KeyError:
            story_list.extend(seed_story(text_dict))
    return story_list[:n]


def seed_story(text_dict):
    """Generate random seed for story."""
    return random.choice(list(text_dict.keys()))


def create_story(story_list):
    """Create string of text from story_list."""
    return ' '.join(story_list)


def main(file, n):
    """Main Module."""
    text = read_file(file)
    text = strip_d_hyphen(text)
    text_list = create_list(text)
    text_dict = create_dict(text_list)
    story_list = create_story_list(text_dict, n)
    story = create_story(story_list)
    print(story)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

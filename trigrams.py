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
    text = text.replace('--', ' ')
    return text


def create_list(text):
    """Create and return a list of the words present in story."""
    text_list = text.split()
    return text_list


def create_dict(text_list):
    """Create and return a dict of trigrams present in story."""
    text_dict = {}
    for i in range(0, len(text_list) - 2):
        dict_key = tuple(text_list[i:i + 2])
        dict_value = text_list[i + 2]
        text_dict.setdefault(dict_key, []).append(dict_value)
    return text_dict


def create_story_list(text_dict, n):
    """Create and return a story as a list."""
    story_list = list(seed_story(text_dict))
    # print(list(text_dict.keys)
    # for i in range(0, n - 2):
    while len(story_list) < n:
        dict_key = (story_list[-2], story_list[-1])
        if dict_key in text_dict.keys():
            story_list.append(random.choice(text_dict[dict_key]))
        else:
            story_seed = seed_story(text_dict)
            if len(story_list) < n - 1:
                story_list.append(story_seed[0])
                story_list.append(story_seed[1])
            else:
                story_list.append(story_seed[0])
    return story_list


def seed_story(text_dict):
    """Generate random seed for story."""
    story_seed = random.choice(list(text_dict.keys()))
    return story_seed


def create_story(story_list):
    """Create string of text from story_list."""
    story = ' '.join(story_list)
    print(story)
    return(story)  # NOTE: this return is for function test


def main(file, n):
    """Main Module."""
    text = read_file(file)
    text = strip_d_hyphen(text)
    text_list = create_list(text)
    text_dict = create_dict(text_list)
    story_list = create_story_list(text_dict, n)
    create_story(story_list)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

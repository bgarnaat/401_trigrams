# -*- coding: utf-8 -*-
"""Shut the hell up docstring."""


text = 'this is some--text--to test. This is some other text'
text_cleaned = 'this is some text to test. This is some other text'
text_list = [
            'this', 'is', 'some', 'text', 'to', 'test.',
            'This', 'is', 'some', 'other', 'text',
            ]

text_dict = {
    ('this', 'is'): ['some'],
    ('is', 'some'): ['text', 'other'],
    ('some', 'text'): ['to'],
    ('text', 'to'): ['test.'],
    ('to', 'test.'): ['This'],
    ('test.', 'This'): ['is'],
    ('This', 'is'): ['some'],
    ('some', 'other'): ['text'],
}

story_list = [
            'this', 'is', 'some', 'text', 'to', 'test.',
            'This', 'is', 'some', 'other', 'text',
            ]

n = 25


def test_strip_d_hyphen():
    """Assert double hyphen is removed."""
    from trigrams import strip_d_hyphen
    assert strip_d_hyphen(text) == text_cleaned


def test_create_list():
    """Assert text string is converted to list of strings."""
    from trigrams import create_list
    assert create_list(text_cleaned) == text_list


def test_create_dict():
    """Assert dictionary of trigrams is created with tuple keys."""
    from trigrams import create_dict
    assert create_dict(text_list) == text_dict


def test_seed_story():
    """Assert random story seed is generated."""
    from trigrams import seed_story
    assert len(seed_story(text_dict)) == 2


def test_create_story_list():
    """Assert a story is returned as a list of strings."""
    from trigrams import create_story_list
    assert len(create_story_list(text_dict, n)) == n


def test_create_story():
    """Assert a string is returned (for testing)."""
    from trigrams import create_story
    assert isinstance(create_story(story_list), str)

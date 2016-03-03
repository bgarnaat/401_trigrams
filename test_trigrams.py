# -*- coding: utf-8 -*-
"""Trigram tests."""


text = "az"
text_with_punct = "a.,/-z"

text_w_space = "this is some text to test"
text_list = ['zero', 'one', 'two', 'zero', 'one', 'three', 'four']

text_dict = {
    ('zero', 'one'): ['two', 'three'],
    ('one', 'two'): ['zero'],
    ('two', 'zero'): ['one'],
    ('one', 'three'): ['four'],
    ('three', 'four'): ['']
    }
n = 4


def test_read_file():
    """Assert the file imported and was split into lines."""
    from trigrams import read_file
    assert len(read_file()) > 0


def test_strip_punct():
    """Assert no punctuation exists in the text."""
    from trigrams import strip_punct
    assert strip_punct(text_with_punct) == text


def test_create_list():
    """Assert list is created on space."""
    from trigrams import create_list
    assert '' not in create_list(text_w_space)


def test_create_dict():
    """Assert dictionary is created with tuple keys."""
    from trigrams import create_dict
    assert len(create_dict(text_list).keys())


def test_repeat():
    """Assert that there are dict items with multiple list values."""
    from trigrams import create_dict
    assert len(create_dict(text_list)[('zero', 'one')]) > 1


def test_story_list():
    """Assert something."""
    from trigrams import make_a_damn_story_list
    assert len(make_a_damn_story_list(text_dict)) > 2


def test_story():
    """Assert that a single string is returned."""
    from trigrams import make_a_damn_story
    assert isinstance(make_a_damn_story(text_list), str)

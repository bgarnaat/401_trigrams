# -*- coding: utf-8 -*-
"""Trigram tests."""


text = "az"
text_with_punct = "a.,/-z"

text_w_space = "this is some text to test"
text_to_list = []


def test_read_file():
    """Assert the file imported and was split into lines."""
    from trigrams import read_file
    assert len(read_file()) > 0


def test_strip_punct():
    """Assert no punctuation exists in the text."""
    from trigrams import strip_punct
    assert strip_punct(text_with_punct) == text


def test_create_list():
    """Assert list is created on space"""
    from trigrams import create_list
    assert '' not in create_list(text_w_space)

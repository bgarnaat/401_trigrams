# -*- coding: utf-8 -*-
"""Trigram tests."""
import pytest


text = "az"
text_with_punct = "a.,/-z"


def test_read_file():
    """Assert the file imported and was split into lines."""
    from trigrams import read_file
    assert len(read_file()) > 0


@pytest.mark.parametrize('text, text_res', text_with_punct, text)
def test_strip_punct(text, text_res):
    """Assert no punctuation exists in the text."""
    from trigrams import strip_punct
    assert strip_punct(text) == text_res

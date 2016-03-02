# -*- coding: utf-8 -*-
"""Trigram tests."""
import pytest


text = "egtidfjgiojfigjerg"


def test_read_file():
    """Assert the file imported and was split into lines."""
    from trigrams import read_file
    assert len(read_file()) > 0


@pytest.mark.parametrize('text', text)
def test_strip_punct(text):
    """Docstring."""
    # from trigrams import strip_punct()
    assert text.isalpha()

# -*- coding: utf-8 -*-
import pytest


def test_read_file():
    """Assert the file imported and was split into lines."""
    from trigrams import read_file
    assert len(read_file()) > 0


import pytest


def test_read_file():
    from trigrams import read_file
    lines = read_file()
    assert len(lines) > 0

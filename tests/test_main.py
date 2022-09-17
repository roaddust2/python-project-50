import pytest
from gendiff.diff import calculate_diff


@pytest.fixture
def file1():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
        }


@pytest.fixture
def file2():
    return {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
        }


def test(file1, file2):
    assert calculate_diff(file1, file2) == {
        'removed': {'proxy', 'follow'},
        'new': {'verbose'}, 'updated': {'timeout'},
        'unchanged': {'host'}
        }
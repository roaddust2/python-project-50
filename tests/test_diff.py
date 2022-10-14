import pytest
from gendiff.diff import generate_diff


@pytest.fixture
def result():
    return "{" + f'''
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
''' + "}"


def test_generate_diff(result):
    assert generate_diff("file1.json", "file2.json") == result
    assert generate_diff("file1.yaml", "file2.yaml") == result
    assert generate_diff("file1.json", "file2.yaml") == result
    assert generate_diff("file1.json", "file2.yml") == result
    assert generate_diff("file1.yaml", "file2.yml") == result

import pytest
from pytest_lazyfixture import lazy_fixture
from gendiff.generate_diff import generate_diff
from tests.fixtures.output import STYLISH, PLAIN, JSON


@pytest.fixture
def json_path1():
    return "./tests/fixtures/file1.json"


@pytest.fixture
def json_path2():
    return "./tests/fixtures/file2.json"


@pytest.fixture
def yaml_path1():
    return "./tests/fixtures/file1.yaml"


@pytest.fixture
def yaml_path2():
    return "./tests/fixtures/file2.yaml"


@pytest.mark.parametrize('path1,path2,format,expected', [
    (lazy_fixture('json_path1'), lazy_fixture('json_path2'), "stylish", STYLISH),
    (lazy_fixture('json_path1'), lazy_fixture('json_path2'), "plain", PLAIN),
    (lazy_fixture('json_path1'), lazy_fixture('json_path2'), "json", JSON),
    (lazy_fixture('yaml_path1'), lazy_fixture('yaml_path2'), "stylish", STYLISH),
    (lazy_fixture('yaml_path1'), lazy_fixture('yaml_path2'), "plain", PLAIN),
    (lazy_fixture('yaml_path1'), lazy_fixture('yaml_path2'), "json", JSON)])
def test_generate_diff(path1, path2, format, expected):
    assert generate_diff(path1, path2, format) == expected

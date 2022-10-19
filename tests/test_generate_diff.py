from gendiff.generate_diff import generate_diff
from tests.output import OUTPUT


def test_generate_diff():
    assert generate_diff(
      "./tests/fixtures/file1.json",
      "./tests/fixtures/file2.json") == OUTPUT
    assert generate_diff(
      "./tests/fixtures/file1.yaml",
      "./tests/fixtures/file2.yaml") == OUTPUT

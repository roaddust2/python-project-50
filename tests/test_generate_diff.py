from gendiff.generate_diff import generate_diff
from tests.output import STYLISH, PLAIN


def test_generate_diff():
    assert generate_diff(
      "./tests/fixtures/file1.json",
      "./tests/fixtures/file2.json") == STYLISH
    assert generate_diff(
      "./tests/fixtures/file1.yaml",
      "./tests/fixtures/file2.yaml") == STYLISH

    assert generate_diff(
      "./tests/fixtures/file1.json",
      "./tests/fixtures/file2.json", "plain") == PLAIN
    assert generate_diff(
      "./tests/fixtures/file1.yaml",
      "./tests/fixtures/file2.yaml", "plain") == PLAIN

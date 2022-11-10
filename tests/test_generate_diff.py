from gendiff.generate_diff import generate_diff
from tests.fixtures.output import STYLISH, PLAIN, JSON


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

  assert generate_diff(
    "./tests/fixtures/file1.json",
    "./tests/fixtures/file2.json", "json") == JSON
  assert generate_diff(
    "./tests/fixtures/file1.yaml",
    "./tests/fixtures/file2.yaml", "json") == JSON

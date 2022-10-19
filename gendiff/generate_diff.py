import gendiff.parse
from gendiff.diff import calculate_diff
from gendiff.formaters.stylish import format


def generate_diff(first_file, second_file):
    first_file = gendiff.parse.choose_parse_type(first_file)
    second_file = gendiff.parse.choose_parse_type(second_file)

    return format(calculate_diff(first_file, second_file))

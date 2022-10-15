import gendiff.parse
import gendiff.diff
import gendiff.formaters.stylish


def generate_diff(first_file, second_file):
    first_file = gendiff.parse.choose_parse_type(first_file)
    second_file = gendiff.parse.choose_parse_type(second_file)

    diff = gendiff.diff.calculate_diff(first_file, second_file)
    return gendiff.formaters.stylish.list_diff(first_file, second_file, diff)

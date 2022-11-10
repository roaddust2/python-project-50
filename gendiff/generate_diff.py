import gendiff.parse
from gendiff.diff import calculate_diff
from gendiff.formaters import select_format


def generate_diff(first_file, second_file, format_name="stylish"):
    first_file = gendiff.parse.choose_parse_type(first_file)
    second_file = gendiff.parse.choose_parse_type(second_file)

    diff = calculate_diff(first_file, second_file)

    format = select_format(format_name)

    return format(diff)

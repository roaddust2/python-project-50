import os.path
from gendiff.parsing import parse
from gendiff.diff import calculate_diff
from gendiff.formaters import select_format


def generate_diff(first_path, second_path, format_name="stylish"):

    old_file, o_ext = read_file(first_path)
    new_file, n_ext = read_file(second_path)

    old_data = parse(old_file, o_ext)
    new_data = parse(new_file, n_ext)

    diff = calculate_diff(old_data, new_data)

    format = select_format(format_name)

    return format(diff)


def read_file(path):
    name, extension = os.path.splitext(path)
    with open(path) as file:
        data = file.read()
        return data, extension[1:]

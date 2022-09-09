import json


def generate_diff(first_file, second_file):
    with open(first_file) as original:
        first_dictionary = json.load(
            original
        )
        with open(second_file) as changed:
            second_dictionary = json.load(
                changed
            )

    return first_dictionary, second_dictionary

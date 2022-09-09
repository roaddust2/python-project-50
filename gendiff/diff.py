import json


def generate_output(list):  # Приведение итера к строке для вывода в консоль
    return


def diff_to_list(diff):  # Выпрямление разницы в итерабельный объект
    return


def calculate_diff(original, changed):
    x, y = set(original), set(changed)

    new = y.difference(x)
    removed = x.difference(y)
    updated, unchanged = set(), set()

    for item in original:
        memory = []
        if item in changed and original[item] != changed[item]:
            memory.append(item)
            updated.update(memory)
        if item in changed and original[item] == changed[item]:
            memory.append(item)
            unchanged.update(memory)

    output = {
        'removed': removed,
        'new': new,
        'updated': updated,
        'unchanged': unchanged,
        }

    return output


def generate_diff(first_file, second_file):
    with open(first_file) as original:
        first_dictionary = json.load(
            original
        )
        with open(second_file) as changed:
            second_dictionary = json.load(
                changed
            )

    diff = calculate_diff(first_dictionary, second_dictionary)
    return diff

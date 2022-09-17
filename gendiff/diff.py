import json


def generate_output(list):
    output = ''

    for item in list:
        output += ' '.join(item) + '\n'
    return '{\n' + output + '}'


def list_diff(original, changed, diff):  # noqa: C901
    output = []

    for key, value in diff.items():
        if key == 'removed':
            for j in value:
                output.append(['-', j + ':', str(original[j])])
        if key == 'new':
            for j in value:
                output.append(['+', j + ':', str(changed[j])])
        if key == 'updated':
            for j in value:
                output.append(['-', j + ':', str(original[j])])
                output.append(['+', j + ':', str(changed[j])])
        if key == 'unchanged':
            for j in value:
                output.append([' ', j + ':', str(original[j])])

    output.sort(key=lambda json_key: json_key[1])

    return output


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
    diff_list = list_diff(first_dictionary, second_dictionary, diff)

    return generate_output(diff_list)

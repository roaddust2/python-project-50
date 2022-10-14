import gendiff.parser
import os.path


PARSE_TYPE = {
    ".json": gendiff.parser.parse_json,
    ".yaml": gendiff.parser.parse_yaml,
    ".yml": gendiff.parser.parse_yaml
}


def choose_parse_type(path):
    name, extension = os.path.splitext(path)
    if extension in PARSE_TYPE:
        return PARSE_TYPE[extension](path)
    else:
        return


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
    first_file = choose_parse_type(first_file)
    second_file = choose_parse_type(second_file)

    diff = calculate_diff(first_file, second_file)
    diff_list = list_diff(first_file, second_file, diff)
    return generate_output(diff_list)

import gendiff.parser
import gendiff.style


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
    first_file = gendiff.parser.choose_parse_type(first_file)
    second_file = gendiff.parser.choose_parse_type(second_file)

    diff = calculate_diff(first_file, second_file)
    return gendiff.style.list_diff(first_file, second_file, diff)

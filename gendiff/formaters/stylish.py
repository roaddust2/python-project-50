MAPPING = {
    "new": ["+", 1],
    "removed": ["-", 0],
    "unchanged": [" ", 0],
    "changed": ["+", 0, "-", 1]
}

SPACE = " "

TEMPLATE = "{0}{1} {2}: {3}"


def format(diff, depth=2):

    output = []

    for key, value in diff.items():
        item_name = key
        item_state = value.get("state")
        item_value = value.get("value")

        if item_state != "node":
            output.append(TEMPLATE.format(
                SPACE * depth,
                MAPPING[item_state][0],
                item_name,
                item_value[MAPPING[item_state][1]]))

        elif item_state == "changed":
            output.append(TEMPLATE.format(
                SPACE * depth,
                MAPPING[item_state][0],
                item_name,
                item_value[MAPPING[item_state][1]]))
            output.append(TEMPLATE.format(
                SPACE * depth,
                MAPPING[item_state][0],
                item_name,
                item_value[MAPPING[item_state][3]]))

        else:
            output.append(TEMPLATE.format(
                SPACE * depth,
                ' ',
                item_name,
                format(
                    value["value"], depth * 2)))

    return generate_output(output)


def generate_output(list):
    output = ''
    list.sort(key=lambda item_key: item_key)

    for item in list:
        output += ''.join(item) + '\n'
    return '{\n' + output + '}'

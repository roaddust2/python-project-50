NEW = "+"
REMOVED = "-"
CHANGED = "+", "-"
UNCHANGED = " "
SPLITTER = ":"
SPACE = " "

TEMPLATE = "{0}{1} {2}: {3}"


def format(diff, depth=2):  # noqa: C901

    output = []

    for key, value in diff.items():
        item_name = key
        item_state = value.get("state")
        item_value = value.get("value")

        if item_state == "new":
            output.append(TEMPLATE.format(
                SPACE * depth, NEW, item_name, str(item_value[1])))
        elif item_state == "removed":
            output.append(TEMPLATE.format(
                SPACE * depth, REMOVED, item_name, str(item_value[0])))
        elif item_state == "changed":
            output.append(TEMPLATE.format(
                SPACE * depth, CHANGED[0], item_name, str(item_value[0])))
            output.append(TEMPLATE.format(
                SPACE * depth, CHANGED[1], item_name, str(item_value[1])))
        elif item_state == "unchanged":
            output.append(TEMPLATE.format(
                SPACE * depth, UNCHANGED, item_name, str(item_value[0])))
        elif item_state == "node":
            output.append(TEMPLATE.format(
                SPACE * depth, ' ', item_name, format(
                    value["value"], depth * 2)))

    output.sort(key=lambda json_key: json_key[1])

    return generate_output(output)


def generate_output(list):
    output = ''

    for item in list:
        output += ''.join(item) + '\n'
    return '{\n' + output + '}'

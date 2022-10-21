MAPPING = {
    "new": "+",
    "removed": "-",
    "unchanged": " ",
    "changed": {
        "style_old": "-", "value_old": 0,
        "style_new": "+", "value_new": 1}
}

SPACE = " "

TEMPLATE = "{0}{1} {2}: {3}"


def format(diff, depth=2):

    output = []

    for key, value in diff.items():
        item_name = key
        item_state = value.get("state")
        item_value = value.get("value")

        if item_state == "changed":
            output.append(TEMPLATE.format(
                SPACE * depth,
                MAPPING[item_state]["style_old"],
                item_name,
                item_value[MAPPING[item_state]["value_old"]]))
            output.append(TEMPLATE.format(
                SPACE * depth,
                MAPPING[item_state]["style_new"],
                item_name,
                item_value[MAPPING[item_state]["value_new"]]))

        elif item_state != "node":
            output.append(TEMPLATE.format(
                SPACE * depth,
                MAPPING[item_state],
                item_name,
                item_value[0]))

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

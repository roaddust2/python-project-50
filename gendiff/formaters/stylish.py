from json import dumps


MAPPING = {
    "new": "+",
    "removed": "-",
    "unchanged": " ",
    "changed": {
        "style_old": "+", "value_old": 0,
        "style_new": "-", "value_new": 1}
}

SPACE, TAB_NUM = " ", 4

TEMPLATE = "{0}{1} {2}: {3}"


def format(diff, depth=1):

    output = ['{']
    start_tab = calc_tabs(depth).get('start_tab')
    end_tab = calc_tabs(depth).get('end_tab')
    new_diff = dict(sorted(diff.items()))

    for key, value in new_diff.items():
        item_name = key
        item_state = value.get("state")
        item_value = value.get("value")

        if item_state == "changed":
            output.append(TEMPLATE.format(
                start_tab,
                MAPPING[item_state]["style_old"],
                item_name,
                generate_string(
                    item_value[MAPPING[item_state]["value_old"]],
                    depth + 1)))
            output.append(TEMPLATE.format(
                start_tab,
                MAPPING[item_state]["style_new"],
                item_name,
                generate_string(
                    item_value[MAPPING[item_state]["value_new"]],
                    depth + 1)))

        elif item_state != "node":
            output.append(TEMPLATE.format(
                start_tab,
                MAPPING[item_state],
                item_name,
                generate_string(item_value[0], depth + 1)))

        else:
            output.append(TEMPLATE.format(
                start_tab,
                ' ',
                item_name,
                format(
                    value["value"], depth + 1)))

    output.append(end_tab + '}')
    return '\n'.join(output)


def calc_tabs(depth):
    tabs = {
        'start_tab': SPACE * (TAB_NUM * depth - 2),
        'end_tab': SPACE * (TAB_NUM * (depth - 1))
    }
    return tabs


def generate_string(node, depth):
    output = []
    start_tab = calc_tabs(depth).get('start_tab')
    end_tab = calc_tabs(depth).get('end_tab')

    if isinstance(node, dict):
        output.append('{')
        for key, value in node.items():
            output.append(TEMPLATE.format(
                start_tab,
                ' ',
                key,
                generate_string(value, depth + 1)
            ))

        output.append(end_tab + '}')
    elif isinstance(node, str):
        output.append(node)
    else:
        output.append(dumps(node))
    return '\n'.join(output)

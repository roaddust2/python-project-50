from json import dumps


MAPPING = {
    "new": "Property '{0}' was added with value: {1}",
    "removed": "Property '{0}' was removed",
    "changed": "Property '{0}' was updated. From {1} to {2}"
}


def format(diff, name=[]):

    output = []
    new_diff = dict(sorted(diff.items()))

    for key, value in new_diff.items():
        item_name = key
        item_state = value.get("state")
        item_value = value.get("value")

        name.append(item_name)

        if item_state == "new":
            output.append(MAPPING[item_state].format(
                '.'.join(name),
                generate_string(item_value[0])))
        
        elif item_state == "removed":
            output.append(MAPPING[item_state].format(
                '.'.join(name)))
        
        elif item_state == "changed":
            output.append(MAPPING[item_state].format(
                '.'.join(name),
                generate_string(item_value[1]),
                generate_string(item_value[0])))

        elif item_state == "node":
            output.append(format(
                value["value"], name))

        name.pop()

    return '\n'.join(output)


def generate_string(node):
    if isinstance(node, str):
        result = f"'{node}'"
    elif isinstance(node, dict):
        result = '[complex value]'
    else:
        result = dumps(node)

    return result
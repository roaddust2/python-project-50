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

    return generate_output(output)


def generate_output(list):
    output = ''

    for item in list:
        output += ' '.join(item) + '\n'
    return '{\n' + output + '}'

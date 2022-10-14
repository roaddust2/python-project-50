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

# Inner view example
#
# {
# "name": {
#   "old_value": old_value
#   "new_value": new_value,
#   "state": removed/new/updated/unchanged,
#   },
# }

def calculate_diff(original, changed):
    diff = {}
    original_keys = set(original.keys())
    changed_keys = set(changed.keys())

    new_keys = changed_keys.difference(original_keys)
    for key in new_keys:
        diff[key] = {
            "old_value": "",
            "new_value": changed[key],
            "state": "new"
        }

    removed_keys = original_keys.difference(changed_keys)
    for key in removed_keys:
        diff[key] = {
            "old_value": original[key],
            "new_value": "",
            "state": "new"
        }

    for key in original_keys.intersection(changed_keys):
        if isinstance(original[key], dict) and isinstance(changed[key], dict):
            diff[key] = calculate_diff(original[key], changed[key])

        elif original[key] == changed[key]:
            diff[key] = {
                "old_value": original[key],
                "new_value": "",
                "state": "unchanged"
            }
        else:
            diff[key] = {
                "old_value": original[key],
                "new_value": changed[key],
                "state": "unchanged"
            }

    return diff

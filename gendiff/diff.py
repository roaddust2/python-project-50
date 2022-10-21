# Inner view example
#
# {
# "name": {
#   "state": node/removed/new/updated/unchanged
#   "value": [value]
#   },
# }

def calculate_diff(original, changed):
    diff = {}

    original_keys = set(original.keys())
    changed_keys = set(changed.keys())

    new_keys = changed_keys.difference(original_keys)
    for key in new_keys:
        diff[key] = {
            "state": "new",
            "value": [changed[key]]
        }

    removed_keys = original_keys.difference(changed_keys)
    for key in removed_keys:
        diff[key] = {
            "state": "removed",
            "value": [original[key]]
        }

    for key in original_keys.intersection(changed_keys):
        if isinstance(original[key], dict) and isinstance(changed[key], dict):
            diff[key] = {
                "state": "node",
                "value": calculate_diff(original[key], changed[key])
            }

        elif original[key] != changed[key]:
            diff[key] = {
                "state": "changed",
                "value": [changed[key], original[key]]
            }
        else:
            diff[key] = {
                "state": "unchanged",
                "value": [original[key]]
            }

    return diff

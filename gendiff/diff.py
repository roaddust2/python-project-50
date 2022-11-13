def calculate_diff(old_data: dict, new_data: dict):
    """Forms inner view (dictionary) of difference between data.

    Keyword arguments:
    old_data - dictionary, which was parsed from a first file
    new_data - dictionary, which was parsed from a second file

    Inner view example:
    {
        "name": {
            "state": node/removed/added/updated/unchanged,
            "value": [value]
            },
    }
    """
    diff = {}

    original_keys = set(old_data.keys())
    changed_keys = set(new_data.keys())

    new_keys = changed_keys.difference(original_keys)
    for key in new_keys:
        diff[key] = {
            "state": "added",
            "value": [new_data[key]]
        }

    removed_keys = original_keys.difference(changed_keys)
    for key in removed_keys:
        diff[key] = {
            "state": "removed",
            "value": [old_data[key]]
        }

    for key in original_keys.intersection(changed_keys):
        if isinstance(old_data[key], dict) and isinstance(new_data[key], dict):
            diff[key] = {
                "state": "node",
                "value": calculate_diff(old_data[key], new_data[key])
            }

        elif old_data[key] != new_data[key]:
            diff[key] = {
                "state": "changed",
                "value": [new_data[key], old_data[key]]
            }
        else:
            diff[key] = {
                "state": "unchanged",
                "value": [old_data[key]]
            }

    return diff

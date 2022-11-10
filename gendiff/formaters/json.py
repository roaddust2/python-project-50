from json import dumps


def format(diff):
    return dumps(diff, indent=2, sort_keys=True)

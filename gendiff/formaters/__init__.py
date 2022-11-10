from gendiff.formaters import stylish, plain, json


FORMATS = {
    'stylish': stylish.format,
    'plain': plain.format,
    'json': json.format}


def select_format(format):
    if format not in FORMATS:
        raise ValueError('Wrong format')
    return FORMATS.get(format)

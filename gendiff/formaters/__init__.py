from gendiff.formaters import stylish, plain


FORMATS = {
        'stylish': stylish.format,
        'plain': plain.format
    }


def select_format(format):
    if format not in FORMATS:
        raise ValueError('Wrong format')
    return FORMATS.get(format)

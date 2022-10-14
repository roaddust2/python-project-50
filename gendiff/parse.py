import json
import yaml
import os.path


def parse_json(path):
    with open(path) as file:
        output = json.load(file)
    return output


def parse_yaml(path):
    with open(path) as file:
        output = yaml.safe_load(file)
    return output


def choose_parse_type(path):
    name, extension = os.path.splitext(path)
    if extension in PARSE_TYPE:
        return PARSE_TYPE[extension](path)
    else:
        print('Error! Only JSON or YAML files are accepted.')
        return


PARSE_TYPE = {
    ".json": parse_json,
    ".yaml": parse_yaml,
    ".yml": parse_yaml
}

import json
import yaml


PARSE_TYPE = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load
}


def parse(file, type):
    data = PARSE_TYPE.get(type)(file)
    return data

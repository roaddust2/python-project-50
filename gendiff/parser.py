import json
import yaml


def parse_json(path):
    with open(path) as file:
        output = json.load(file)
    return output


def parse_yaml(path):
    with open(path) as file:
        output = yaml.safe_load(file)
    return output

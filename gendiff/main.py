#!/usr/bin/env python3
import argparse
from gendiff.diff import generate_diff


parser = argparse.ArgumentParser(
    description="Compares two configuration files and shows a difference."
)
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")
args = parser.parse_args()


def main():
    print(
        generate_diff(args.first_file, args.second_file)
    )
    return


if __name__ == '__main__':
    main()

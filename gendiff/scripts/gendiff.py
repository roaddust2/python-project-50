#!/usr/bin/env python3
from gendiff.scripts.cli import argpaser
from gendiff.generate_diff import generate_diff


def main():
    args = argpaser()

    try:
        print(
            generate_diff(args.first_file, args.second_file, args.format)
        )
    except ValueError:
        print("Fatal error! Please, try again.")
    return


if __name__ == '__main__':
    main()

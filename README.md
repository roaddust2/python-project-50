### Hexlet tests and linter status:
[![Actions Status](https://github.com/roaddust2/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/roaddust2/python-project-50/actions)
[![python](https://github.com/roaddust2/python-project-50/actions/workflows/python.yml/badge.svg)](https://github.com/roaddust2/python-project-50/actions/workflows/python.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/b1c956c8a88f6d95550a/maintainability)](https://codeclimate.com/github/roaddust2/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b1c956c8a88f6d95550a/test_coverage)](https://codeclimate.com/github/roaddust2/python-project-50/test_coverage)

### About The Project
This is small console util written on Python which helps to calculate differnce between two files (supports .json, .yaml, .yml formats).

### How it works
[![asciicast](https://asciinema.org/a/PUzN4kezHeuIy4ykBxWlo2Lml.svg)](https://asciinema.org/a/PUzN4kezHeuIy4ykBxWlo2Lml)

### Getting started
  **Install:**
  ```sh
  sudo apt install python3-pip
  python -m pip install --user git+https://github.com/roaddust2/python-project-50.git
  ```

  **How to use:**
  ```sh
  gendiff file1.json file2.json

  or

  gendiff file1.json file2.json -f stylish
  ```
  ```sh
  gendiff file1.json file2.json -f plain
  ```
  ```sh
  gendiff file1.json file2.json -f json
  ```
  
  **Uninstall:**
  ```sh
  python3 -m pip uninstall hexlet-code
  ``` 

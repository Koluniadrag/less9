import os

def  count_lines(name):
    with open(name, 'r') as file:
        return len(file.readlines())

def count_chars(name):
    with open(name, 'r') as file:
        return len(file.read())

def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"File {name} has {lines} lines and {chars} characters.")






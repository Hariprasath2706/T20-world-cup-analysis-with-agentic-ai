import json

def read_json(file_name):
    with open(file_name, "r") as file:
        return json.load(file)

def print_line():
    print("-------------------------------------")

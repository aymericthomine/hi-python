import json
import sys

input = sys.argv[1]

file = open(input)

data = json.load(file)
file.close()


with open('example.json', 'r') as file:
    data = json.load(file)

data.keys()
data.items()

string = ""

for key in data.keys():

    string = string + "[" + key + "]\n"

    for sub_key in data[key].keys():
        string = string + sub_key + "=" + data[key][sub_key] + "\n"
    string = string + "\n"

with open('example.ini', 'w') as file:
    file.write(string)
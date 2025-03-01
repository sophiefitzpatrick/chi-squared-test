import csv
import json
import os
import pdb


def convert_csv_to_json():
    # read from the input csv
    with open('input.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # return the csv data as json data
    return data

def do_something():
    json_array = convert_csv_to_json()
    for x in json_array:
        # do something
        print(x)

do_something()

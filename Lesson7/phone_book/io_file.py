import csv
import json


def csv_writer(file_name, list_writing):
    with open(file_name, "w", encoding="utf-8", newline='') as w_file:
        file_writer = csv.writer(w_file, delimiter=";")
        file_writer.writerows(list_writing)


def csv_reader(file_name):
    result = []
    with open(file_name, "r", encoding="utf-8") as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for row in file_reader:
            result.append(row)
    return result


def json_writer(file_name, dict_writing):
    with open(file_name, 'w', encoding="utf-8") as outfile:
        json.dump(dict_writing, outfile, ensure_ascii=False)


def json_reader(file_name):
    with open(file_name, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

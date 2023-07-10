import csv
from importlib import resources


def find_ids_in_csv_file():
    print(f"Finding ids in file foo.csv", end="\n\n")
    ids = []
    with resources.files("tryloadresource").joinpath("foo.csv").open("r") as f:
        rows = csv.DictReader(f)
        for row in rows:
            ids.append(row["ID"])
    return ids


def read_csv_file(id):
    print(f"Reading text for id {id}")
    with resources.files("tryloadresource").joinpath("foo.csv").open("r") as f:
        rows = csv.DictReader(f)
        for row in rows:
            if row["ID"] == id:
                return row["Txt"]


def run():
    ids = find_ids_in_csv_file()
    for id in ids:
        print(read_csv_file(id))

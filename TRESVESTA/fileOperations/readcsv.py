import csv

with open("resources/employee.csv","r") as fp:
    for row in csv.DictReader(fp):
        print(row)
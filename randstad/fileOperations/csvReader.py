import csv

d = []

with open("resources/employee.csv","r") as fp:
    for line in csv.DictReader(fp):
        print(line)
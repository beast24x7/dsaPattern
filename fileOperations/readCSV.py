import csv
d = []

with open("resources/employee.csv","r",newline="") as fp:
    for row in csv.DictReader(fp):
        d.append(row)

    print(max(d,key=lambda x: int(x["salary"])))
    print(d)
employees = {
    101: {"name":"Ravi","salary":50000},
    102: {"name":"John","salary":70000},
    103: {"name":"Sam","salary":60000}
}


print(max(employees,key=lambda x:employees[x]["salary"]))


maxSalary1 = 0
e = 0

for emp_id, details in employees.items():
    if details["salary"] > maxSalary1:
        maxSalary1 = details["salary"]
        e = emp_id
print(maxSalary1,e)
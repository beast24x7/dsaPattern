employees = {
    101: {"name":"Ravi","salary":50000},
    102: {"name":"John","salary":70000},
    103: {"name":"Sam","salary":60000}
}

print(max(employees,key=lambda emp_id:employees[emp_id]["salary"]))


print(employees[101]["salary"])
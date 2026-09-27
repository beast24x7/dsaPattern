#Find total failures.

logs =[
 "SUCCESS",
 "FAILED",
 "FAILED",
 "SUCCESS",
 "FAILED"
]
count =0
for i in logs:
    if i == 'FAILED':
        count +=1
print(count)
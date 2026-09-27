s = "python"
start = len(s) -1 
for i in range(start,-1,-1):
    print(s[i],end="")
print()


s1 = "hello world"
# reverse only words 

s1 = s1.split(" ")
l = len(s1) -1 

for i in range(l,-1,-1):
    print(s1[i], end=' ')

count = 0 

with open("resources/input.txt","r") as fp:
    for i in fp:
        count +=1 
print(count)

arr = [0,1,0,2,0,0,0,1]

def moveZero(arr: list):
    fixed = 0 
    for i in range(0,len(arr)):
        if arr[i] != 0:
            arr[i],arr[fixed] = arr[fixed],arr[i]
            fixed += 1
    return arr

print(moveZero(arr)) 


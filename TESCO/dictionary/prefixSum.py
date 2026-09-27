arr = [1, 2, 3]
k = 3

prefix_sum = 0
count = 0

freq = {0: 1}

for num in arr:
    prefix_sum += num

    if prefix_sum - k in freq:
        count += freq[prefix_sum - k]

    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

print(count)

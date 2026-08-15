arr = [1, 2, 2, 3, 1, 2, 4, 3, 3]

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1


print("Frequency:")
print(frequency)

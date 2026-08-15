arr = [4, 5, 1, 2, 1, 5, 4, 3]

frequency = {}

# Count frequency
for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

for num in arr:

    if frequency[num] == 1:
        print("First non-repeating element:", num)
        break

else:
    print("No non-repeating element found")
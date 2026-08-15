arr = [1, 2, 3, 2, 4, 5, 1, 3]

seen = set()
duplicates = set()

for num in arr:

    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)


print("Duplicate elements:")

for num in duplicates:
    print(num)
def two_sum(arr, target):

    numbers = {}

    for i in range(len(arr)):

        current = arr[i]

        needed = target - current

        if needed in numbers:
            return [numbers[needed], i]

        numbers[current] = i
    return []
arr = [2, 7, 11, 15]
target = 9

result = two_sum(arr, target)

print("Array:", arr)
print("Target:", target)
print("Indices:", result)

def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

arr = [10, 5, 25, 8, 30, 15]
result = find_largest(arr)
print("Array:", arr)
print("Largest element:", result)

def move_zeros(arr):
    non_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero] = arr[non_zero], arr[i]
            non_zero += 1
    return arr

arr = [0, 1, 0, 3, 12]

result = move_zeros(arr)

print("Array after moving zeros:", result)

def rotate_left(arr):

    if len(arr) == 0:
        return arr

    first = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[len(arr) - 1] = first
    return arr
arr = [1, 2, 3, 4, 5]

result = rotate_left(arr)

print("Array after left rotation:", result)

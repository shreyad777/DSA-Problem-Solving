
def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    return result
arr = [4, 5, 2, 10, 8]
result = next_greater_element(arr)
print("Array:", arr)
print("Next greater elements:", result)
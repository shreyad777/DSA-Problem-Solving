def find_subarray(arr, target):
    prefix_sum = 0
    seen = {0: -1}
    for i in range(len(arr)):
        prefix_sum += arr[i]
        required = prefix_sum - target
        if required in seen:
            start = seen[required] + 1
            end = i
            return arr[start:end + 1]
        seen[prefix_sum] = i
    return []
arr = [1, 2, 3, 7, 5]
target = 12
result = find_subarray(arr, target)
if result:
    print("Subarray:", result)
else:
    print("No subarray found")
    
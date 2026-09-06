def longest_consecutive(arr):
    numbers = set(arr)
    longest = 0
    for num in numbers:
        if num - 1 not in numbers:
            current = num
            length = 1
            while current + 1 in numbers:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest
arr = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(arr)
print("Longest consecutive sequence length:", result)
# Question 80: Find Majority Element


def majority_element(arr):

    frequency = {}

    # Count frequency
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    # Find majority element
    for num in frequency:

        if frequency[num] > len(arr) // 2:
            return num

    return None


# Example
arr = [2, 2, 1, 1, 1, 2, 2]

result = majority_element(arr)

if result is not None:
    print("Majority element:", result)
else:
    print("No majority element exists")

    
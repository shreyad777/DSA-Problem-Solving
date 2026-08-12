from collections import deque


def first_non_repeating(string):

    frequency = {}
    queue = deque()

    # Count frequencies
    for char in string:

        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1

    # Add non-repeating characters
    for char in string:

        if frequency[char] == 1:
            queue.append(char)

    # Return first non-repeating character
    if queue:
        return queue[0]

    return None


# Test
string = "aabbcdde"

result = first_non_repeating(string)

print("String:", string)
print("First non-repeating character:", result)
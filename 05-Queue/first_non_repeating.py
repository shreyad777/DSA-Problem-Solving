from collections import deque
def first_non_repeating(string):
    frequency = {}
    queue = deque()
    for char in string:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    for char in string:
        if frequency[char] == 1:
            queue.append(char)
    if queue:
        return queue[0]
    return None
string = "aabbcdde"
result = first_non_repeating(string)
print("String:", string)
print("First non-repeating character:", result)
def are_anagrams(s1, s2):

    if len(s1) != len(s2):
        return False

    frequency = {}

    for char in s1:
        frequency[char] = frequency.get(char, 0) + 1

    for char in s2:

        if char not in frequency:
            return False

        frequency[char] -= 1

        if frequency[char] < 0:
            return False

    return True

s1= "listen"
s2 = "silent"

if are_anagrams(s1, s2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
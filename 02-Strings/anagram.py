def are_anagrams(text1, text2):
    if len(text1) != len(text2):
        return False
    frequency1 = {}
    frequency2 = {}
    for char in text1:
        if char in frequency1:
            frequency1[char] += 1
        else:
            frequency1[char] = 1

    for char in text2:

        if char in frequency2:
            frequency2[char] += 1
        else:
            frequency2[char] = 1

    return frequency1 == frequency2


text1 = "listen"
text2 = "silent"

if are_anagrams(text1, text2):
    print("Anagram")
else:
    print("Not an anagram")
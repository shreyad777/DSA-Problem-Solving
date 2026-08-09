def count_vowels_consonants(text):

    vowels = "aeiou"

    vowel_count = 0
    consonant_count = 0

    for char in text:

        if char.lower() in vowels:
            vowel_count += 1

        elif char.isalpha():
            consonant_count += 1

    return vowel_count, consonant_count


text = "hello"

vowels, consonants = count_vowels_consonants(text)

print("String:", text)
print("Vowels:", vowels)
print("Consonants:", consonants)
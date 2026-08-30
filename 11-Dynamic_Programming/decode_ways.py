def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    previous_two = 1
    previous_one = 1
    for i in range(1, len(s)):
        current = 0
        if s[i] != '0':
            current += previous_one

        two_digit = int(s[i - 1:i + 1])

        if 10 <= two_digit <= 26:
            current += previous_two

        previous_two = previous_one
        previous_one = current

    return previous_one

print(num_decodings("226"))
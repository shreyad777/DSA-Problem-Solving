def compress_string(text):
    if not text:
        return ""
    result = ""
    count = 1
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            result += text[i] + str(count)
            count = 1
    result += text[-1] + str(count)
    return result
text = "xxxxxyyzz"
result = compress_string(text)
print("Original string:", text)
print("Compressed string:", result)
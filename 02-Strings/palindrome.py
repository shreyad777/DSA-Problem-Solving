def is_palindrome(text):
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
text = "madam"
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")

class Solution:
    def decodeString(self, s):
        count_stack = []
        string_stack = []
        current_string = ""
        current_number = 0
        for char in s:
            if char.isdigit():
                current_number = (
                    current_number * 10
                    + int(char)
                )
            elif char == "[":
                count_stack.append(current_number)
                string_stack.append(current_string)
                current_number = 0
                current_string = ""
            elif char == "]":
                repeat_count = count_stack.pop()
                previous_string = string_stack.pop()
                current_string = (
                    previous_string
                    + current_string * repeat_count
                )
            else:
                current_string += char
        return current_string
s = input("Enter encoded string: ")
solution = Solution()
print(
    "Decoded String:",
    solution.decodeString(s)
)
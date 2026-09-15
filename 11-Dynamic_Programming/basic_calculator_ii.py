class Solution:
    def calculate(self, s):
        stack = []
        number = 0
        operation = "+"
        for i, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)
            if (not char.isdigit() and char != " ") or i == len(s) - 1:
                if operation == "+":
                    stack.append(number)
                elif operation == "-":
                    stack.append(-number)
                elif operation == "*":
                    stack.append(stack.pop() * number)
                elif operation == "/":
                    previous = stack.pop()
                    stack.append(
                        int(previous / number)
                    )
                operation = char
                number = 0
        return sum(stack)
s = input("Enter expression: ")
solution = Solution()
print("Result:", solution.calculate(s))
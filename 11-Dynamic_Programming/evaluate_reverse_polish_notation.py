class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                else:
                    result = int(first / second)
                stack.append(result)
        return stack[0]
tokens = input("Enter RPN expression: ").split()
solution = Solution()
print("Result:", solution.evalRPN(tokens))
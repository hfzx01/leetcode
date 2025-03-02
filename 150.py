from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', "/"]:
                x = int(stack.pop())
                y = int(stack.pop())
                if i == '+':
                    z = x + y
                elif i == '-':
                    z = y - x
                elif i == '*':
                    z = x * y
                else:
                    z = int(y / x)
                stack.append(z)
            else:
                stack.append(i)
        return int(stack[0])


print(Solution().evalRPN(["4","13","5","/","+"]))
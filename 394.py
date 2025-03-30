class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ''
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            elif s[i] == '[':
                stack.append(num)
                num = ''
            else:
                stack.append(s[i])
            if s[i] == ']':
                left = stack.pop()
                string = ''
                while not left.isdigit():
                    string += left
                    left = stack.pop()
                string = string[:0:-1]
                k = int(left)
                stack.extend(k * list(string))
        return ''.join(stack)
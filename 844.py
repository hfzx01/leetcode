class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        self.delete(s)


    def delete(self, str):
        slow = 0
        fast = 0
        for i in range(len(str)):
            if str[i] == '#':
                str[i-1] = str[i+1]
                slow += 1

            fast += 1
        return str
print(Solution().backspaceCompare("ab#c", "ad#c"))
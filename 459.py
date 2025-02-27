from collections import Counter
class Solution:
    def getnext(self, next, s):
        j = -1
        next[0] = j
        for i in range(1, len(s)):
            while j >=0 and s[i] != s[j+1]:
                j = next[j]
            if s[i] == s[j+1]:
                j += 1
            next[i] = j

    def repeatedSubstringPattern(self, s: str) -> bool:
        nexts = [0] * len(s)
        self.getnext(nexts, s)
        if nexts[-1] != -1 and len(s) % (len(s) - (nexts[-1] + 1)) == 0:
            return True
        else:
            return False


print(Solution().repeatedSubstringPattern("abab"))

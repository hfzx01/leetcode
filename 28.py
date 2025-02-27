class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if needle in haystack:
    #         return haystack.index(needle)
    #     return -1
    # KMP
    def strStr(self, haystack: str, needle: str) -> int:
        def getnext(nexts, s):
            j = -1
            nexts[0] = j
            for i in range(1, len(s)):
                while j >= 0 and s[i] != s[j+1]:
                    j = nexts[j]
                if s[i] == s[j+1]:
                    j += 1
                nexts[i] = j
        nexts = [0]*len(needle)
        getnext(nexts, needle)
        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j+1]:
                j = nexts[j]
            if haystack[i] == needle[j+1]:
                j += 1
            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1
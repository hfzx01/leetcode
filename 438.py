from copy import deepcopy
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(s) < len(p):
            return []
        elif s == p:
            return [0]
        else:
            a = [0] * 26
            b = [0] * 26
            for i in range(len(p)):
                a[ord(s[i]) - ord('a')] += 1
            for i in range(len(p)):
                b[ord(p[i]) - ord('a')] += 1
            if a == b:
                result.append(0)
            for i in range(len(s) - len(p)):
                a[ord(s[i]) - ord('a')] -= 1
                a[ord(s[i + len(p)]) - ord('a')] += 1
                if a == b:
                    result.append(i + 1)
        return result

print(Solution().findAnagrams("abab", "ab"))
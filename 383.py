from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        count = 0
        for key, value in r.items():
            if key in m and m[key] >= value:
                count += 1
        return count == len(r)
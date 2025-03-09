from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = [0] * 26
        index = 0
        result = []
        pre = -1
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] = i
        for i in range(len(s)):
            index = max(index, count[ord(s[i]) - ord('a')])
            if i == index:
                result.append(index-pre)
                pre = index
        return result

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
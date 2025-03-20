class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 1
        result = 1
        while right < len(s):
            if s[right] not in s[left:right]:
                result = max(result, right - left + 1)
                right += 1
            else:
                left += s[left:right].find(s[right]) + 1
        return result
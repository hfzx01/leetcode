class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        dp = [[0] * len(s) for _ in range(len(s))]
        length = 0
        result = s[0]
        for i in range(len(s)-1, -1 ,-1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = 1
                        if j - i > length:
                            length = j - i
                            result = s[i:j+1]
                    elif dp[i+1][j-1]:
                        dp[i][j] = 1
                        if j - i > length:
                            length = j - i
                            result = s[i:j+1]
        return result
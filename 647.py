class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        result += 1
                        dp[i][j] = 1
                    elif dp[i+1][j-1]:
                        result += 1
                        dp[i][j] = 1
        return result

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0]*len(s)
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                if i >= 2:
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = 2
            elif s[i] == ')' and s[i-1] == ')' and s[i-dp[i-1]-1] == '(' and i-dp[i-1] > 0:
                if i-dp[i-1]-2 >= 0:
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                else:
                    dp[i] = dp[i-1] + 2
        return max(dp)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = (len(s)+1)
        dp = [False] * n
        dp[0] = True
        for j in range(n):
            for i in wordDict:
                if j >= len(i):
                    dp[j] = dp[j] or (dp[j-len(i)] and s[j-len(i):j] in wordDict)
        return dp[len(s)]
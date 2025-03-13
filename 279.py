class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        len = int(n ** 0.5)
        for i in range(1, len+1):
            for j in range(i*i, n+1):
                dp[j] = min(dp[j], dp[j - i**2] + 1)
        return dp[n]

print(Solution().numSquares(12))
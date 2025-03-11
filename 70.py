class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0]*3
        dp[1:2] = [1, 2]
        for i in range(3, n + 1):
            sum_ = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = sum_
        return dp[2]
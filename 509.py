# 递归
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return n
#         else:
#             return self.fib(n-1) + self.fib(n-2)
# dp
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0, 1]
        for i in range(2, n+1):
            sum_ = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = sum_
        return dp[1]

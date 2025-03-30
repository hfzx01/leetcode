class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * i for i in range(1, numRows+1)]
        for i in range(numRows):
            if i >= 2:
                for j in range(len(dp[i])):
                    if j - 1 >=0 and j < len(dp[i-1]):
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp
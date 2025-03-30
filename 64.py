class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        count_x = 0
        count_y = 0
        for j in range(len(grid[0])):
            count_x += grid[0][j]
            dp[0][j] = count_x
        for i in range(len(grid)):
            count_y += grid[i][0]
            dp[i][0] = count_y
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
        return dp[-1][-1]
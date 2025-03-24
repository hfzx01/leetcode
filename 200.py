class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(grid, x, y):
            if visited[x][y]:
                return
            visited[x][y] = 1
            for i in range(4):
                next_x = x + directions[i][0]
                next_y = y + directions[i][1]
                if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                    continue
                if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                    dfs(grid, next_x, next_y)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, i, j)
                    result += 1
        return result
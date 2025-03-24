from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        layer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, layer))
                    visited[i][j] = 1
        while q:
            x, y, layer = q.popleft()
            for i, j in directions:
                next_x = x + i
                next_y = y + j
                if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                    continue
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    grid[next_x][next_y] = 2
                    q.append((next_x, next_y, layer+1))
                    visited[next_x][next_y] = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return layer
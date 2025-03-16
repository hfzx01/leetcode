# dfs
# directions = [[0,-1],[0,1],[1,0],[-1,0]]
# n , m = map(int, input().split())
# graph = [[0]*m for _ in range(n)]
# for i in range(n):
#     graph[i] = list(map(int, input().split()))
#
# visited = [[0]*m for _ in range(n)]
# def dfs(graph, x, y):
#     for i in range(4):
#         next_x = x + directions[i][0]
#         next_y = y + directions[i][1]
#         if next_x < 0 or next_x > n-1 or next_y < 0 or next_y > m -1:
#             continue
#         elif not visited[next_x][next_y] and graph[next_x][next_y] == 1:
#             visited[next_x][next_y] = 1
#             dfs(graph, next_x, next_y)
# result = 0
# for i in range(n):
#     for j in range(m):
#         if not visited[i][j] and graph[i][j] == 1:
#             result += 1
#             visited[i][j] = 1
#             dfs(graph, i, j)
# print(result)
# bfs
from collections import deque
directions = [[0,-1],[0,1],[1,0],[-1,0]]
n , m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

visited = [[0]*m for _ in range(n)]
def bfs(graph, x, y):
    queue = deque([[x,y]])
    visited[x][y] = 1
    while queue:
        node_x, node_y = queue.popleft()
        for i in range(4):
            next_x = node_x + directions[i][0]
            next_y = node_y + directions[i][1]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue
            elif not visited[next_x][next_y] and graph[next_x][next_y] == 1:
                visited[next_x][next_y] = 1
                queue.append([next_x, next_y])


result = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            result += 1
            visited[i][j] = 1
            bfs(graph, i, j)
print(result)
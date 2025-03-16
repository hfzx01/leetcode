directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
n, m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))
visited1 = [[0]*m for _ in range(n)]
visited2 = [[0]*m for _ in range(n)]
def dfs(graph, visited, x, y):
    for i in range(4):
        next_x = x + directions[i][0]
        next_y = y + directions[i][1]
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        if not visited[next_x][next_y] and graph[next_x][next_y] >= graph[x][y]:
            visited[next_x][next_y] = 1
            dfs(graph, visited, next_x, next_y)

for i in range(n):
    visited1[i][0] = 1
    dfs(graph, visited1, i, 0)
    visited2[i][m-1] = 1
    dfs(graph, visited2, i, m-1)
for i in range(m):
    visited1[0][i] = 1
    dfs(graph, visited1, 0, i)
    visited2[n-1][i] = 1
    dfs(graph, visited2, n-1, i)
for i in range(n):
    for j in range(m):
        if visited1[i][j] and visited2[i][j]:
            print(str(i) + ' '+ str(j))
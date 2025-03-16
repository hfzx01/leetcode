from collections import deque
directions = [[0,-1],[0,1],[1,0],[-1,0]]
n , m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

visited = [[0]*m for _ in range(n)]
def bfs(graph, x, y):
    queue = deque([[x,y]])
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

def bfs_result(graph, x, y):
    queue = deque([[x,y]])
    while queue:
        node_x, node_y = queue.popleft()
        for i in range(4):
            next_x = node_x + directions[i][0]
            next_y = node_y + directions[i][1]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue
            elif not visited[next_x][next_y] and graph[next_x][next_y] == 1:
                visited[next_x][next_y] = 1
                graph[next_x][next_y] = 0
                queue.append([next_x, next_y])


for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1 and (i == 0 or i == n-1 or j == 0 or j == m-1):
            visited[i][j] = 1
            bfs(graph, i, j)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j] = 1
            graph[i][j] = 0
            bfs_result(graph, i, j)
for i in graph:
    print(' '.join(map(str, i)))

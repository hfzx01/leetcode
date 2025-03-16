from collections import defaultdict
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
n, m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

def dfs(graph, x, y, mask):
    global count
    if visited[x][y]:
        return
    visited[x][y] = 1
    graph[x][y] = mask
    count += 1
    for i in range(4):
        next_x = x + directions[i][0]
        next_y = y + directions[i][1]
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        elif graph[next_x][next_y] == 1:
            dfs(graph, next_x, next_y, mask)
    return count

mask = 2
count = 0
size = defaultdict(int)
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            size[mask] = dfs(graph, i, j, mask)
            mask += 1
            count = 0
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            v = set()
            c = 1
            for k in range(4):
                next_x = i + directions[k][0]
                next_y = j + directions[k][1]
                if next_x < 0 or next_x >= n or next_y < 0 or next_y >=m:
                    continue
                elif graph[next_x][next_y] not in v and graph[next_x][next_y] != 0:
                    c += size[graph[next_x][next_y]]
                    v.add(graph[next_x][next_y])
            result = max(result, c)
# 全陆地
if result == 0:
    print(max(size.values()))
else:
    print(result)
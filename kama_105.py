n, k = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    graph[i-1][j-1] = 1
visited = [0]*n
def dfs(graph, node):
    if visited[node]:
        return
    visited[node] = 1
    for i in range(n):
        if graph[node][i] == 1:
            dfs(graph, i)
dfs(graph, 0)
if all(visited):
    print(1)
else:
    print(-1)
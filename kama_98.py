n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
result = []
path = [0]
def dfs(graph, node, n):
    if node == n-1:
        result.append(path[:])
        return
    for i in range(n):
        if graph[node][i] == 1:
            path.append(i)
            dfs(graph, i, n)
            path.pop()
dfs(graph, 0, n)
if not result:
    print(-1)
else:
    for i in result:
        print(' '.join(map(lambda x: str(x+1), i)))
n, m = map(int, input().split())
graph = [[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int,input().split())
    graph[u][v] = w
    graph[v][u] = w
q = int(input())
plans = []
for i in range(q):
    start, end = map(int, input().split())
    plans.append([start, end])


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for start, end in plans:
    if graph[start][end] == float('inf'):
        print(-1)
    else:
        print(graph[start][end])

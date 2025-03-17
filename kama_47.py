# 朴素dijkstra
# n, m = map(int, input().split())
# visited = [0]*(n+1)
# minDis = [5001] * (n+1)
# minDis[1] = 0
# parent = [-1] * (n+1)
# graph = [[5001]*(n+1) for _ in range(n+1)]
# for i in range(m):
#     s, e, v = map(int, input().split())
#     graph[s][e] = v
# for i in range(1, n+1):
#     min_ = 5002
#     cur = -1
#     for j in range(1, n+1):
#         if not visited[j] and minDis[j] < min_:
#             cur = j
#             min_ = minDis[j]
#     visited[cur] = 1
#     for j in range(1, n+1):
#         if not visited[j] and minDis[cur] + graph[cur][j] < minDis[j]:
#             minDis[j] = minDis[cur] + graph[cur][j]
#             parent[j] = cur
# if minDis[n] == 5001:
#     print(-1)
# else:
#     print(minDis[n])
# 堆优化
import heapq
from collections import defaultdict
n, m = map(int, input().split())
visited = [0]*(n+1)
minDis = [5001] * (n+1)
parent = [-1] * (n+1)
edges = defaultdict(list)
for i in range(m):
    s, e, v = map(int, input().split())
    edges[s].append([e, v])
hq = []
heapq.heappush(hq, (0, 1))
while hq:
    min_, cur = heapq.heappop(hq)
    if visited[cur]:
        continue
    visited[cur] = 1
    for i in edges[cur]:
        if not visited[i[0]] and min_ + i[1] < minDis[i[0]]:
            minDis[i[0]] = min_ + i[1]
            heapq.heappush(hq, (minDis[i[0]], i[0]))
            parent[i[0]] = cur
if minDis[n] == 5001:
    print(-1)
else:
    print(minDis[n])
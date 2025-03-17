# bellman_ford 算法
# n, m = map(int, input().split())
# minDis = [101]*(n+1)
# minDis[1] = 0
# edges = []
# for i in range(m):
#     s, t, v = map(int, input().split())
#     edges.append([s, t, v])
# for i in range(n-1):
#     update = False
#     for edge in edges:
#         if minDis[edge[0]] != 101 and minDis[edge[0]] + edge[2] < minDis[edge[1]]:
#             minDis[edge[1]] = minDis[edge[0]] + edge[2]
#             update = True
#     if not update:
#         break
# if minDis[-1] == 101:
#     print('unconnected')
# else:
#     print(minDis[-1])
# bellman_ford 队列优化 SPFA
from collections import defaultdict,deque
n, m = map(int, input().split())
minDis = [101]*(n+1)
minDis[1] = 0
edges = defaultdict(list)
for i in range(m):
    s, t, v = map(int, input().split())
    edges[s].append([t, v])
visited = [0]*(n+1)
queue = deque([1])
while queue:
    cur = queue.popleft()
    visited[cur] = 0
    for edge in edges[cur]:
        if minDis[cur] != 101 and minDis[cur] + edge[1] < minDis[edge[0]]:
            minDis[edge[0]] = minDis[cur] + edge[1]
            if not visited[edge[0]]:
                visited[edge[0]] = 1
                queue.append(edge[0])
if minDis[-1] == 101:
    print('unconnected')
else:
    print(minDis[-1])
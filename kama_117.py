from collections import deque, defaultdict
n, m = map(int, input().split())
in_degree = [0]*n
umap = defaultdict(list)
result = []
for i in range(m):
    s, t = map(int, input().split())
    in_degree[t] += 1
    umap[s].append(t)
queue = deque([])
for i in range(len(in_degree)):
    if in_degree[i] == 0:
        queue.append(i)
while queue:
    cur = queue.popleft()
    result.append(cur)
    for i in umap[cur]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)
if len(result) == n:
    print(' '.join(map(str,result)))
else:
    print(-1)
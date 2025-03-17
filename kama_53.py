# prim算法
# v, e = map(int, input().split())
# graph = [[10001]*(v+1) for _ in range(v+1)]
# for i in range(e):
#     v1, v2, val = map(int, input().split())
#     graph[v1][v2] = val
#     graph[v2][v1] = val
#
# minDis = [10001]*(v+1)
# visited = [0]*(v+1)
# parent = [0]*(v+1)
#
# for i in range(1, v+1):
#     min_ = 10002
#     cur = 0
#     for j in range(1, v+1):
#         if not visited[j] and minDis[j] < min_:
#             cur = j
#             min_ = minDis[j]
#     visited[cur] = 1
#     for j in range(1, v+1):
#         if not visited[j] and minDis[j] > graph[cur][j]:
#             minDis[j] = graph[cur][j]
#             parent[j] = cur
# print(sum(minDis[2:]))
# kruskal算法
class Unionfind:
    def __init__(self, size):
        self.parent = list(range(size + 1))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            self.parent[v] = u

    def isSame(self, u, v):
        return self.find(u) == self.find(v)


v, e = map(int, input().split())
edges = []
uf = Unionfind(v)
for i in range(e):
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda x: x[2])
result = 0
result_list = []
for i in edges:
    if not uf.isSame(i[0], i[1]):
        result += i[2]
        result_list.append([i[0], i[1]])
        uf.join(i[0], i[1])

print(result)
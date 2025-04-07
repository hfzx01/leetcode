from collections import defaultdict
# https://mp.weixin.qq.com/s/XGWtaW1csuC5gSsI-eWuEg

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
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

n = 5
matrix = [[0, 0, 50, 0, 0],
          [0, 0, 0, 25, 0],
          [50, 0, 0, 0, 15],
          [0, 25, 0, 0, 0],
          [0, 0, 15, 0, 0]]

result = defaultdict(int)
result1 = defaultdict(int)
uf = UnionFind(n)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 0 and not uf.isSame(i, j):
            uf.join(i, j)
            result[(i,j)] = matrix[i][j]
for key, value in result.items():
    result1[uf.find(key[0])] += value
print(result1)
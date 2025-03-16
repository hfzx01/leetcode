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

    def issame(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u == v


n, m = map(int, input().split())
uf = Unionfind(n)
for i in range(m):
    u, v = map(int, input().split())
    uf.join(u, v)
source, destination = map(int, input().split())
if uf.issame(source, destination):
    print(1)
else:
    print(0)

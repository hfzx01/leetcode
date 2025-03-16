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
        return self.find(u) == self.find(v)

n = int(input())
uf = Unionfind(n)
for i in range(n):
    u, v = map(int, input().split())
    if uf.issame(u, v):
        print(str(u)+' '+str(v))
        break
    else:
        uf.join(u, v)
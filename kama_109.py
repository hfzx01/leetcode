from collections import defaultdict
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


def is_tree(edges, edge, n):
    uf = Unionfind(n)
    for i in range(len(edges)):
        if edges[i] == edge:
            continue
        u, v = edges[i]
        if not uf.issame(u, v):
            uf.join(u, v)
        else:
            return False
    return True

def delete_ring(edges, n):
    uf = Unionfind(n)
    for u, v in edges:
        if not uf.issame(u, v):
            uf.join(u, v)
        else:
            print(u, v)

n = int(input())
in_degree = defaultdict(int)
edges = []
for i in range(n):
    u, v = map(int, input().split())
    in_degree[v] += 1
    edges.append([u, v])

vec = []
for u, v in edges:
    if in_degree[v] >= 2:
        vec.append([u, v])

if len(vec) > 0:
    if is_tree(edges, vec[-1], n):
        print(vec[-1][0], vec[-1][1])
    else:
        print(vec[0][0], vec[0][1])
else:
    delete_ring(edges, n)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = [0]
        def dfs(graph, node, n):
            if node == n-1:
                result.append(path[:])
                return
            for i in graph[node]:
                path.append(i)
                dfs(graph, i, n)
                path.pop()
        dfs(graph, 0, len(graph))
        return result
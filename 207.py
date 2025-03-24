from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        grid = {}
        inDegree = [0] * numCourses
        q = deque()
        for i in range(numCourses):
            grid[i] = []
        for u, v in prerequisites:
            grid[v].append(u)
            inDegree[u] += 1
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        result = []
        while q:
            key = q.popleft()
            result.append(key)
            for dst in grid[key]:
                inDegree[dst] -= 1
                if inDegree[dst] == 0:
                    q.append(dst)
        if len(result) == numCourses:
            return True
        else:
            return False
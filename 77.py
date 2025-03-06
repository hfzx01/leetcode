class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def bt(start, n, k):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n - (k - len(path))+2):
                path.append(i)
                bt(i+1, n, k)
                path.pop()
        bt(1, n, k)
        return result
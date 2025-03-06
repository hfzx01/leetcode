class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        sum_ = 0
        def bt(k, n, start, sum_):
            if len(path) == k:
                if sum_ == n:
                    result.append(path[:])
                return

            for i in range(start, 11 - (k - len(path))):
                path.append(i)
                sum_ += i
                if sum_ > n:
                    sum_ -= i
                    path.pop()
                    return
                bt(k, n, i+1, sum_)
                sum_ -= i
                path.pop()
        bt(k, n, 1, sum_)
        return result

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        sum_ = 0
        def bt(candidates, target, start, sum_):
            if sum_ == target:
                result.append(path[:])
                return
            elif sum_ > target:
                return
            for i in range(start, len(candidates)):
                sum_ += candidates[i]
                path.append(candidates[i])
                if sum_ > target:
                    sum_ -= candidates[i]
                    path.pop()
                    return
                bt(candidates, target, i, sum_)
                sum_ -= candidates[i]
                path.pop()
        candidates.sort()
        bt(candidates, target, 0, sum_)
        return result
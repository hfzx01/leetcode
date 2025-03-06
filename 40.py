class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        sum_ = 0
        def bt(candidates, target, start, sum_):
            if sum_ == target:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                sum_ += candidates[i]
                path.append(candidates[i])
                if sum_ > target:
                    sum_ -= candidates[i]
                    path.pop()
                    return
                bt(candidates, target, i + 1, sum_)
                sum_ -= candidates[i]
                path.pop()
        candidates.sort()
        bt(candidates, target, 0, sum_)
        return result
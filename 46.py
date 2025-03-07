class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        visited = []
        def bt(nums):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in nums:
                if i not in visited:
                    visited.append(i)
                    path.append(i)
                    bt(nums)
                    path.pop()
                    visited.pop()
                else:
                    continue
        bt(nums)
        return result
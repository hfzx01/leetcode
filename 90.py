class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def bt(nums, start):
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                else:
                    path.append(nums[i])
                    bt(nums, i+1)
                    path.pop()
        nums.sort()
        bt(nums, 0)
        return result
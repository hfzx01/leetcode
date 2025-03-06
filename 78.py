class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def bt(nums, start):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                bt(nums, i+1)
                path.pop()
        bt(nums, 0)
        return result
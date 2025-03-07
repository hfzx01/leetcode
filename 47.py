class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        visited = [0] * len(nums)

        def bt(nums):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if (i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0) or visited[i] == 1:
                    continue
                else:
                    visited[i] = 1
                    path.append(nums[i])
                    bt(nums)
                    path.pop()
                    visited[i] = 0

        nums.sort()
        bt(nums)
        return result

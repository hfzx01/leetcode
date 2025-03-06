class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = [] 
        def bt(nums, start):
            visited = []
            if len(path) >= 2:
                result.append(path[:])
            for i in range(start, len(nums)):
                if nums[i] not in visited:
                    visited.append(nums[i])
                    if not path:
                        path.append(nums[i])
                        bt(nums, i+1)
                        path.pop()
                    elif nums[i] >= path[-1]:
                        path.append(nums[i])
                        bt(nums, i+1)
                        path.pop()
                    else:
                        continue
                else:
                    continue
        bt(nums, 0)
        return result
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums = set(nums)
        for i in nums:
            if i -1 not in nums:
                count = 1
                while i + 1 in nums:
                    count += 1
                    i += 1
                result = max(result, count)
        return result
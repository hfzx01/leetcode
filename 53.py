class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = 0
        result = float('-inf')
        for i in nums:
            count += i
            if count > result:
                result = count
            if count < 0:
                count = 0

        return result
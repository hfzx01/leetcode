# 贪心 连续和为正继续加，如果为负，重新计数
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         count = 0
#         result = float('-inf')
#         for i in nums:
#             count += i
#             if count > result:
#                 result = count
#             if count < 0:
#                 count = 0
#         return result
# dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)

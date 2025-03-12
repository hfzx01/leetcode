from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        bagweight = sum_ // 2
        m = len(nums)
        dp = [0] * (bagweight+1)
        for i in range(m):
            for j in range(bagweight, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
        return dp[bagweight] == bagweight
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#
#         total_sum = sum(nums)
#
#         if total_sum % 2 != 0:
#             return False
#
#         target_sum = total_sum // 2
#         dp = [False] * (target_sum + 1)
#         dp[0] = True
#
#         for num in nums:
#             # 从target_sum逆序迭代到num，步长为-1
#             for i in range(target_sum, num - 1, -1):
#                 dp[i] = dp[i] or dp[i - num]
#         return dp[target_sum]

print(Solution().canPartition([1,5,11,5]))
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_ = sum(nums)
        if target > sum_:
            return 0
        if (target + sum_) % 2 == 1:
            return 0
        count = (target + sum_) // 2
        dp = [0]*(count+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(count, nums[i]-1,-1):
                dp[j] += dp[j-nums[i]]
        return dp[count]

print(Solution().findTargetSumWays([1,1,1,1,1], 3))
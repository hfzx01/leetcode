from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(target + 1):
            for i in range(len(nums)):
                if nums[i] <= j:
                    dp[j] += dp[j-nums[i]]
        return dp[target]

print(Solution().combinationSum4([1,2,3], 4))
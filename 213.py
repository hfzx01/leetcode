class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * (len(nums)-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        dp1 = [0] * (len(nums)-1)
        dp1[0] = nums[1]
        dp1[1] = max(nums[1], nums[2])
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i+1])
        return max(dp[-1], dp1[-1])
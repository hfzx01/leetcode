from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = [0]*len(nums)
        pre = 0
        result = 0
        mp = defaultdict(int)
        mp[0] = 1
        for i in range(len(nums)):
            pre += nums[i]
            if (pre - k) in mp:
                result += mp[pre - k]
            mp[pre] += 1

        return result
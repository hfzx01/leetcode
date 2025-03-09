class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cover_pre = 0
        cover_cur = 0
        result = 1
        i = 0
        while i <= cover_pre:
            cover_cur = max(cover_cur, i + nums[i])
            if cover_cur >= len(nums) - 1:
                return result
            if i == cover_pre:
                result += 1
                cover_pre = cover_cur
            i += 1

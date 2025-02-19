from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_2_list = list(nums_set) * 2
        for i in nums:
            nums_2_list.remove(i)
        return nums_2_list[0]
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p1 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p1 > p0:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
        return nums
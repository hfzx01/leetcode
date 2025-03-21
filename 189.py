class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums
        elif len(nums) == 1:
            return nums
        if k > len(nums):
            k = k % len(nums)
        cur = nums[-k:]
        for i in range(len(nums)-1, k-1, -1):
            nums[i] = nums[i-k]
        nums[:k] = cur
        return nums
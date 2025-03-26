class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] < nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid
        return -1
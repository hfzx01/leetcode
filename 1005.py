class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k:
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            elif nums[i] == 0:
                break
            elif nums[i] > 0 and i > 0:
                if nums[i] > abs(nums[i - 1]):
                    while k:
                        nums[i - 1] = -nums[i - 1]
                        k -= 1
                else:
                    while k:
                        nums[i] = -nums[i]
                        k -= 1
            else:
                while k:
                    nums[i] = -nums[i]
                    k -= 1
            i += 1
            if i > len(nums) - 1:
                i -= 1
        return sum(nums)
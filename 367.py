class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = 2 ** 16
        while l < r:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False

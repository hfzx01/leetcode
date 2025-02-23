class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = 2 ** 16
        while left < right:
            middle = (left + right) // 2
            if middle * middle > x:
                right = middle
            elif middle * middle < x:
                left = middle + 1
            else:
                return middle
        return left - 1

print(Solution().mySqrt(5))
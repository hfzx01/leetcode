class Solution:
    def isHappy(self, n: int) -> bool:
        result = []
        while n != 1:
            sums = 0
            c = str(n)
            for i in c:
                sums += int(i) ** 2
            if sums not in result:
                result.append(sums)
            else:
                return False
            n = sums
        return True


print(Solution().isHappy(18))
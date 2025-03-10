class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        n = [int(d) for d in str(n)]
        for i in range(len(n)-1, 0, -1):
            if n[i] < n[i-1]:
                n[i:] = [9]*(len(n)-i)
                n[i-1] -= 1
        return int(''.join(map(str, n)))
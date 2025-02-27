class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        def reverse(s):
            s = list(s)
            for i in range(len(s) // 2):
                s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
            return ''.join(s)
        n = len(s) // (2* k)
        r = len(s) % (2*k)
        for i in range(n):
            result += reverse(s[i * 2*k:i*2*k+k])
            result += s[i*2*k+k:i*2*k+2*k]
        if r < k and r != 0:
            result += reverse(s[-r:])
        elif k < r < 2 *k:
            result += reverse(s[-r:-r+k])
            result += s[-r+k:]
        elif k == r:
            result += reverse(s[-r:])
        return result
print(Solution().reverseStr("abcd", 4))
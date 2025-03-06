class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        def bt(s, start):
            if start == len(s):
                result.append(path[:])
                return
            for i in range(start, len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    path.append(s[start:i+1])
                else:
                    continue
                bt(s, i+1)
                path.pop()
        bt(s, 0)
        return result
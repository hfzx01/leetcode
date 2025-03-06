class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = []
        def isvalid(s):
            if s[0] == '0' and len(s) != 1:
                return False
            elif eval(s) >= 0 and eval(s) <= 255:
                return True

        def bs(s, start, path):
            if len(path) == 4:
                if isvalid(path[0]) and isvalid(path[1]) and isvalid(path[2]) and isvalid(path[3]):
                    result.append(path)
                return
            for i in range(start, len(s)):
                path.append(s[start:i+1])
                bs(s, i+1, path)
                path.pop()
        bs(s, 0, path)
        return result


print(Solution().restoreIpAddresses("25525511135"))
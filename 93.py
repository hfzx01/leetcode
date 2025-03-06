class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def isvalid(s):
            if not s or (s[0] == '0' and len(s) != 1):
                return False
            elif int(s) >= 0 and int(s) <= 255:
                return True
            else:
                return False

        def bs(s, start, string, point):
            if point == 3:
                if isvalid(s[start:]):
                    result.append(string + s[start:])
                return
            for i in range(start, len(s)):
                if isvalid(s[start:i+1]):
                    bs(s, i+1, string + s[start:i+1] + '.', point+1)
                else:
                    break
        bs(s, 0, '', 0)
        return result
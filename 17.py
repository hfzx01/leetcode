class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        path = ''
        chars = {'2':'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def bt(digits, path, start):
            if len(path) == len(digits):
                result.append(path)
                return
            char = chars[digits[start]]
            for i in range(len(char)):
                path += char[i]
                bt(digits, path, start+1)
                path =  path[:-1]
        bt(digits, path, 0)
        return result
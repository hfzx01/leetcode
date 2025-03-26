class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        def backtrack(left, right, n):
            if left + right == 2 * n:
                result.append(''.join(path))
            if left < n:
                path.append('(')
                backtrack(left+1, right, n)
                path.pop()
            if right < left:
                path.append(')')
                backtrack(left, right+1, n)
                path.pop()
        backtrack(0, 0 ,n)
        return result
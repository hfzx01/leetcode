class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        path = ['.' * n] * n
        visited = [0]*n
        def isvalid(row, col, q_list, n):
            for i in range(row):
                if q_list[i][col] == 'Q':
                    return False
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if q_list[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if q_list[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def bt(row, path, n):
            if row == n:
                result.append(path[:])
                return
            for i in range(n):
                if isvalid(row, i, path, n):
                    if visited[i]:
                        continue
                    visited[i] = 1
                    path[row] = path[row][:i] + 'Q' + path[row][i + 1:]
                    bt(row + 1, path, n)
                    visited[i] = 0
                    path[row] = path[row][:i] + '.' + path[row][i + 1:]
                else:
                    continue

        bt(0, path, n)
        return result
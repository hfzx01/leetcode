class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[0]*len(board[0]) for _ in range(len(board))]
        def backtrack(x, y, string, index, word):
            if string == word:
                return True
            if index >= len(word):
                return False
            for i, j in directions:
                next_x = x + i
                next_y = y + j
                if next_x < 0 or next_x >= len(board) or next_y < 0 or next_y >= len(board[0]):
                    continue
                if board[next_x][next_y] == word[index] and not visited[next_x][next_y]:
                    visited[next_x][next_y] = 1
                    if backtrack(next_x, next_y, string + word[index], index+1, word):
                        return True
                    visited[next_x][next_y] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if backtrack(i, j, word[0], 1, word):
                        return True
                    visited[i][j] = 0
        return False
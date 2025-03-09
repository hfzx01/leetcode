# 暴力 超时
# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         def isvalid(row, col, board, val):
#             for i in range(9):
#                 if board[i][col] == val or board[row][i] == val:
#                     return False
#             start_row = row//3 * 3
#             start_col = col//3 * 3
#             for i in range(3):
#                 for j in range(3):
#                     if board[start_row + i][start_col+j] == val:
#                         return False
#             return True
#         def bt(board):
#             for i in range(9):
#                 for j in range(9):
#                     if board[i][j] == '.':
#                         for k in map(str, range(1, 10)):
#                             if isvalid(i, j, board, k):
#                                 board[i][j] = k
#                                 if bt(board):
#                                     return True
#                                 board[i][j] = '.'
#                         return False
#             return True
#         bt(board)
# 去重 拼尽全力无法战胜
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    row_used[i].add(board[i][j])
                    col_used[j].add(board[i][j])
                    box_used[(i//3)*3 + j//3].add(board[i][j])


        def bt(row, col):
            if row == 9:
                return True
            if col < 8:
                next_row, next_col = row, col+1
            else:
                next_row, next_col = row+1, 0
            if board[row][col] != '.':
                return bt(next_row, next_col)
            for num in map(str, range(1, 10)):
                if num not in row_used[row] and num not in col_used[col] and num not in box_used[(row//3)*3 + col//3]:
                    board[row][col] = num
                    row_used[row].add(num)
                    col_used[col].add(num)
                    box_used[(row//3)*3 + col//3].add(num)
                    if bt(next_row, next_col):
                        return True
                    board[row][col] = '.'
                    row_used[row].remove(num)
                    col_used[col].remove(num)
                    box_used[(row//3)*3 + col//3].remove(num)
            return False
        bt(0, 0)



print(Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
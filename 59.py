from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []

        for i in range(n):
            line = []
            for j in range(n):
                line.append(0)
            matrix.append(line)
        row1 = 0
        col2 = n - 1
        row3 = n - 1
        col4 = 0
        count = n
        for i in range(2 * n - 1):
            if i % 4 == 0:
                for j in range(count):
                    matrix[row1][col4 + j] = matrix[row1][col4 + j] + j + matrix[row1][col4 - 1] + 1
                row1 += 1
            elif i % 4 == 1:
                count -= 1
                for j in range(count):
                    matrix[row1 + j][col2] = matrix[row1 + j][col2] + j + matrix[row1 - 1][col2] + 1
                col2 -= 1
            elif i % 4 == 2:
                for j in range(count):
                    matrix[row3][col2 - j] = matrix[row3][col2 - j] + j + matrix[row3][col2 + 1] + 1
                row3 -= 1
            else:
                count -= 1
                for j in range(count):
                    matrix[row3 - j][col4] = matrix[row3 - j][col4] + j + matrix[row3 + 1][col4] + 1
                col4 += 1
        return matrix


print(Solution().generateMatrix(4))
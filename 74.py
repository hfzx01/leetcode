class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        for i in range(len(matrix)-1, -1 ,-1):
            if matrix[i][0] < target:
                row = i
                break
            elif matrix[i][0] == target:
                return True
        if row == -1:
            return False
        j = 0
        while j < len(matrix[0]):
            if matrix[row][j] == target:
                return True
            elif matrix[row][j] < target:
                j += 1
            elif matrix[row][j] > target:
                return False
        return False
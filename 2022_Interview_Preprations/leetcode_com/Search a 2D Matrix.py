class Solution:
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        i = 0
        j = cols - 1
        while (0 <= i < rows) and (0 <= j < cols):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
class Solution1:

    def _bSearch(self, elements, target):
        low = 0
        high = len(elements) - 1

        while low <= high:
            mid = (low + high) // 2

            if elements[mid] == target:
                return True
            elif elements[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for row in matrix:
            if self._bSearch(row, target):
                return True
        return False


class Solution2:

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        rows = len(matrix)
        col = len(matrix[0])

        i = 0
        j = col - 1

        while True:
            if i < 0 or i > rows - 1:
                break
            if j < 0 or j > col - 1:
                break

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False



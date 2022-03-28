class Solution:

    def is_validate_rows(self, mat, rows, cols):
        for i in range(rows):
            nums = 0
            A = set()
            for j in range(cols):
                if mat[i][j].isnumeric():
                    A.add(mat[i][j])
                    nums += 1
            if nums != len(A):
                return False

        return True

    def is_valid_cols(self, mat, rows, cols):
        for i in range(cols):
            nums = 0
            A = set()
            for j in range(rows):
                if mat[j][i].isnumeric():
                    A.add(mat[j][i])
                    nums += 1
            if nums != len(A):
                return False
        return True

    def gen_sub_box_start_indexes(self):
        ans = []
        # [
        #     [0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]
        # ]

        for row_sub_box in range(3):
            for col_sub_box in range(3):
                i = row_sub_box * 3
                j = col_sub_box * 3
                ans.append([i, j])
        return ans

    def is_valid_subboxes(self, mat, rows, cols):

        boxes_start_idx = self.gen_sub_box_start_indexes()
        # print(boxes_start_idx)
        for indexes in boxes_start_idx:
            start_i = indexes[0]
            start_j = indexes[1]
            # print(start_i, start_j)
            nums = 0
            A = set()
            for i in range(start_i, start_i + 3):
                for j in range(start_j, start_j + 3):
                    if mat[i][j].isnumeric():
                        A.add(mat[i][j])
                        nums += 1
            if nums != len(A):
                return False
        return True

    def isValidSudoku(self, board):
        # print(self.is_validate_rows(board, 9, 9))
        # print(self.is_valid_cols(board, 9, 9))
        # print(self.is_valid_subboxes(board, 9, 9))

        if not self.is_validate_rows(board, 9, 9):
            return False
        if not self.is_valid_cols(board, 9, 9):
            return False
        if not self.is_valid_subboxes(board, 9, 9):
            return False
        return True

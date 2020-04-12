"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution:

    def isValidIndex(self, i,j,rows, cols):
        if i<0 or i>=rows:
            return False
        if j<0 or j>=cols:
            return False

        return True

    def search(self, board, i, j, rows, cols, word, matchedIndex):

        wordSz = len(word)

        if matchedIndex == wordSz:
            return True

        if not self.isValidIndex(i,j,rows, cols):
            return False

        if board[i][j] != word[matchedIndex]:
            return False

        temp = board[i][j]
        board[i][j] = "#" # if you dont want to restrict already visited comment it

        if self.search(board, i+1, j, rows, cols, word, matchedIndex+1):
            return True
        if self.search(board, i-1, j, rows, cols, word, matchedIndex+1):
            return True
        if self.search(board, i, j+1, rows, cols, word, matchedIndex+1):
            return True
        if self.search(board, i, j-1, rows, cols, word, matchedIndex+1):
            return True

        board[i][j] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        if rows*cols<len(word):
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if self.search(board, i, j, rows, cols, word, 0):
                        return True
        return False

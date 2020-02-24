"""
Given a non-negative integer numRows, generate the first numRows of
 Pascal's triangle.
 Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows: int):
        pascle_list = []
        current_list = []
        current_row = 1
        while current_row<=numRows:
            new_list = [None]*current_row
            new_list[0] = 1
            new_list[-1] = 1
            # print(new_list, current_list)
            for i in range(1,len(current_list)):
                # print(len(current_list))
                new_list[i] = current_list[i] + current_list[i-1]
            pascle_list.append(new_list)
            current_list = new_list[:]
            current_row +=1
        return pascle_list
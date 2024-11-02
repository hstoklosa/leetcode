""" 
PROBLEM:     0036. Valid Sudoku
             https://leetcode.com/problems/valid-sudoku
DIFFICULTY:  Medium 
PATTERN:     Arrays, Hashing (Sets)
"""

class Solution:

    """
    Overview of board indices:

        (0, 0), (0, 1), (0, 2)  (0, 3), (0, 4), (0, 5)
        (1, :), (1, :), (1, :)  (1, 3), (1, :), (1, :)        |
        (2, :), (2, :), (2, :)  (2, 3), (2, :), (1, :) 

        (3, 0), (3, 1), (3, 2)            
        (4, :), (4, :), (5, :)            |                   |
        (5, :), (5, :), (5, :)            
                        
        
                |                         |                   |
        
    Calculation to determine which 3x3 box the current (i, j) belongs to:

        - (i // 3) * 3 -> calculate row of a box (considering combined rows)

        - j // 3 -> calculate box position on a certain row (offset) 

        - ((i // 3) * 3) + j // 3 -> calculate exact box number (0-indexed)

    Optimised solution:
        - create sets before iterations
        - ignore all dots (doesn't affect algorithm)
        - replace complex offset logic with box number calculation ^^
        - utilise sets created beforehand to check for duplicates in rows/cols
          instead of converting from lists to sets during iterations
    """

    # OPTIMISED SOLUTION 
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)

        boxes = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        rows = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                curr_value = board[i][j]

                if curr_value == ".":
                    continue

                curr_box = ((i//3) * 3) + j//3

                if (
                    curr_value in rows[i] or
                    curr_value in cols[j] or
                    curr_value in boxes[curr_box]
                ):
                    return False
                
                rows[i].add(curr_value)
                cols[j].add(curr_value)
                boxes[curr_box].add(curr_value)
   
        return True

    def _isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)

        for i in range(n):
            box_elements = set()
            row, col = [], []

            offset = 0
            for j in range(n):
                if i == 0 or i == 3 or i == 6: 
                    col_x, col_y, col_z = (
                        board[i+offset][j], 
                        board[i+offset+1][j], 
                        board[i+offset+2][j] 
                    )
                
                    if (col_x in box_elements or
                        col_y in box_elements or
                        col_z in box_elements
                    ): 
                        return False 
                    
                    if col_x != ".": box_elements.add(board[i][j])
                    if col_y != ".": box_elements.add(board[i+1][j])
                    if col_z != ".": box_elements.add(board[i+2][j])
                    
                if (j + 1) % 3 == 0:
                    box_elements = set()

                if (i + 1) % 3 == 0:
                    offset += 3

                curr_row_element = board[i][j]
                if curr_row_element != ".": 
                    row.append(curr_row_element)
                
                curr_col_element = board[j][i]
                if curr_col_element != ".": 
                    col.append(curr_col_element)
            
            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False
   
        return True
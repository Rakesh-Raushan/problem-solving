class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #let's do the brute force check
        from collections import Counter
        #first all rows
        for row in board:
            count_map = Counter(row)
            for digit in count_map:
                if count_map[digit] > 1 and digit != ".":
                    return False
        #next all cols
        for i in range(9):
            col_i = [row[i] for row in board]
            count_map = Counter(col_i)
            for digit in count_map:
                if count_map[digit] > 1 and digit != ".":
                    return False
        
        #next all sub3x3 blocks
        subblock_starts = []
        for i in [0,3,6]:
            for j in [0,3,6]:
                subblock_starts.append([i,j])
        
        for start_i, start_j in subblock_starts:
            subblock_digits = []
            for i in range(start_i, start_i+3):
                for j in range(start_j, start_j+3):
                    subblock_digits.append(board[i][j])
            count_map = Counter(subblock_digits)
            for digit in count_map:
                if count_map[digit] > 1 and digit != ".":
                    return False
        
        return True



                

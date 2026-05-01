class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #simple idea is to use a hashmap and iterate through the board
        #we can keep three hashmaps to check if we have seen a value in the same row or same col or same 3x3
        #as we traverse the board
        rows_dict = collections.defaultdict(set) #key row, value- set of seen vals
        cols_dict = collections.defaultdict(set) #key col, value- set of seen vals
        grid_dict = collections.defaultdict(set) #key (grid row, grid col), value - set of seen vals in that grid

        #we can map the grid as; grid row = board row //3 and grid col = board col //3

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    #vacant cell
                    continue
                if (board[row][col] in rows_dict[row] or 
                board[row][col] in cols_dict[col] or 
                board[row][col] in grid_dict[(row//3, col//3)]):
                    #has been seen in the row or has been seen in col or has been seen in same 3x3
                    return False
                #otherwise add them to seen sets for row, col and grid 3x3
                rows_dict[row].add(board[row][col])
                cols_dict[col].add(board[row][col])
                grid_dict[(row/3, col//3)].add(board[row][col])
        
        return True
        
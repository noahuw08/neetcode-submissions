class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force: O(n^2)
            # iterate over each list (each row of the board), then within each row, iterate over each column and check if all requirements are satisfied
        
        # more optimal soln:
        # 1. we know that it's valid if each row contains no duplicates,
        # 2. each col contains no duplicates, 3. and each each 3x3 box contains no duplicate
            # so we need some sort of mechniasm to be able to "lookback" at it as we traverse.
            # each constraint here requires a different traversal path.
        
        # for constraint 1.
            # traversal over each board[i] , and a hashmap for each
        
        # for constraint 2.
            # traversal over board[j][0], and a hashmap for each
        
        # for constraint 3.
            # traversal over board[i][]
        
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        grid_3x3 = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row_set[r]) or (board[r][c] in col_set[c]) or (board[r][c] in grid_3x3[(r // 3, c // 3)]):
                    return False
                else:
                    row_set[r].add(board[r][c])
                    col_set[c].add(board[r][c])
                    grid_3x3[(r // 3, c // 3)].add(board[r][c])
        return True 



                








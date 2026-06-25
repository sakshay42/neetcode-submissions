class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        """
        keep track of elts in a row, col, 3x3 square
        - uniques -> store as sets
        row_dict = {i: set(elts)}
        col_dict = "
        subsquare = {(0,0): set(),....}

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num in row_dict[i] or num in col_dict[j]
                
                or num in subsquare[(i//3,j//3)]:
                    return False
                
                row_dict[i].add(num)
                col_dict[i].add(num)
                subsquare[(i//3,j//3)].add(num)
        return False
                

        """
        row_dict = {}
        col_dict = {}
        subsquare = {}
        for i in range(9):
            row_dict[i] = set()
            col_dict[i] = set()
        
        for i in range(3):
            for j in range(3):
                subsquare[(i,j)] = set()


        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if (num in row_dict[i]) or (num in col_dict[j]):
                    return False
                if num in subsquare[(i//3,j//3)]: 
                    return False
                
                row_dict[i].add(num)
                col_dict[j].add(num)
                subsquare[(i//3,j//3)].add(num)
        return True

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        cols = set()
        rows = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    cols.add(j)
                    rows.add(i)
        for i in range(m):
            if i in rows:
                matrix[i] = [0]*n
        for j in range(n):
            if j in cols:
                for i in range(m):
                    matrix[i][j]=0
        
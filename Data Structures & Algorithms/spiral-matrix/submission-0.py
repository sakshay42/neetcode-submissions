class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0,n-1
        ans = []
        while top<=bottom and left<= right:
            for j in range(left, right+1):
                ans.append(matrix[top][j])
            for i in range(top+1, bottom+1):
                ans.append(matrix[i][right])
            if top != bottom:
                for j in range(right-1, left-1,-1):
                    ans.append(matrix[bottom][j])
            if left != right:       
                for i in range(bottom-1, top,-1):
                    ans.append(matrix[i][left])
            top+=1
            bottom-=1
            left+=1
            right-=1
        return ans
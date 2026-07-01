class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        m+n-2 choose n-1
        we can start with n-1Cn-1 and move to m+n-2 choose n-1
        n-1+k+1C n-1 = (n-1+k)/k n-1+k-1Cn-1
        """
        ans = 1
        for i in range(1,m):
            ans = (ans * (n-1+i))//i
        return ans
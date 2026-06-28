class Solution:
    def climbStairs(self, n: int) -> int:
        """

        a_n  = a_n-1 + a_n-2
        a_0 = 0
        a_1 = 1
        a_2 = 2

        """
        if n<= 2:
            return n
        a,b = 1,2
        for i in range(n-2):
            a,b = b,a+b
        return b
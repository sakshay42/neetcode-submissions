class Solution:
    def countBits(self, n: int) -> List[int]:

        """
        10101000
        d= # num of bits
        f(d-1) = all d-1 sequences are allowed -> so 2^(d-2) (d-1) ones there
        f(3) + f(5) + f(7)
        """
        dp = [0,1]
        if n<=1:
            return dp[:n+1]
        for i in range(2, n+1):
            ans = dp[i//2]
            ans +=1 if i%2 == 1 else 0
            dp.append(ans)
        return dp

        
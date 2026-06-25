class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        ans = 0
        for i in prices:
            if i < low:
                low = i
            ans = max(ans, i-low)
        return ans
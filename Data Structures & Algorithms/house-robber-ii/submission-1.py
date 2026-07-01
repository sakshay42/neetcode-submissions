class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        """
        solve house robber 1 - f 
        ans is max(f(nums[1:n-1]), f(nums[1:]))
        """
        def robber(arr):
            if len(arr)==1:
                return arr[0]
            dp = [0]*len(arr)
            dp[0]=arr[0]
            dp[1] = max(arr[0],arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(arr[i]+dp[i-2], dp[i-1])
            return dp[-1]
        
        return max(robber(nums[1:]), robber(nums[:len(nums)-1]))
    
            

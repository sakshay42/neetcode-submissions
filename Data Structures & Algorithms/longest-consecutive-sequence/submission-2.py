class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        dictionary = {v:what is the longest cons seq ending at i}
        
        for i in nums:
            dictionary[i] = dictionary[i-1]+1
            ans = max(ans, len(dictionary[i]))
        
        return ans
            


        """

        nums_set = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in nums_set:
                l = 1
                while i+1 in nums_set:
                    l+=1
                    i+=1
                ans = max(ans,l)
        return ans
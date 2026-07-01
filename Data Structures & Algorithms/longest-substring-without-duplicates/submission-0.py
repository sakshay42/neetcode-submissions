class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        use sliding window
        
        """
        ans = 0
        window = set()
        left =0 
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            ans = max(ans, right-left+1)
        return ans
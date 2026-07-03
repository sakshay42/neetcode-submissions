class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        """
        for each find the longest palindromic substring centered aroun i
        O(n^2)

        """
        n = len(s)
        

        def centered_palindrome(idx):
            ans = ""
            ## even palindrome
            left= idx-1
            right = idx
            while left >=0 and right <n:
                if s[left]==s[right]:
                    ans = s[left:right+1]
                    left-=1
                    right+=1
                else: 
                    break

            ## odd palindrome
            left = idx
            right =idx
            while left>=0 and right <n:
                if s[left]==s[right]:
                    if len(ans) < right-left+1:
                        ans = s[left:right+1]
                    left-=1
                    right+=1
                else: 
                    break
            return ans
        longest_palindrome = ""
        for i in range(len(s)):
            if len(longest_palindrome)< len(centered_palindrome(i)):
                longest_palindrome = centered_palindrome(i)
        return longest_palindrome        


           


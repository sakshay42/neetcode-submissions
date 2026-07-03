class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def centered_palindrome(idx):
            ans = 0
            # odd length
            left= idx-1
            right = idx
            while left>= 0 and right < n:
                if s[left] == s[right]:
                    ans +=1
                    left-=1
                    right +=1
                else:
                    break
            ## even length
            left = idx
            right = idx
            while left>=0 and right< n:
                if s[left]==s[right]:
                    ans+=1
                    left-=1
                    right+=1
                else:
                    break
            return ans
        total = 0
        for i in range(n):
            total += centered_palindrome(i)
        return total
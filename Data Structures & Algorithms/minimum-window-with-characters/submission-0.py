class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s = "OUZODYXAZV", t = "XYZ"

        do sliding window - keep a dictionary of frequencies
        window = {X: , Y: , Z:}
        if window_freq > t_freq -> valid window
        move left and see if we can find smaller window
            if window_freq ==0:
            move left
        """
        window = defaultdict(int)
        length = float("inf")
        t_freq = Counter(t)
        for i in t_freq:
            window[i] = 0
        
        def valid_window(freq):
            for i in t_freq:
                if freq[i] < t_freq[i]:
                    return False
            return True



        left = 0
        ans = ""
        for right in range(len(s)):
            if s[right] in t_freq:
                window[s[right]]+=1
                while valid_window(window):
                    if right-left+1 < length:
                        ans = s[left:right+1]
                        length = right-left+1
                    if s[left] in t_freq:
                        window[s[left]]-=1
                     
                    left+=1

                
        return ans
        


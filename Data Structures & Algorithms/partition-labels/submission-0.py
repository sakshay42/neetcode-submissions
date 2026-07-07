class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = defaultdict(int)
        for idx, val in enumerate(s):
            last[val] = idx
        
        end = last[s[0]]
        ans = []
        curr = 0
        for i in range(len(s)):
            if i <= end:
                end = max(end, last[s[i]])
            else:
                ans.append(end-curr+1)
                end = last[s[i]]
                curr = i
            if i== len(s)-1:
                ans.append(end-curr+1)
        return ans
        

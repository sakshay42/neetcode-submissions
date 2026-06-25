class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for i in strs:
            encoded.append(str(len(i)))
            encoded.append("#")
            encoded.append(i)
            
        return "".join(encoded)
    
    def decode(self, s: str) -> List[str]:
        ans = []
        while s:
            for i in range(len(s)):
                if s[i]=="#":
                    n = int(s[:i])
                    ans.append(s[i+1:i+n+1])
                    s = s[i+n+1:]
                    break
        return ans
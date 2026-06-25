class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tracker = defaultdict(list)
        for word in strs:
            tracker[tuple(sorted(word))].append(word)
        ans = []
        for i in tracker:
            ans.append(tracker[i])
        return ans
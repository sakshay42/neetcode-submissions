class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        curr = intervals[0]
        i = 0 
        ans = []
        while i < n:
            if max(intervals[i][0], curr[0]) <= min(intervals[i][1],curr[1]):
                curr = [min(intervals[i][0], curr[0]),max(intervals[i][1],curr[1])]
                
            else:
                ans.append(curr)
                curr = intervals[i]
            if i==n-1:
                    ans.append(curr)
            i+=1

        return ans


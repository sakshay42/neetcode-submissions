class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        def left_insert_point(a):
            left = 0
            right = n-1
            ans = n
            while left<=right:
                mid = (left+right)//2
                x,y = intervals[mid]
                if a<=y:
                    ans = mid
                    right = mid-1
                else:
                    left = mid+1
            return ans
        
        
        i = left_insert_point(newInterval[0])
        

        if i==n:
            intervals.append(newInterval)

            return intervals
        
        ans = intervals[:i]
        merged = newInterval
        first = False
        for k in range(i,n):
            if max(merged[0],intervals[k][0])<= min(merged[1],intervals[k][1]):
                merged = [min(merged[0],intervals[k][0]),max(merged[1],intervals[k][1])]
            else:
                if not first:
                    first = True
                    ans.append(merged)
                ans.append(intervals[k])
        if not first:

            ans.append(merged)
        return ans



                     
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        n = len(temperatures)
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1]-i)
            stack.append(i)
        ans.reverse()
        return ans
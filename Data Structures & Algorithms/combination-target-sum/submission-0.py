class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        (subset array, index -what is the index I have to decide now, curr)
        """
        ans = []
        n = len(nums)
        def backtrack(subset, idx, curr_sum):
            if curr_sum > target:
                return 
            if curr_sum == target:
                ans.append(subset[:])
                return
            if idx == n:
                return 

            subset.append(nums[idx])
            backtrack(subset, idx, curr_sum+nums[idx])
            subset.pop()

            backtrack(subset, idx+1, curr_sum)
            return 

            
        
        backtrack([],0, 0)
        return ans
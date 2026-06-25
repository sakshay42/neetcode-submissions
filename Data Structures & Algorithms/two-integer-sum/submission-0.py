class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elt_idx = defaultdict(int)
        for idx, val in enumerate(nums):
            if target-val in elt_idx:
                return [elt_idx[target-val],idx]
            elt_idx[val] = idx
        
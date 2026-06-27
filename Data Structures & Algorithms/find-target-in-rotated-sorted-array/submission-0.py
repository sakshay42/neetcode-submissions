class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        search for min elt then search on right or search on left

        [first....Max , Min.... last]
        if num in first to max, search here
        else:
            search the tail
        """

        def find_min():
            left = 0
            right = len(nums) - 1
            ans = 0
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= nums[-1]:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        min_idx = find_min()

        def bs(arr):
            left = 0
            right = len(arr) - 1
            ans = float("inf")

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] >= target:      # lower_bound
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if ans == float("inf") or arr[ans] != target:
                return -1
            return ans

        if nums[min_idx] <= target <= nums[-1]:
            idx = bs(nums[min_idx:])
            if idx == -1:
                return -1
            return idx + min_idx
        else:
            return bs(nums[:min_idx])
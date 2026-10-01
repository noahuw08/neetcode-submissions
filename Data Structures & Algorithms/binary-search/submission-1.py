class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # intuition:
        # init two pointers: one leftmost, one rightmost. And a midpoint
        # start at midpoint. if the midpoint value < target, eliminate everything from midpoint to the left. Update left to index to the right of midpoint
            # otherwise if midpoint > target, eliminate everything from midpoint to the right. Update right to the index to the left of midpoint.
        # repeat this procedure
        # end the repetitive process when midpoint == 0 (meaning there's only 1 element in the search)
            # if it equals target, return that index. otherwise -1.
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1





        
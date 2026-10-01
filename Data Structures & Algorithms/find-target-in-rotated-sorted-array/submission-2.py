class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # [3,4,5,6,1,2]
        # [5,6,1,2,3,4], target = 4
        # [9,10,1,2,3,4,5,6,7,8], target = 6
        # [4,5,6,7,8,9,10,1,2,3], target = 6
        # [4,5,6,7,8,9,10,1,2,3], target = 2
        

        # condition to eliminate half of the search space:
        # first we need to understand  that the target could appear in these areas:
            # 1. at the left, right, or mid pointers
            # 2. within the fully sorted area, or
            # 3. within the rotated sorted area (containing the rotation)
            # if the target dont appear in either 2. or 3., we eliminate one and search in the other.

            # target in fully sorted area: 
                # nums[l] < target < nums[m]
            # target in the rotated sorted area:
                # else
            # at any iteration, if the target is at the left, right, or mid, we return that index right away and break out of the loop.
            # otherwise after all iterations if we can't find the target, return -1.
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # for each half sorted, there're 2 scenarios:
                # 1. either the target is within the range of that half,
                # 2. or it's in the other half.

            # for left half sorted:
            if nums[l] < nums[m]:
                if nums[l] < target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # for right half sorted
            else:
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
            
            





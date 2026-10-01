class Solution:
    def findMin(self, nums: List[int]) -> int:
        # trivial case is normal sort the rotated sorted array, then do a binary search. But the sort alone would take O(n) time worst case. Or a min() to return min right away but this also takes O(n) time.


        # [3,4,5,6,1,2]
        # [6,1,2,3,4,5]
        # [4,5,6,1,2,3]
        # [2,3,4,5,6,1]
        # [1,2,3,4,5,6]
        # [4,5,6,7,8,9,10,1,2,3]
        # [9,10,1,2,3,4,5,6,7,8]

        # in a rotated sorted array, there's a special property: one part is always sorted, while the other part contains the rotation (which means the minimum element is there).
            # for a binary search here, if the left half is sorted, we know the minimum can't be there, and search the right half
                # the left half is sorted  when nums[l] < nums[r]
            # if the right half is sorted, then the minimum must be in the left half or at the midpoint

        # idea is that, since the array is not fully sorted, we need to do min() between 2 elements to keep track of the curr min element every time.

        # in a rotated sorted array, if nums[l] < nums[r], then we know that the array is fully sorted. otherwise it's still a rotated sorted one.

        # init 2 pointers
        res = nums[0]
        l, r = 0, len(nums) - 1

        # start our binary search for rotated sorted array
        while l <= r:
            # if this is true, it means the whole array area we're looking at is fully sorted, so the min element would be at nums[l]. More concisely, it's the mininum between the curr min element and nums[l]
            if nums[l] <= nums[r]: 
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])     # compare curr min with the midpoint value, whichever smaller gets updated
            # if nums[m]  >= nums[l], it means the left half is sorted, meaning the rotation point (containing the min element) is not there, and we search for the right half
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


    



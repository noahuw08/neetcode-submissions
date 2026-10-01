class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers. even though it seems like we need to keep track of 3 values, but the 3rd one could just be deduced from the other two.
        # which two pointers?
        # since the desired triplets could just be any 3 numbers anywhere in the array, we need to sort the array.
        # ex: [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]

        # intuition:
        # after sorting the array, fix one number, use two pointers to track the other two. 
        # two pointers makes it very easy to skip duplicates (pointers keep moving)
        # two pointers ensure that moving the left or right pointer will increase or decrease the sum in a predictable way (given array sorted).

        # fix one number. 
            # and two pointers, left pointer right after the fixed number, right pointer starts at the end.
            # if the sum is too large, then move right pointer to the left to reduce (sicne array is sorted)
            # if the sum is too small, move left pointer to the right to increase
            # if the sum is 0, record the triplets.
        
        res = []
        nums.sort()

        # enumerate for loop since we need to access both the value (of fixed number) and its index as well
        for i, n in enumerate(nums):
            # more optimized, if the current num is > 0 then break out of the for loop right away (since num is left most of the 3 indices in a sorted array, if num > 0 then obv the 2 pointers' values are also > 0)
            if n > 0:
                break
            # the 2nd duplicate edge case: the 1st one is dupl related to pointers (within a fixed number), this one is related to the fixed number.
            if i > 0 and n == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + n == 0:
                    res.append([nums[l], nums[r], n])
                    l, r = l + 1, r - 1
                    # 1st duplicate edge case: after the append of the desired triplets, we move both pointers. if this new pointer's value is the same as the previous pointer's value, we need to keep on moving this pointer until it's not a duplicate.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + n > 0:
                    r = r - 1
                elif nums[l] + nums[r] + n < 0:
                    l = l + 1
        return res


# [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]

# [-4, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 2]





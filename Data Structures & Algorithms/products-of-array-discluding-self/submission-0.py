class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # in order to return product of all ele of nums for each index of the output except that same index of the nums array,
        
        # non optimal soln woulud be in O(n^2) time complexity. for each product ele in the output we'd have to traverse thru the whole array to compute the product.
        # in order to achieve O(n) time, we only want to traverse through the array once

        # prefix & suffix:
            # for each index of the result arr, we need product of all elements before it and all elements after it
            # so we need an array that handle everything before it
            # and an array that handle everything after it
            # result of each product ele would be sth like:
                # pref[i] * suff[i] -> product of all elements before i AND all elements after i

        
        # steps:
            # first 2 steps follow the same algo setup for the prefix sum algo
        # 1st step: init the output array ssame size as the input array. same with pref and suff
        n = len(nums)
        res = [1] * n
        pref = [1] * n
        suff = [1] * n

        # 2nd step: assign first element of both pref and suff array to 1
            # reason is we need to multiply starting from 1 for each of the pref and suff array separately before multplying them at the end for the result
        pref[0] = suff[n-1] = 1

        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]     # each pref element is the product of everything before each i
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]     # each suff element is the product of everything after each i
        for i in range(n):
            res[i] = pref[i] * suff[i]      # each result element is just the product of everything before i AND after i
        return res



        



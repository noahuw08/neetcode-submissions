class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we need to calc the minimum banana eating rate k to finish all bananas within h hours.

        # idea:
        # each hour h you choose a pile of bananas and eat k bananas.
            # ** BUT if that pile has less than k bananas you can finish eating the pile BUT you cant eat from another pile in the same hour

        # algo:
            # two constraints:
            # 1. the rate k always has to be <= h
            # 2. keep iterating from 1 to h, while k > h then keep incrementing the i to keep searching for the k that would satisfy constraints. (turn into k <= h)

        # brute force:
        # iterate through each pile and accumulate the total time for each pile then total time for all piles then compare with h, while k > h , increment the k. return the first k that <= h.

        # k = 1
        # # while the total eating time > h we keep going until we find the k that would make total eating time <= h
        # while True:
        #     mink = 0
        #     for p in piles:
        #         mink += math.ceil(p / k)
        #     if mink <= h:
        #         return k
        #     k += 1
        # return k

        # brute force solution doens't pass the edge cases


        # optimal solution:
        # intuition:
            # notice that the search space for k should go from 1 to max(piles)
            # max(piles) means that Koko will finish eating one pile in at most one hour
            # and any rate of eating k greater than max(piles) would be the same for Koko, an since we want to get the minimum k so he can eat all bananas within h hours, there's no point in finding any k > max(piles)
        
        # we can search for the minimum k that Koko can eat all bananas within h hours by binary search. Intuition:
        # Find a comparison to eliminate half of the search space. Instead of searching for an element, think about feasible answers: if this is the value of k, is this feasible based on our constraints?
        # our constraint: if with this k, total pile eating time > h, move left pointer inward. (because we need to find larger eating speed k to reduce the total eating time)
        # elif with this k, total pile eating time <= h, move right pointer inward (since total eating time still within h hours, then keep finding smaller and smaller eating speed to eventually find the smallest one that still make total eating time <= h)

        l, r = 1, max(piles)
        k = 0
        min_k = 0
        while l <= r:
            # the midpoint searches for each possibly feasible eating speed k
            k = (l + r) // 2
            eating_time = 0
            # for each eating speed, calc the total eating time
            for p in piles:
                eating_time += math.ceil(p / k)
            if eating_time <= h:
                # keep track of the curr minimum eating speed k
                min_k = k
                r = k - 1
            else:
                l = k + 1
        return min_k

        

        
        
            



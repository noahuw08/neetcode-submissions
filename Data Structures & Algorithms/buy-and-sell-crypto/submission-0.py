class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # a dynamic sliding window pattern problem (subproblem of a two pointer)
            # we choose a single day to buy, and choose any different day in the future to sell -> size isn't fixed, its dynamic.

        
        # intuition:
        # init the max profit as 0
        # profit = sell - buy
            # sell is alwasy in the future after buy

        # init the left and right pointer at the same index
        # loop over the right pointer
            # if the right pointer < left pointer (meaning we find a sell smaller than buy), we update it as the left pointer since now we find a cheaper buy.
            # otherwise, keep moving the right pointer
            # at each iteration  we keep track of the max profit. if r < l, 


        # [1,5,6,10,7,1]

        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                curr_profit = prices[r] - prices[l]
                if curr_profit >= max_profit:
                    max_profit = curr_profit
                r += 1
        return max_profit
        












class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        # "abcdbyz"
        
        # to find the longest substring without repeating chars:
            # need a window to keep track of the length so far,
            # sth to "lookback" to check if a char is repeated -> a hash set
        
        # for the window:
            # if the curr char is unique, keep expanding the window (expand the right pointer)
            # when it hits a curr char that appeared before (violation), 
                # "shrink" the left pointer to the right pointer (update left wit right).
                # repeat the procedure
        
        # char_freq = {}
        # l, r = 0, 1
        # max_length = 0
        # while r < len(s):
        #     if s not in char_freq:
        #         char_freq[s] = 1
        #         curr_length = r - l
        #         r += 1
        #     # if the char showed up before, we reset the curr_length count to start tracking the next contiguous substring.
        #     else:
        #         if curr_length >= max_length:
        #             max_length = curr_length
        #         l = r
        #         r += 1
        #         curr_length = 0
        #         char_freq = {}
        # return max_length


        # # "abcabcbb"


        # init a left pointer at begin, and loop over the right pointer
        # if the rightpointer char is unique, keep expanding
        # otherwise, keep shrinking from the left pointer
        # after shrinking to a valid window, update the curr length and check with the max length we're tracking
        # the whole idea is to maintain a "valid" window size (valid = non duplicate substring)

        unique_char = set()
        l = 0
        max_length = 0
        # iterate over the right pointer
        for r in range(len(s)):
            # violation: if current char is a duplicate, then shrink from left
            while s[r] in unique_char:
                unique_char.remove(s[l])
                l += 1
            # otherwise unique, then expand from right
            unique_char.add(s[r])
            # for each time we expand we keep track of length and compare with the max
            curr_length = r - l + 1
            if curr_length >= max_length:
                max_length = curr_length
        return max_length









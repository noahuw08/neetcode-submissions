class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "XYYX", k = 2 -> "XXXX" -> 4
        # "AAABABB", k = 1 -> "AAAAABB" -> 5
        # think about how long a substring could become if we're alloed to change up to k characters
        # better, think about this problem as:
            # "i'm not looking for the substring that already has the same characters (it makes sense to have thought of it this way), i'm looking for the longest substring that is almost all the same characters ("AAABA" within "AAABABB"), while the wrong characters can be replaced within k replacements."
        
        # valid window = window size - max frequency <= k

        # the key is to keep track of the current longest possible repeat-char substring WITH the non-repeated ones, whose repleacement can be fitted within k.

        # flow:
            # "AAABABB"
            # ..., then at "AAABAB", the current window is invalid (2 B's to replace while we can only replace 1)
            # so we need to move back the count to keep count of the frequency of the current char. and also move the left pointer forward by 1

        
        # "ABAAAB", k = 1

        charset = set(s)
        res = 0
        for c in charset:
            count, l = 0, 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                # window size is essentially the longest substring containing the non-repeating characters whose replacement cnt is within k replacements.
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res
                
        






        

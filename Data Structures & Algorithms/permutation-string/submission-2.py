class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s2 contains a substring that is a permutation of s1 -> true
        # otherwise false

        # substring in s2 is valid when:
            # need to be same length as s1 -> set a fixed size sliding window as len(s1)

        # traverse the s2 in one pass.
            # in each iteration, 

        # for permutation check: need a method to normalize s1 and the potential substring in s2 into the same string, such as sorted string -> hash map

        s1 = ''.join(sorted(s1))
        l = 0
        r = len(s1)
        while r <= len(s2):
            s = ''.join(sorted(s2[l:r]))
            if s == s1:
                return True
            else:
                l += 1
                r += 1
        return False








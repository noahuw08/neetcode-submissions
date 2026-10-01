class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s2 contains a substring that is a permutation of s1 -> true
        # otherwise false

        # substring in s2 is valid when:
            # need to be same length as s1 -> set a fixed size sliding window as len(s1)

        # traverse the s2 in one pass.
            # in each iteration, 

        # for permutation check: need a method to normalize s1 and the potential substring in s2 into the same string, such as sorted string -> hash map

        # s1 = ''.join(sorted(s1))
        # l = 0
        # r = len(s1)
        # while r <= len(s2):
        #     s = ''.join(sorted(s2[l:r]))
        #     if s == s1:
        #         return True
        #     else:
        #         l += 1
        #         r += 1
        # return False

        # but this is non-optimal. At each sliding window of size (len(s1)), we normalize (sort) the substring, resulting in an O(n^2) time complexity.

        # Optimal soln:
            # use a hashmap for both s1 and s2. for s1 since unchanged keep the same map
            # for s2, at each sliding window, update the map with the count
        
        count1 = {}
        count2 = {}

        # keep the count of each character in s1
        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        l = 0

        # count the freq of each character in s2 as well
        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1

            # if the window size > len(s1), reduce the count freq of the char at the left pointer by 1, and then shrink from the left pointer by 1
            while r - l + 1 > len(s1):
                count2[s2[l]] -= 1

                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            
            if count1 == count2:
                return True

        return False






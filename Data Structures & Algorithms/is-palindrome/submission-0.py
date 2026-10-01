class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        # init 1 pointer at the beginning, 1 pointer at the end
        # start traversing for begin pointer and reverse traversal for the other pointer
            # and check if both pointers match. at any point if no match, return False. otherwise, move both pointers inward and repeat
        # if both pointers meet (at the same index), meaning all match, return True
        
        # conditions we need to check for palindrome:
            # whether a character is alphanumeric
            # and also A is the same as a (case insensitive), we should .lower() when a char is an uppercase letter and then perform the check
        

        # ex:
            # "abba" -> palindrome
            # "abb   a" -> palindrome (ignore whitespaces)
            # "abb  @#   a" -> palindrome (ignore whitspaces & special characters)
        
        # init two pointers, 1 at begin, 1 at end
        l, r = 0, len(s) - 1

        # start the two pointers on the palindrome check
        while l < r:
            # if a char is not alphanumeric (ex: whitespace, special chars), then we ignore (moving l pointer forward) until we find an alphanumeric one.
            while l < r and not self.is_alpha_num(s[l]):
                l += 1
            # same thing for the right pointer
            while r > l and not self.is_alpha_num(s[r]):
                r -= 1
            # after converting to lowercase and not match -> return False
            if s[l].lower() != s[r].lower():
                return False
            # after checking all conditions, update the two pointers by moving them inward to each other by one.
            l, r = l + 1, r - 1
        return True

    # helper (a constructor): check if a char is alphanumeric, as the condition logic is quite lengthy and we don't wanna repeatedly write that
    def is_alpha_num(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
        ord('A') <= ord(c) <= ord('Z') or
        ord('0') <= ord(c) <= ord('9'))

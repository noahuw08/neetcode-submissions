class Solution:
    def isValid(self, s: str) -> bool:
        # Stack data structure
        #
        # Based on the conditions, the key observation is that whenever
        # we encounter a closing bracket, we need to check whether it
        # matches the most recent unmatched opening bracket.
        #
        # The "most recent" opening bracket is always the one at the
        # top of the stack.
        #
        # Ex1 is trivial.
        #
        # Ex2: whenever we encounter a closing bracket, we check it
        # against the most recent unmatched opening bracket (the one
        # at the top of the stack).
        #
        # Ex3: when we encounter the ')' bracket, the most recent
        # unmatched opening bracket is '['. Since '[' does not match
        # ')', we return False immediately.
        #
        # The key is the "most recent":
        # always check a closing bracket against the most recent
        # unmatched opening bracket.

        # Steps:
        # 1. Traverse through the string one bracket at a time.
        # 2. If a bracket is an opening bracket, push it onto the stack.
        # 3. If a bracket is a closing bracket:
        #       - If the stack is empty, there is no opening bracket
        #         to match it with, so return False.
        #       - Otherwise, pop the opening bracket at the top of
        #         the stack and check if it matches the closing bracket.
        #       - If it doesn't match, return False immediately.
        # 4. If the whole string is traversed and the stack is empty,
        #    every opening bracket had a matching closing bracket,
        #    so return True.

        stack = []

        for b in s:
            # if it's an opening bracket, push on top of the stack
            if (b == '(') or (b == '[') or (b == '{'):
                stack.append(b)
            # otherwise if it's a closing bracket:
            else:
                # if the stack is empty (meaning there's no opening bracket to match it with), simply return False
                if len(stack) == 0:
                    return False
                top = stack.pop()   # the opening bracket top of stack
                # check whether opening and closing match
                if (b == ')') and (top != '('):
                    return False
                if (b == ']') and (top != '['):
                    return False
                if (b == '}') and (top != '{'):
                    return False
            # if none  of these is true, it means there's a matching pair, then keep traversing.
        
        # The string is valid only if there are no unmatched # opening brackets left in the stack
        return len(stack) == 0
        






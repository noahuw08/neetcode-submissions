class Solution:
    def isValid(self, s: str) -> bool:
        # stack data tsructure
        # based on the iff bullet points, only case we'd know  each bracket pair is valid is if we check an opening bracket with  the most recent unmatched closing bracket
        # ex1 is trivial. ex2, it's always the check of the opening bracket with the most recent unmatched closing bracket (curly, square, normal brackets).
        # ex3, the ( bracket didn't match with the most recent closing bracket, the ] one. return false right away. (violate point 2)
        # the key is the "most recent". always check an opening bracket with the most recent closing  bracket to see if it's a pair.

        # steps:
            # traverse through the list of opening and closing brackets, if a bracket is open, then push onto the stack
            # otherwise, pop the opening bracket that's on top of the stack and check if it pairs with the most recent closing bracket
            # if it doenst match, return false right away
            # if it matches , keep going.
            # the whole thing is true if the stack is empty after the traversal.

        stack = []

        for b in s:
            # if it's an opening bracket, push onto the stack
            if (b == '(') or (b == '[') or (b == '{'):
                stack.append(b)
            # otherwise if it's a closing bracket:
            else:
                # if the stack is empty (meaning the closing bracket's opening one doesnt exist earlier, then whoel thing invalid)
                if len(stack) == 0:
                    return False
                top = stack.pop()   # the opening bracket top of stack
                if (b == ')') and (top != '('):
                    return False
                if (b == ']') and (top != '['):
                    return False
                if (b == '}') and (top != '{'):
                    return False
            # if none  of these is true, it means there's a matching pair, then keep traversing.
        
        return len(stack) == 0
        






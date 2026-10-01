class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flatten mxn 2D matrix:
        #  [1,2,4,8,10,11,12,13,14,20,30,40]

        # but flatten everything into a single array is O(m * n)
        #  we can do a 2-pass binary search to achieve O(log(m * n))

        # core idea: think about binary search in terms of checking the target with each row's max value
            # if the target is greater than  a row max value, then it's greater than all values of all previous rows., because the row is sorted in non-decreasing order
        
        # so we can eliminate half of the search area by doing this
    

    # 1st pass of binary search to determine the row where the target can belong:
        # how do we decide the midpoint?
            # the index of the row midpoint of the whole matrix, then get its max val
            # if target > max val of that row, eliminate everything from left and move left pointer to the next row's max val.
            # otherwise, eliminate everything to the right and move right pointer to the previous row's max val
    
    # 2nd pass of binary search to determine if the target exists in that row:
        # perform a vanilla binary search in a sorted array. 

    
        l, r = 0, len(matrix) - 1
        l_, r_ = 0, len(matrix[0]) - 1
        # 1st pass of the binary search
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            # else, meaning only possilbe case is that the target must belong in this row, or the target is not there at all.
            else:
                break

        # 2nd pass of the binary search
        while l_ <= r_:
            m_ = (l_ + r_) // 2
            if target > matrix[m][m_]:
                l_ = m_ + 1
            elif target < matrix[m][m_]:
                r_ = m_ - 1
            else:
                return True
        return False
        





        
            

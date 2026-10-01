class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # problem understanding: contain the most water when:
        # both width and height need to be at maximum (imagine the area of rectangle).
            # width: distance in terms of indices -> maximize
            # height: the value. -> maximize
            # contraints: 
        # [1,7,2,5,4,7,3,6]
            # for the height calculation, always do the min(val1, val2) to make sure the height is valid
        
        # # two pointers will work here:
        #     # start at the same end (beginning) 
        #     # fix one pointer (left pointer) at i for each iteration i over the for loop
        #     # right pointer traverses to explore and compute the area.
        #         # if the  new area > old area, update the area.
        #         # return after both pointers  are at the end of the array.
        # area = 0
        # for i in range(len(heights)):
        #     l, r = i, i + 1
        #     if l == len(heights) - 1:
        #         break
        #     while r <= len(heights) - 1:
        #         curr_area = min(heights[l], heights[r]) * (r - l)
        #         if curr_area >= area:
        #             area = curr_area
        #             r += 1
        #         else:
        #             r += 1
        # return area


        # intuition: we can do this in O(n)
        # start with the widest container (left at start, right at end)
        # **since the height is always limited by the shorter line (bcuz we need to maintain a valid area), moving the taller line never helps with finding the maxinmum area but reduces the width.
            # SO, move the left or right pointer dynamically depending on which pointer's value is smaller (shorter line), then move that pointer inward.

        area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            curr_area = height * width
            if curr_area >= area:
                area = curr_area
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return area
            




         



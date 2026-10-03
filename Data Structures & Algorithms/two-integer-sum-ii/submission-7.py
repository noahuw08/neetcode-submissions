class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force two pointers
        # O(1) additional space, so can't init an array to store the indexes.
        # not using the same element twice
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return []

        # [1,2,3,3,3,3,4,5], target = 6

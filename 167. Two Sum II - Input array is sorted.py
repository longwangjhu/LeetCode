# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Given an array of integers numbers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer
# of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

# You may assume that each input would have exactly one solution and you may
# not use the same element twice.

###############################################################################

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]
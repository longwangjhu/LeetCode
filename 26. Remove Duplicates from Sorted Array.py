# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. The
# relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you
# must instead have the result be placed in the first part of the array nums. More
# formally, if there are k elements after removing the duplicates, then the first
# k elements of nums should hold the final result. It does not matter what you
# leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the
# input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# If all assertions pass, then your solution will be accepted.

################################################################################

# in-place remove, sorted -> slow and fast ptrs

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1 # only increase when different
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1

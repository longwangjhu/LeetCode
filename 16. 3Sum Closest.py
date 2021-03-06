# https://leetcode.com/problems/3sum-closest/

# Given an array nums of n integers and an integer target, find three integers in
# nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.

################################################################################

# recall 3Sum -> sort -> fix a -> 2Sum
# since sorted, use pointers for b and c and move towards the middle

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3: return None
        
        n = len(nums)
        nums.sort()
        best = float('inf')
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]: # skip identical a
                continue
            
            # use pointers for b and c, and move towards the middle
            l = i + 1
            r = n - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # update the best
                if abs(total - target) < abs(best - target):
                    best = total
                
                # move the pointers
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
        
        return best

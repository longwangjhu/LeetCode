# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
# the x-axis forms a container, such that the container contains the most
# water.

# Notice that you may not slant the container.

###############################################################################

# two pointers starting from both ends -> move towards the middle
# move the shorter one (hope to improve)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 1: return 0

        # two pointers move towards the middle
        l, r = 0, len(height) - 1
        ans = 0
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            
            # move the shorter one
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
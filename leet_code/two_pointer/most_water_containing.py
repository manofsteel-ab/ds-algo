"""
Given n non-negative integers a1, a2, ..., an , where each represents a point
 at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
 of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
 forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j = len(height)-1
        ans = 0
        while i<j:
            h = min(height[i], height[j])
            ans = max(ans, h*(j-i))
            while i<j and height[i]<=h:
                i+=1
            while i<j and height[j]<=h:
                j-=1
        return ans

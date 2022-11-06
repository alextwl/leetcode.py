'''
onepass 2 point approach
learnt from official solution & detailed proof:
https://leetcode.com/problems/container-with-most-water/discuss/6099/yet-another-way-to-see-what-happens-in-the-on-algorithm
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            maxarea = max(maxarea,
                          min(height[left], height[right]) * width
                         )
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return maxarea

    
'''
brute force recursion
time=O(n**2)
'''
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        maxwater = 0
        
        for left in range(0, len(height)-1):
            if height[left] == 0: continue
            for right in range(left+1, len(height)):
                if height[right] == 0: continue
                width = right - left
                minheight = min(height[left], height[right])
                water = width * minheight
                maxwater = max(maxwater, water)
        
        return maxwater

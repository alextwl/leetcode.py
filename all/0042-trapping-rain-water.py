'''
2022/09/18 daily challenge
'''

'''
dynamic programming ver
memorize each position's max left & right heights in advance.
time=O(n), space=O(2n)
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        width = len(height)
        dp_left = [0] * width
        dp_right = [0] * width
        
        # find max height of bar from the left
        dp_left[0] = height[0]
        for i in range(1, width):
            dp_left[i] = max(height[i], dp_left[i-1])
        
        # find max height of bar from the right
        dp_right[-1] = height[-1]
        for i in range(width-1-1, -1, -1):
            dp_right[i] = max(height[i], dp_right[i+1])
        
        # add trapped water
        for i in range(1, width):
            water += min(dp_left[i], dp_right[i]) - height[i]
        
        return water

'''
brute force
time=O(n**2)
'''

class Solution2:
    def trap(self, height: List[int]) -> int:
        water = 0
        
        for idx in range(len(height)):
            left_max = right_max = 0
            
            for left_idx in range(idx, -1, -1):
                left_max = max(left_max, height[left_idx])
            for right_idx in range(idx, len(height)):
                right_max = max(right_max, height[right_idx])
            
            water += min(left_max, right_max) - height[idx]
        
        return water

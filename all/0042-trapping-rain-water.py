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


'''
2024/04/12 daily challenge

monotonic stack approach
'''


class Solution3:
    def trap(self, height: List[int]) -> int:
        water = 0
        stack = []  # previous higher terrarin (position, height)
        
        for right, right_height in enumerate(height):
            last_floor = None  # memorize last floor of height of low-lying area
            while stack:
                left, left_height = stack[-1]
                ceiling = min(left_height, right_height)

                if last_floor is not None:
                    # there're lower low-lying area in the right side,
                    # time to trap the water.
                    # note both the point of right and left do not trap water,
                    # so the water range is (right - left - 1).
                    water += (right - left - 1) * (ceiling - last_floor)
                
                last_floor = ceiling

                if left_height <= right_height:
                    stack.pop()
                else:
                    break

            stack.append((right, right_height))

        return water


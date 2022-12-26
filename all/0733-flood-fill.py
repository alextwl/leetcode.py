'''
leetcode 75 lv1 day 9

breadth first search approach
'''

import collections

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height, width = len(image), len(image[0])

        orig_color = image[sr][sc]
        if orig_color == color:
            # the color of the starting pixel is same to the target color, no need to replace.
            return image

        q = collections.deque([(sr, sc)])

        while(q):
            h, w = q.popleft()
            if image[h][w] == orig_color:
                image[h][w] = color

                # queue neighbor pixels connected 4-directionally
                for i, j in [(h+1, w), (h-1, w), (h, w-1), (h, w+1)]:
                    if 0 <= i < height and 0 <= j < width:
                        q.append((i, j))
        
        return image


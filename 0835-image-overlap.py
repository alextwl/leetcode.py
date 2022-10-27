'''
2022/10/27 daily challenge

linear transformation approach

learnt from official solution 2

suppose 1's of img2 is linear-transformed from img1,
a vector is applied to img1 in order to become img2.

by evaluating all possible vectors,
find the maximum number of overlapped coordinate from all vectors.

time=O(n**4)
'''

import collections


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        width = len(img1)
        
        '''
        filter all 1's coordinates from img1 & img2.
        '''
        img1_one = [(x, y) for x in range(width) for y in range(width) if img1[x][y] == 1]
        img2_one = [(x, y) for x in range(width) for y in range(width) if img2[x][y] == 1]
        
        '''
        count overlapped coordinates for each vector.
        '''
        vector_overlapped = collections.defaultdict(int)
        
        '''
        suppose any 1's coordinate of img2 is transformed from any 1's coordinate of img1,
        find the maximum number of the same vector found from the difference between 2 coords from img1 & img2,
        the number is also the maximum number of overlapped coordinates.
        '''
        for x1, y1 in img1_one:
            for x2, y2 in img2_one:
                vector = (x2 - x1, y2 - y1)
                vector_overlapped[vector] += 1
        
        return max(vector_overlapped.values()) if vector_overlapped else 0

'''
2022/09/30 daily challenge

learnt from
https://leetcode.com/problems/the-skyline-problem/discuss/61261/11-line-Python-solution-with-max-heap-easy-to-understand

Max heap approach (by python's min heap with negative values)
'''

import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        First sort all the coordinate changes of x with two parts (left + right coords).
        
        x_height_right[i] = (left_i or right_i, negative_height_i or 0, right_i or 0)
        '''
        x_height_right = [(L, -H, R) for L, R, H in buildings]  # left part of building
        x_height_right += [(R, 0, 0) for _, R, _ in buildings]  # right part of building with height changed to zero.
        x_height_right.sort()  # sort by x
        
        '''
        the outer contour of the silhouette
        the default coord [0,0] is for comparsion of max heights, not a part of answer.
        '''
        contour = [[0,0]]
        
        '''
        max_heap[i] = (-height, R)
        implemented by python's min heap which it pops the minimum element (min(-height) == max(height))
        '''
        max_heap = [(0, float('inf'))]
        
        current_max_height = 0
        
        for x, negative_height, R in x_height_right:
            while x >= max_heap[0][1]:  # x >= R with max height
                '''
                remove last building with max height
                because the building is proceeded (ended) and do not overlap current building.
                '''
                heapq.heappop(max_heap)
                
            if negative_height:
                '''
                it matches heights with full data (L, -H, R)
                and pushes only height & right x to the heap.
                '''
                heapq.heappush(max_heap, (negative_height, R))
            
            # update current max height by retrieving min(-height)
            current_max_height = -max_heap[0][0]
            
            if contour[-1][1] != current_max_height:
                # the outer contour of height changed from the last coord to x.
                contour.append([x, current_max_height])
        
        return contour[1:]

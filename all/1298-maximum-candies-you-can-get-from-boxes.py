'''
2025/06/03 daily challenge

breadth first search approach
'''


import collections


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        earns = 0
        boxes = set(initialBoxes)

        q = collections.deque([i for i in initialBoxes if status[i]])
        while q:
            box = q.popleft()
            if box not in boxes:
                continue
            boxes.remove(box)
            earns += candies[box]
            boxes.update(containedBoxes[box])
            for k in keys[box]:
                status[k] = 1
            q.extend([i for i in boxes if status[i]])
        return earns


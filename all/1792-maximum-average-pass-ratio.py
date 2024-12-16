'''
2024/12/15 daily challenge

max heap approach

prioritize the gain of ratio when an extra student to be added to a class,
to maximize the average pass ratio.
'''


import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return ((p + 1.0)/(t + 1.0)) - p/t
        h = []
        full = 0
        for p, t in classes:
            if p < t:
                heapq.heappush(h,(-gain(p, t), t, p))
            else:
                # no need to add more student to a class with full passed students
                full += 1
        if not h:
            # no need to go further if all students/classes passed already.
            return 1.0
        for _ in range(extraStudents):
            _, t, p = h[0]
            t += 1
            p += 1
            heapq.heapreplace(h,(-gain(p,t), t, p))
        return (sum(p/t for _, t, p in h) + full) / len(classes)


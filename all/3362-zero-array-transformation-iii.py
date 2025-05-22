'''
2025/05/22 daily challenge

max heap + greedy method approach
'''


import heapq


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        qn = len(queries)
        queries.sort()  # sort by left bound of queries
        j = 0  # next index of query to be queued
        h = []  # max heap of right bounds

        offsets = [0] * (len(nums) + 1)  # diff array
        ops = 0
        for i, v in enumerate(nums):
            ops += offsets[i]

            while j < qn and queries[j][0] == i:
                heapq.heappush(h, -queries[j][1])
                j += 1
            # check if current ops was sufficient or not
            while ops < v and h and -h[0] >= i:
                # apply one more query from the heap
                ops += 1
                # decrement the delta next to the right bound by 1
                offsets[-heapq.heappop(h) + 1] -= 1
            if ops < v:
                return -1
        # the question asks for the maximum number of queries can be removed, not minimum operations.
        return len(h)


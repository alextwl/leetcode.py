'''
2026/01/23 daily challenge

doubly linked list + min heap approach

learnt from official editorial:
https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/editorial/#approach-priority-queue--lazy-deletion

maintain the minimum pair sum structure (the min heap),
relationships of adjacent nodes (the linked list),
and the status (merged or not) of nodes simultaneously.

same to problem 3507 with large input.
'''


import heapq


class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx  # original index in nums
        self.prev = None
        self.next = None


class Pair:
    def __init__(self, node0, node1, pair_sum):
        self.node0 = node0
        self.node1 = node1
        self.pair_sum = pair_sum
    
    def __lt__(self, opnd):
        # for heap
        if self.pair_sum == opnd.pair_sum:
            # same pair sum, choose the leftmost one.
            return self.node0.idx < opnd.node0.idx
        return self.pair_sum < opnd.pair_sum


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        merged = set()  # indices of deleted Nodes
        ans = 0  # the count of merger
        dec_count = 0  # the count of pairs of decreasing
        h = []  # min heap of Pair instances
        it = enumerate(nums)
        n1 = head = Node(next(it)[1], 0)

        # build doubly-linked list
        for i, v in it:
            n2 = Node(v, i)
            n1.next = n2
            n2.prev = n1

            heapq.heappush(h, Pair(n1, n2, n1.val + v))

            if n1.val > v:
                dec_count += 1

            n1 = n2

        # merger
        while dec_count > 0:
            p = heapq.heappop(h)
            n1, n2, pair_sum = p.node0, p.node1, p.pair_sum

            if n1.idx in merged or n2.idx in merged or \
                    n1.val + n2.val != pair_sum:
                # skip merged nodes
                continue

            # anyway we are going to merge a pair
            ans += 1

            if n1.val > n2.val:
                # it's a decreasing pair
                dec_count -= 1

            # merge n1 & n2
            # n0, n1, n2, n3 -> n0, n1_updated, n3
            n0 = n1.prev
            n3 = n2.next

            n1.next = n3
            if n3:
                n3.prev = n1

            # create new pairs for (n0, n1) & (n1, n3)
            if n0:
                if n0.val > n1.val and n0.val <= pair_sum:
                    # also eliminate a decreasing pair of (n0, n1)
                    dec_count -= 1
                elif n0.val <= n1.val and n0.val > pair_sum:
                    # it was non-decreasing for (n0, n1)
                    # but changed to a decreasing pair of (n0, n1_updated)
                    dec_count += 1
                heapq.heappush(h, Pair(n0, n1, n0.val + pair_sum))

            if n3:
                if n2.val > n3.val and pair_sum <= n3.val:
                    # also eliminate a decreasing pair of (n2, n3)
                    dec_count -= 1
                elif n2.val <= n3.val and pair_sum > n3.val:
                    # it was non-decreasing for (n2, n3)
                    # but changed to a decreasing pair of (n1_updated, n3)
                    dec_count += 1
                heapq.heappush(h, Pair(n1, n3, pair_sum + n3.val))

            n1.val = pair_sum   # n2 combined into n1
            merged.add(n2.idx)  # n2 is discarded

        return ans


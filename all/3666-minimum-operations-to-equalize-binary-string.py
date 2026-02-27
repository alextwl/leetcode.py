'''
2026/02/27 daily challenge

breadth first search + binary search approach

learnt from official editorial:
https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/editorial/#approach-breadth-first-search
'''


import bisect
import collections


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        m, n = s.count('0'), len(s)
        # min_ops[i] = minimum operations to reach i zeros.
        min_ops = [float('inf')] * (n + 1)
        node_sets = [sorted(range(0, n + 1, 2)), sorted(range(1, n + 1, 2))]
        q = collections.deque([m])
        min_ops[m] = 0  # base case
        node_sets[m & 1].remove(m)

        while q:
            # current count of zeros
            m = q.popleft()
            # the new number of zeros is m + k - 2c, c is within [c1, c2].
            c1, c2 = max(k - n + m, 0), min(m, k)  # max ones, max zeros
            left, right = m + k - 2 * c2, m + k - 2 * c1
            curr_set = node_sets[left & 1]
            i = bisect.bisect_left(curr_set, left)
            while i < len(curr_set) and curr_set[i] <= right:
                new_m = curr_set[i]
                min_ops[new_m] = min_ops[m] + 1
                q.append(new_m)
                curr_set.pop(i)

        # when all chars in the string equal to '1', no zeros exist.
        if min_ops[0] == float('inf'):
            return -1
        return min_ops[0]


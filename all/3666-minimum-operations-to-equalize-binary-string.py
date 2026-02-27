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


'''
math approach
'''


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        m, n = s.count('0'), len(s)

        # corner case
        if n == k:
            if m == 0:
                # no need to flip
                return 0
            if m == n:
                # flip all digits in a batch only
                return 1
            else:
                # impossible to make all bits equal to one.
                return -1

        min_ops = float('inf')

        # even count of zeros,
        # calculate min even operations.
        if m & 1 == 0:
            # max(math.ciel(m / k), math.ciel(m / (n - k)))
            # (n - k) = the max non-overlapped region size
            ops = max((m + k - 1) // k, (m + (n - k) - 1) // (n - k))
            # adjust if ops was not even.
            if ops & 1:
                ops += 1
            min_ops = min(min_ops, ops)

        # when counts of zeros & k have the same parity,
        # calculate min odd operations.
        if m & 1 == k & 1:
            # max(math.ciel(m / k), math.ciel((n - m) / (n - k)))
            ops = max((m + k - 1) // k, (n - m + (n - k) - 1) // (n - k))
            # adjust if ops was not odd.
            if ops & 1 == 0:
                ops += 1
            min_ops = min(min_ops, ops)

        if min_ops == float('inf'):
            return -1
        return min_ops


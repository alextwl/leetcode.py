'''
topological sort approach

test all divisors as the value of a component.

similar to problem 2872.
'''


import collections


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = {i: set() for i in range(n)}
        indegree = [0] * n
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
            indegree[a] += 1
            indegree[b] += 1

        def search(k):
            values = nums.copy()
            deg = indegree.copy()
            q = collections.deque(i for i, v in enumerate(deg) if v == 1)

            while q:
                curr = q.popleft()
                deg[curr] = 0
                adds = values[curr] if values[curr] != k else 0
                for adj in g[curr]:
                    if adds:
                        values[adj] += adds

                    deg[adj] -= 1
                    if deg[adj] == 0:
                        # terminal reached, test the value
                        return values[adj] == k

                    if deg[adj] == 1:
                        q.append(adj)

        # test all divisors of sum(nums) as sum of components.
        # no need to test divisors smaller than minimum node value.
        total_sum = sum(nums)
        for tree_val in range(min(nums), total_sum):
            if total_sum % tree_val == 0 and search(tree_val):
                print("test %d %d" % (total_sum, tree_val))
                return total_sum // tree_val - 1
        # the whole tree can be single component only. no cut can be made.
        return 0


'''
2024/02/25 daily challenge

Union-find approach

learnt from official solution

treat it as a graph problem, connect each node
with all its prime factors as dummy nodes,
and then validate if all nodes were in the same graph.
'''


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        max_val = max(nums)
        # sieve[i] == the greatest prime factor of i
        sieve = [0] * (max_val + 1)

        if n == 1:
            # edge case: a graph with single node
            return True

        if 1 in nums:
            # edge case: gcd(1, any val) == 1
            return False

        # generate prime factors
        for i in range(2, max_val + 1):
            if sieve[i] == 0:
                for j in range(i, max_val + 1, i):
                    sieve[j] = i

        # Union-find structure
        parent = [i for i in range(max_val + 1)]
        rank = [0] * (max_val + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)

            if rank[x] >= rank[y]:
                rank[x] += 1
                parent[y] = x
            else:
                rank[y] += 1
                parent[x] = y

        for v in nums:
            next_factor = v

            # connect v with its prime factors
            while(next_factor > 1):
                # get the greatest prime factor of next_factor
                prime = sieve[next_factor]

                # build an edge between prime and next_factor
                if find(prime) != find(v):
                    union(prime, v)

                # remove the current prime factor and search next factor
                while (next_factor % prime == 0):
                    next_factor //= prime

        # check if v and nums[0] were in the same graph
        for v in nums:
            if find(v) != find(nums[0]):
                return False

        # all pairs of nodes were reacheable
        return True


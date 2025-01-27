'''
2025/01/26 daily challenge

topological sort approach

learnt from official editorial 2:
https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/editorial/#approach-2-topological-sort-to-reduce-non-cyclic-nodes

the answer will be either:
(1) a cycle which is size > 2 and big enough.
    we cannot attach any acyclic path to the cycle because
    it breaks the dependency of favorite chain in the cycle.
(2) one or more 2-cycles with extended pathes from its endpoints.
'''


import collections


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegrees = [0] * n

        for fav in favorite:
            indegrees[fav] += 1
        
        # topological sort
        q = collections.deque([i for i, v in enumerate(indegrees) if v == 0])

        # each node's depth = the length of the longest path extended to the node.
        depth = [1] * n
        # scan acyclic parts
        while q:
            node = q.popleft()
            next_hop = favorite[node]
            depth[next_hop] = max(depth[next_hop], depth[node] + 1)
            indegrees[next_hop] -= 1
            if indegrees[next_hop] == 0:
                q.append(next_hop)
        
        # the length of the longest size>2 cycle.
        longest = 0
        # the sum of lengthes of 2-cycle + extended pathes
        two_cycles = 0
        # scan all nodes within cycles
        for i in range(n):
            if indegrees[i] == 0:
                # proceeded acyclic part or visited node in a cycle
                continue
            
            # estimate the length of a cycle
            cycle_length = 0
            j = i
            while indegrees[j]:
                indegrees[j] = 0  # visited
                cycle_length += 1
                j = favorite[j]
            
            if cycle_length == 2:
                # it's a 2-cycle: i <-> j
                # a path = (extended path + node i) + (node j + extended path)
                # we can have multiple groups of 2-cycle joined.
                two_cycles += depth[i] + depth[favorite[i]]
            else:
                # it's a size>2 cycle, maximize the longest.
                longest = max(longest, cycle_length)
        return max(longest, two_cycles)


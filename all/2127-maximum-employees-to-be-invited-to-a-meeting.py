'''
2025/01/26 daily challenge

topological sort approach (functional graph problem)

learnt from official editorial 2:
https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/editorial/#approach-2-topological-sort-to-reduce-non-cyclic-nodes
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

        depth = [1] * n  # each node's depth
        while q:
            node = q.popleft()
            next_hop = favorite[node]
            depth[next_hop] = max(depth[next_hop], depth[node] + 1)
            indegrees[next_hop] -= 1
            if indegrees[next_hop] == 0:
                q.append(next_hop)
        
        longest = 0
        two_cycles = 0
        for i in range(n):
            if indegrees[i] == 0:
                continue
            
            cycle_length = 0
            j = i
            while indegrees[j]:
                indegrees[j] = 0  # visited
                cycle_length += 1
                j = favorite[j]
            
            if cycle_length == 2:
                two_cycles += depth[i] + depth[favorite[i]]
            else:
                longest = max(longest, cycle_length)
        return max(longest, two_cycles)


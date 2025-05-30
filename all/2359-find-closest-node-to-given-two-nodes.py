'''
2023/01/25 daily challenge
2025/05/30 daily challenge

breadth first search approach

calculate the distance between node1/node2 to all nodes first,
and then find the minimum of max(distToNode1[i], distToNode2[i]).
'''


import collections


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def bfs(src):
            ret = [float('inf')] * n
            q = collections.deque([src])
            distance = 0
            while q:
                width = len(q)
                for _ in range(width):
                    node = q.popleft()
                    if ret[node] <= distance:
                        continue
                    ret[node] = distance
                    if edges[node] > -1:
                        q.append(edges[node])
                distance += 1
            return ret

        dist1 = bfs(node1)
        dist2 = bfs(node2)
        min_dist = float('inf')
        ans = -1

        for i, (a, b) in enumerate(zip(dist1, dist2)):
            max_ab = max(a, b)
            if max_ab < min_dist:
                min_dist = max_ab
                ans = i

        return ans


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


'''
single loop ver

since each node has at most 1 outgoing edge,
we can run BFS from both node1 & node2 by single loop simultaneously
without the need to estimate the distance.
'''


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        a, b = node1, node2
        seen1, seen2 = set(), set()

        # traverse from both node1 & node2 simultaneously.
        while a != -1 or b != -1:
            # cycle detection
            if a in seen1:
                a = -1
            if b in seen2:
                b = -1

            # visit nodes
            if a != -1:
                seen1.add(a)
            if b != -1:
                seen2.add(b)

            # check if both nodes already reached from another sources
            if a in seen2 and b in seen1:
                return min(a, b)  # node with smaller index prevails
            if a in seen2:
                return a
            if b in seen1:
                return b

            # go to next nodes
            if a != -1:
                a = edges[a]
            if b != -1:
                b = edges[b]
        # not found
        return -1


'''
2023/01/25 daily challenge

breadth first search approach

calculate the distance between node1/node2 to all nodes first,
and then find the minimum of max(distToNode1[i], distToNode2[i]).
'''

import collections


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start: int):
            '''
            due to the limitation that each node has at most one outgoing edge,
            the queue will always have at most one node,
            node traversal orders by BFS and DFS will be the same.
            '''
            dist_dict = dict()
            q = collections.deque([start])
            distance = 0
            while(q):
                node = q.popleft()
                if node in dist_dict:
                    # node visited, bypass the cycle.
                    continue

                next_node = edges[node]
                if next_node != -1:
                    q.append(next_node)
                dist_dict[node] = distance
                distance += 1

            return dist_dict

        distToNode1 = bfs(node1)
        distToNode2 = bfs(node2)

        candidates = set(distToNode1.keys()) & set(distToNode2.keys())
        if not candidates:
            return -1
        closetNode = 100001
        minDist = float('inf')

        for node in candidates:
            if (dist := max(distToNode1[node], distToNode2[node])) <= minDist:
                if not(dist == minDist and node > closetNode):
                    # smaller index of the same distance has the higher priority
                    minDist = dist
                    closetNode = node

        return closetNode if closetNode != 100001 else -1


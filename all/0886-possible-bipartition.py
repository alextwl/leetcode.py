'''
2022/12/21 daily challenge

breadth first search approach

traverse all dislike pairs, bipartition each pair with different group,
and find the conflict.
'''

import collections


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # build bidirectional graph by connecting all dislike pairs
        vertices = [[] for _ in range(0, n+1)]
        for v1, v2 in dislikes:
            vertices[v1].append(v2)
            vertices[v2].append(v1)
        
        '''
        set group for each vertex
        None: unset, False: Group 1, True: Group 2
        '''
        vgroup = [None for _ in range(0, n+1)]

        # run BFS from each unset vertex
        for root in range(0, n+1):
            if vgroup[root] is None:
                queue = collections.deque([root])
                vgroup[root] = False  # initialize with group 1
                while(queue):
                    v1 = queue.popleft()
                    v1_group = vgroup[v1]
                    for v2 in vertices[v1]:
                        if vgroup[v2] == v1_group:
                            # conflict found, bipartition is impossible.
                            return False
                        if vgroup[v2] is None:
                            # initialize with opposite group and queue it.
                            vgroup[v2] = not(v1_group)
                            queue.append(v2)

        # conflict not found.
        return True


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
        for root in range(1, n+1):
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


'''
union find approach

use union find to bipartition each pair with different group,
and find the conflict.
'''


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(0, n))  # set all vertices' group (parent) to itself.
    
    def find(self, x):
        '''
        find the ultimate parent of x, and update x's parent with it.
        '''
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def merge(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            # x & y are already in the same group (parent)
            return
        
        # use the parent's index as the priority to merge.
        if px > py:
            self.parent[px] = py
        else:
            self.parent[py] = px


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # build bidirectional graph by connecting all dislike pairs
        vertices = [[] for _ in range(0, n+1)]
        for v1, v2 in dislikes:
            vertices[v1].append(v2)
            vertices[v2].append(v1)
        
        # run union find and merge all opposite childern
        uf = UnionFind(n+1)
        for root, childern in enumerate(vertices):
            for child in childern:
                if uf.find(root) == uf.find(child):
                    # conflict found, root & child cannot be in the same group
                    return False
                # merge all childern to the first child's group
                uf.merge(childern[0], child)

        # conflict not found.
        return True

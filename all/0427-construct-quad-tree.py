'''
2023/02/27 daily challenge

bottom-up approach
'''

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], True, None, None, None, None)
        
        def isLeafNode(*children):
            for child in children:
                if isinstance(child, Node):
                    return False
            return all(child == children[0] for child in children)

        n2 = n >> 1
        newGrid = [[None for _ in range(n2)] for _ in range(n2)]
        while(n2):
            for x in range(n2):
                x2 = x << 1
                for y in range(n2):
                    y2 = y << 1
                    leaves = [grid[x2][y2],
                              grid[x2][y2+1],
                              grid[x2+1][y2],
                              grid[x2+1][y2+1]]
                    if isLeafNode(*leaves):
                        # print("[%d][%d] in %d**2 is leaf" % (x, y, n2))
                        newGrid[x][y] = leaves[0]
                    else:
                        # print("[%d][%d] in %d**2 is NOT leaf" % (x, y, n2))
                        for i in range(4):
                            if not isinstance(leaves[i], Node):
                                leaves[i] = Node(bool(leaves[i]), True, None, None, None, None)
                        newGrid[x][y] = Node(True, False, *leaves)
            n, n2 = n2, n2 >> 1
            if n2:
                grid = newGrid
                newGrid = [[None for _ in range(n2)] for _ in range(n2)]
        
        if not isinstance(newGrid[0][0], Node):
            return Node(bool(newGrid[0][0]), True, None, None, None, None)
        
        return newGrid[0][0]


'''
top-down recursive approach
'''


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], True, None, None, None, None)
        
        def buildQuad(x1, y1, x2, y2):
            '''
            :param x1: x-axis coordinate of top-left corner
            :param y1: y-axis coordinate of top-left corner
            :param x2: x-axis coordinate of bottom-right corner
            :param y2: y-axis coordinate of bottom-right corner
            '''
            if x1 == x2 and y1 == y2:
                # single cell of grid selected
                return grid[x1][y1]
            
            hx = (x1+x2) >> 1
            hy = (y1+y2) >> 1
            '''
            # in the sequence: topLeft, topRight, bottomLeft, bottomRight

            +--------------+--------------+
            |(x1,y1)       |(x1,hy+1)     |
            |   topLeft    |   topRight   |
            |       (hx,hy)|       (hx,y2)|
            +--------------+--------------+
            |(hx+1,y1)     |(hx+1,hy+1)   |
            |  bottomLeft  |  bottomRight |
            |       (x2,hy)|       (x2,y2)|
            +--------------+--------------+
            '''
            leaves = [buildQuad(x1, y1, hx, hy),
                      buildQuad(x1, hy+1, hx, y2),
                      buildQuad(hx+1, y1, x2, hy),
                      buildQuad(hx+1, hy+1, x2, y2)]
            
            if all(leaf == leaves[0] for leaf in leaves):
                # all leaves are the same integer.
                return leaves[0]
            
            # some or no leaves are integer, convert all leaves to Node.
            for i in range(4):
                if isinstance(leaves[i], int):
                    leaves[i] = Node(bool(leaves[i]), True, None, None, None, None)
            
            return Node(True, False, *leaves)
        
        # start from the entire grid.
        root = buildQuad(0, 0, n-1, n-1)

        # corner case: if all cell values of the entire grid are the same,
        #              buildQuad() shall return integer, we need to deal with it.
        if isinstance(root, int):
            return Node(bool(root), True, None, None, None, None)

        return root


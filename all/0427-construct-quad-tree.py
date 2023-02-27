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


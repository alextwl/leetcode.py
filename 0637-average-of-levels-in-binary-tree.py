'''
2022/09/02 daily challenge

BFS ver
'''
import queue

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = queue.Queue()
        avgs = list()
        
        q.put(root)
        
        while(not q.empty()):
            levelsum = 0
            nodecount = q.qsize()
            
            for _ in range(0, nodecount):
                node = q.get()
                levelsum += node.val
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            
            avgs.append(levelsum / float(nodecount))
        
        return avgs

'''
DFS ver
'''
class Solution2:
    def dfs(self, node: Optional[TreeNode], levels, depth):
        if node is None:
            return

        if len(levels) <= depth:
            levels.append([0, 0])  # [sum of level, count of nodes in the level]
        
        levels[depth][0] += node.val
        levels[depth][1] += 1
        
        self.dfs(node.left, levels, depth+1)
        self.dfs(node.right, levels, depth+1)
        
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = list()
        
        self.dfs(root, levels, 0)
        
        return [levelsum / float(nodecount) for levelsum, nodecount in levels]

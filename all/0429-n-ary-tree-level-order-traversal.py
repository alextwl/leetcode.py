class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        ans = list()
        q = [root]
        
        while q:
            level_vals = []
            next_q = []  # list of next level (actually a queue, iterated as a FIFO)
            
            # BFS approach
            for node in q:
                level_vals.append(node.val)
                next_q.extend([child for child in node.children])
            
            q = next_q
            ans.append(level_vals)
        
        return ans

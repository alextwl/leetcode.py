'''
2024/07/16 daily challenge

breadth first search approach
'''


import collections


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # convert the tree to edge-based data
        edges = collections.defaultdict(dict)  # edges[src_val][dest_val] = direction
        
        start_node = None
        dest_node = None
        
        # BFS
        q = collections.deque([root])
        while q:
            node = q.popleft()
            
            if node.val == startValue:
                start_node = node
            elif node.val == destValue:
                dest_node = node
            
            if start_node and dest_node:
                # both terminal nodes found, no need to search further
                break
            
            if node.left:
                edges[node.val][node.left.val] = 'L'
                edges[node.left.val][node.val] = 'U'
                q.append(node.left)
            if node.right:
                edges[node.val][node.right.val] = 'R'
                edges[node.right.val][node.val] = 'U'
                q.append(node.right)

        # find the shortest path
        seen = set()
        
        # BFS again
        q = collections.deque([(startValue, "")])
        while(q):
            node_val, path = q.popleft()

            seen.add(node_val)
            
            if node_val == destValue:
                return path
            
            for child, direction in edges[node_val].items():
                if child not in seen:
                    q.append((child, path + direction))

        return None  # undefined


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


'''
lowest common ancestor + depth first search approach

learnt from official solution 3:
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/solution/
'''


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(node, target_val, path: List[str]):
            '''
            this subroutine returns the boolean value for finding the target value,
            and modifies the input path array.
            '''
            if node is None:
                return False
            if node.val == target_val:
                return True
            
            # recursive DFS
            # find target_val in left subtree
            path.append("L")
            if find_path(node.left, target_val, path):
                return True
            path.pop()
            
            # find target_val in right subtree
            path.append("R")
            if find_path(node.right, target_val, path):
                return True
            path.pop()
            
            return False
        
        start_path = []
        dest_path = []

        # find path from root to start/dest nodes
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)

        # find the length of common path
        common_length = 0
        for d1, d2 in zip(start_path, dest_path):
            if d1 == d2:
                common_length += 1
            else:
                break

        directions = ['U'] * (len(start_path) - common_length)
        directions.extend(dest_path[common_length:])

        return ''.join(directions)


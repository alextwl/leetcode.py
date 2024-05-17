'''
2024/05/17 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        sources = {}  # sources[node] = (parent, 0: left, 1: right)

        toBeRemoved = [] # node with val==target

        # create a dummy head in case root is also removed.
        dummyroot = TreeNode(left=root)

        # BFS
        q = collections.deque([(root, dummyroot, 0)])  # (node, parent, parent's left or right child)

        # search target no matter whether it's a leaf or not.
        while q:
            node, parent, lr = q.popleft()

            if node.val == target:
                sources[node] = (parent, lr)
                if node.left is None and node.right is None:
                    toBeRemoved.append(node)

            if node.left: q.append((node.left, node, 0))
            if node.right: q.append((node.right, node, 1))

        # time to remove targets
        while toBeRemoved:
            node = toBeRemoved.pop()
            parent, lr = sources[node]
            # remove the link from parent and **also** check if parent becomes a leaf.
            if lr:
                parent.right = None
                if parent.val == target and parent.left is None:
                    toBeRemoved.append(parent)
            else:
                parent.left = None
                if parent.val == target and parent.right is None:
                    toBeRemoved.append(parent)

        return dummyroot.left


'''
recursion ver
'''


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # shortcut: None == None means no child
        if root.val == target and root.left == root.right:
            return None
        
        return root


'''
leetcode 75 lv2 day 9

inorder traversal approach
'''

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # traverse to leftmost node first.
        while(root):
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        val = node.val

        node = node.right
        while(node):
            self.stack.append(node)
            node = node.left
        
        return val

    def hasNext(self) -> bool:
        return bool(self.stack)


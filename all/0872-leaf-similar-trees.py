'''
2022/12/08 daily challenge

depth first search approach
'''

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves = []
        stack = [root1]

        # traverse root1 in vertex-left-right order & memorize leaves
        while(stack):
            node = stack.pop()
            if not node:
                continue
            if node.left is None and node.right is None:
                leaves.append(node.val)
            else:
                # VLR
                stack.append(node.right)
                stack.append(node.left)
        
        # traverse root2 in vertex-right-left order & match with root1's leaves
        stack = [root2]
        while(stack):
            node = stack.pop()
            if not node:
                continue
            if node.left is None and node.right is None:
                if not(leaves and leaves.pop() == node.val):
                    # leaves mismatch, two trees are not leaf-similar.
                    return False
            else:
                # VRL
                stack.append(node.left)
                stack.append(node.right)
        
        if leaves:
            # insufficient leaves from 2nd tree to match all leaves from 1s tree,
            # two trees are not leaf-similar.
            return False
        
        # two trees are leaf-similar.
        return True


'''
2024/06/25 daily challenge

inorder traversal approach (recursive ver)
'''


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(node, prev_sum):
            if node.right is not None:
                prev_sum = inorder(node.right, prev_sum)
            
            prev_sum += node.val
            node.val = prev_sum
            
            if node.left is not None:
                prev_sum = inorder(node.left, prev_sum)
            
            return prev_sum

        inorder(root, 0)
        return root


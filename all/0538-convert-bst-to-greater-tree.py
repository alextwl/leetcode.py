'''
2024/06/25 daily challenge

inorder traversal approach (iterative ver)

same to problem 1038:
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
'''


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        prev_sum = 0
        stack = []

        node = root
        while stack or node is not None:
            # RVL
            # traverse right subtree
            while node is not None:
                stack.append(node)
                node = node.right

            # visit
            node = stack.pop()
            prev_sum += node.val
            node.val = prev_sum

            # move to left subtree
            node = node.left

        return root


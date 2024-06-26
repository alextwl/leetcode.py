'''
2024/06/26 daily challenge

inorder traversal approach
'''


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # convert BST to sorted node list
        nodelist = []

        node = root
        stack = []

        while stack or node is not None:
            # LVR
            # left
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            nodelist.append(node)

            node = node.right

        # convert sorted list to balanced tree
        def convert(left, right):
            if left > right:
                return None

            center = (right - left) // 2 + left
            node = nodelist[center]
            node.left = convert(left, center - 1)
            node.right = convert(center + 1, right)

            return node

        return convert(0, len(nodelist) - 1)


'''
2024/06/25 daily challenge

inorder traversal approach (recursive ver)

same to problem 538:
https://leetcode.com/problems/convert-bst-to-greater-tree/
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


'''
morris traversal approach

learnt from official solution 4:
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/solution/
'''


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def get_leftmost(node):
            ret = node.right
            while ret.left is not None and ret.left is not node:
                ret = ret.left
            return ret
        
        prev_sum = 0
        node = root
        while node is not None:
            # assume the node is the current root
            # for the current step of morris traversal
            if node.right is None:
                # visit the node
                prev_sum += node.val
                node.val = prev_sum
                node = node.left
            else:
                # right subtree exists, do morris traversal.
                # check if we need to move left subtree
                # to the child of the leftmost node in the right subtree.
                leftmost = get_leftmost(node)
                if leftmost.left is None:
                    # make a temp link to the current node
                    leftmost.left = node
                    node = node.right
                else:
                    # a left subtree existed means we've created it temporarily
                    # in the previous step, we need to unlink it to recover the tree.
                    leftmost.left = None
                    # visit the node
                    prev_sum += node.val
                    node.val = prev_sum
                    node = node.left

        return root


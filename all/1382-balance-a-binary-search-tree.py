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


'''
Day-Stout-Warren algorithm approach

learnt from official solution 2:
https://leetcode.com/problems/balance-a-binary-search-tree/solution/

also see
https://en.wikipedia.org/wiki/Day%E2%80%93Stout%E2%80%93Warren_algorithm

the DSW algorithm balances the BST, minimize the tree height,
and fills all nodes in the bottom level from left to right.
'''


import math


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def right_rotate(parent, node):
            '''
            parent            parent
                \                \
               three (node)      one (tmp)
               /   \               \
            one     four  =>      three
               \                 /     \
                two             two   four
            '''
            tmp = node.left
            node.left = tmp.right
            tmp.right = node
            parent.right = tmp

        def left_rotate(parent, node):
            '''
            parent          parent
                \               \
               two (node)       four (tmp)
              /   \             /
            one    four  =>    two
                  /           /   \
               three        one  three
            '''
            tmp = node.right
            node.right = tmp.left
            tmp.left = node
            parent.right = tmp
            
        # convert BST to a right-skewed vine
        head = TreeNode(0)  # dummy head with out-of-range value
        head.right = root
        node = head
        while node.right:
            if node.right.left is not None:
                right_rotate(node, node.right)
            else:
                node = node.right
        
        # count nodes
        count = 0
        node = head.right
        while node:
            count += 1
            node = node.right
        
        # convert the vine to a balanced BST
        def make_rotations(head, n_m):
            node = head
            for _ in range(n_m):
                tmp = node.right
                left_rotate(node, tmp)
                node = node.right
        
        power = math.floor(math.log2(count + 1))
        m = 2 ** power - 1
        make_rotations(head, count - m)
        while m > 1:
            m >>= 1
            make_rotations(head, m)

        return head.right


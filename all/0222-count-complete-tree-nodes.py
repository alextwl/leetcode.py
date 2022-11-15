'''
2022/11/15 daily challenge

divide and conquer approach

learnt from
https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time

since the problem asks for time complexity lesser than O(n),
we cannot simply run depth first search because its time=O(v+e) >= O(n).

divide the tree into 2 subtrees and compare its depths.

revisit the definitions of a perfect binary tree and a complete binary tree:
https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees
'''

class Solution:
    def getDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        '''
        the tree is guaranteed to be complete,
        always go down to the left subtree till the end,
        and we'll get the maximum depth of tree.
        '''
        return 1 + self.getDepth(node.left)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        
        if left_depth == right_depth:
            '''
            if both sides of subtrees had the same depth,
            left subtree is always a perfect binary tree (in which all internal nodes
            have two children and all leaves have the same depth or same level),
            and right subtree is either a perfect or a complete binary tree.
            
            because root is a complete binary tree,
            the node number of right side is always equal to or lesser than the left side,
            thus we need to count nodes of the right side.
            
            2**left_depth = root + perfect left nodes = 1 + 2**0 + 2**1 + ... + 2**(h-1) = 2**h
            '''
            return 2**left_depth + self.countNodes(root.right)
        else:
            '''
            the left subtree is deeper than the right.
            
            it means the left subtree has more deeper leaves,
            and the right subtree must be a perfect binary tree
            (because the root is a complete binary tree,
            deeper leaves are always in the left,)
            we need to count nodes of the left side
            since the left might be either perfect or complete.
            
            2**right_depth = root + perfect right nodes = 1 + 2**0 + 2**1 + ... + 2**(h-1) = 2**h
            '''
            return 2**right_depth + self.countNodes(root.left)


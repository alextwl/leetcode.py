'''
2023/08/05 daily challenge

recursive + cache approach

idea: all nodes are the candidates of a root,
and generate the tree by following the attributes of a BST. (L < V < R)
'''

import functools


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @functools.cache
        def genTree(left, right):
            if left > right:
                return [None]  # an empty child
            
            trees = []
            for v in range(left, right+1):
                '''
                generate trees in the range of:
                
                               TreeNode(v)
                                   |
                           +-------+-------+
                           |               |
                genTree(left..v-1)   genTree(v+1..right)
                '''
                for left_child in genTree(left, v - 1):
                    for right_child in genTree(v + 1, right):
                        trees.append(TreeNode(v, left_child, right_child))
            return trees

        return genTree(1, n)


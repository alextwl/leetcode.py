'''
2023/02/28 daily challenge

preorder hash + depth first search approach

use preorder hash to find duplicates.
'''

import collections


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        h = collections.Counter()
        ans = []

        def preorder(node):
            '''
            VLR order, return encoded preorder string of the tree.
            '''
            if not node:
                return ''

            # key = V-L-R           
            key = str(node.val) + '-' + preorder(node.left) + '-' + preorder(node.right)

            h[key] += 1
            if h[key] == 2:
                # we only need to return the root node of any one of the duplicate subtrees,
                # so we append the answer once exactly.
                ans.append(node)
            
            return key
        
        preorder(root)
        return ans


'''
2024/12/20 daily challenge

level order traversal approach
'''


import collections


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lv0 = [root]
        if root.left is None:
            return root
        lv1 = [root.left, root.right]
        lv2 = []

        lv = 1
        while lv1:
            for node in lv1:
                if node.left is not None:
                    lv2.append(node.left)
                    lv2.append(node.right)
                else:
                    break

            if lv & 1:
                lv1.reverse()
                i = 0
                for parent in lv0:
                    parent.left = lv1[i]
                    parent.right = lv1[i+1]
                    i += 2
                if lv2:
                    j = 0
                    for node in lv1:
                        node.left = lv2[j]
                        node.right = lv2[j+1]
                        j += 2

            lv0, lv1 = lv1, lv2
            lv2 = []
            lv += 1

        return root


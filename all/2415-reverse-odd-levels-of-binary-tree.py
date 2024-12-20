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


'''
depth first search approach (recursive ver)
'''


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left, right, lv):
            if left is None:
                # it's perfect so check only left.
                return
            if lv & 1:
                # swap the values of each node
                left.val, right.val = right.val, left.val
            lv += 1
            dfs(left.left, right.right, lv)
            dfs(left.right, right.left, lv)

        dfs(root.left, root.right, 1)
        return root


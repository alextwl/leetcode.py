'''
level order traversal approach
'''


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        prev = [root]
        while prev:
            curr = []
            vals = []
            for node in prev:
                vals.append(node.val)
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            ans.append(vals)
            prev = curr
        ans.reverse()
        return ans


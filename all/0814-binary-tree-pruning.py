'''
2022/09/06 daily challenge
DFS approach
'''
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return False
            
            leftHasOne = dfs(node.left)
            rightHasOne = dfs(node.right)
            
            # prune the subtrees
            if not leftHasOne:
                node.left = None
            if not rightHasOne:
                node.right = None
            
            # return whether the subtrees (if avail) or node itself have a value one or not.
            return (leftHasOne or rightHasOne or node.val)
        
        return root if dfs(root) else None

'''
2022/09/07 daily challenge

intuitive approach
'''
class Solution2:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        
        rootstr = str(root.val)
        leftstr = self.tree2str(root.left)
        rightstr = self.tree2str(root.right)
        if leftstr or rightstr:
            leftstr = "(%s)" % leftstr
        if rightstr:
            rightstr = "(%s)" % rightstr
        
        return rootstr + leftstr + rightstr

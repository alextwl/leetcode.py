'''
2022/09/24 daily challenge

DFS approach
'''

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []  # a template space for constructing each valid path
        
        def dfs(node: Optional[TreeNode], remainSum: int):
            if not node:
                return
            
            # visit the node
            remainSum -= node.val
            path.append(node.val)
            
            if not node.left and not node.right:
                '''
                leaf reached, time to validate the path.
                '''
                if remainSum == 0:
                    ans.append(path.copy())  # the template instance will be reused later, so append a shallow copy.
            else:
                dfs(node.left, remainSum)
                dfs(node.right, remainSum)
            
            path.pop()  # remove current node so that we can traverse back to parent.
        
        dfs(root, targetSum)
        return ans

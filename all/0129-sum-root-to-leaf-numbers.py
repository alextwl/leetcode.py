'''
2023/03/14 daily challenge

depth first search approach
'''

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        ans = 0
        q = [("", root)]  # (path in str format, node)
        while(q):
            path, node = q.pop()
            path = path + str(node.val)
            if node.left is None and node.right is None:
                # add to the sum
                ans += int(path)
            else:
                if node.right:
                    q.append((path, node.right))
                if node.left:
                    q.append((path, node.left))
        
        return ans


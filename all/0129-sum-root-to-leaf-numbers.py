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


'''
2024/04/15 daily challenge

stack + depth first search approach (recursive ver)
'''


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        prefixes = [0]
        total = 0
        
        def dfs(node):
            nonlocal prefixes, total
            
            if node.left is None and node.right is None:
                total += prefixes[-1] + node.val
            else:
                prefixes.append((prefixes[-1] + node.val) * 10)
                if node.left: dfs(node.left)
                if node.right: dfs(node.right)
                prefixes.pop()
        
        dfs(root)

        return total


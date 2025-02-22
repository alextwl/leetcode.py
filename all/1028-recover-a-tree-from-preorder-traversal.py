'''
2025/02/22 daily challenge

depth first search + stack approach
'''


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        decimal = []
        depth = 0
        for c in traversal:
            if c == '-':
                if decimal:
                    stack.append((int(''.join(decimal)), depth))
                    depth = 1
                    decimal = []
                else:
                    depth += 1
            else:
                decimal.append(c)
        stack.append((int(''.join(decimal)), depth))
        stack.reverse()

        def dfs(depth):
            if not stack or stack[-1][1] != depth:
                return None
            node = TreeNode(val=stack.pop()[0])
            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)
            return node

        return dfs(0)


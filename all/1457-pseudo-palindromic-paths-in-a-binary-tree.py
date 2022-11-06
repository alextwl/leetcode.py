'''
2022/09/14 daily challenge
'''

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, mask: int) -> int:
            # let mask be a 10-bit integer,
            # each bit is a mask corresponding to node value digits 1~9
            mask = mask ^ (1 << (node.val))
            
            if node.left is None and node.right is None:
                if bin(mask)[2:].count('1') > 1:
                    return 0
                else:
                    return 1
            
            left = right = 0
            if node.left:
                left = dfs(node.left, mask)
            if node.right:
                right = dfs(node.right, mask)
            
            return left + right
        
        return dfs(root, 0)


'''
iterative + stack approach
learnt from official solution
'''
    
class Solution2:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]  # (node, mask)
        ans = 0
        
        while stack:
            node, mask = stack.pop()
            if node is not None:
                mask = mask ^ (1 << node.val)
                if node.left is None and node.right is None:
                    if mask & (mask - 1) == 0:
                        # same as `bin(mask)[2:].count('1') > 1`
                        # 0b100 & 0b011 = 0 (match)
                        # 0b110 & 0b101 = 4 (mismatch)
                        # 0b111 & 0b110 = 6 (mismatch)
                        ans += 1
                else:
                    stack.append((node.left, mask))
                    stack.append((node.right, mask))
        return ans

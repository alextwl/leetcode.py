'''
2022/12/09 daily challenge

depth first search approach

memorize the minimum & maximum values between ancestors and current node,
and then calculate the maximum difference among them.
'''

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack = [(root, root.val, root.val)]  # [(node, minVal, maxVal)]
        maxDiff = 0

        while(stack):
            node, minVal, maxVal = stack.pop()
            if node:
                # update the maximum difference
                maxDiff = max(maxDiff, abs(minVal - node.val), abs(maxVal - node.val))
                # queue next nodes
                nextMinVal, nextMaxVal = min(minVal, node.val), max(maxVal, node.val)
                stack.append((node.right, nextMinVal, nextMaxVal))
                stack.append((node.left, nextMinVal, nextMaxVal))
        
        return maxDiff


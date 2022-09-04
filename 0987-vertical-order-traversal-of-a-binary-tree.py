'''
2022/09/04 daily challenge

intuitive way
'''

from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        coord = defaultdict(lambda: defaultdict(list))
        # coord[col][row] = list(), note that seq of row & col changed to col & row.
        
        def traverse(node: Optional[TreeNode], col: int, row: int):
            if node is None:
                return
            
            # visit node: save coordinates
            coord[col][row].append(node.val)
            
            traverse(node.left, col-1, row+1)
            traverse(node.right, col+1, row+1)
        
        # start traversing tree.
        traverse(root, 0, 0)
        
        # build ans
        ans = list()
        for col in sorted(coord.keys()):
            vals = []
            for row in sorted(coord[col].keys()):
                vals.extend(sorted(coord[col][row]))
            ans.append(vals)
        
        return ans

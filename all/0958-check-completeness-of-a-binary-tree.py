'''
2023/03/15 daily challenge

breadth first search approach
'''


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        current_q = [root]
        next_q = []

        while(current_q):
            term_found = False
            for node in current_q:
                if node:
                    if term_found:
                        # a terminal was already found in the right side
                        return False
                    next_q.append(node.left)
                    next_q.append(node.right)
                else:
                    term_found = True
            
            if term_found:
                if all(n is None for n in next_q):
                    break
                else:
                    return False

            current_q = next_q
            next_q = []
        
        return True


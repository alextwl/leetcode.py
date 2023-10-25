'''
2023/10/25 daily challenge

depth first search approach
'''


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        root = 0
        for lv in range(n-1, 0, -1):
            width = 2 ** lv
            if k > (width >> 1):
                # the target is in the right side
                if root == 0:
                    next_root = 1
                else:
                    next_root = 0
                k -= width >> 1
            else:
                # the target is in the left side
                if root == 0:
                    next_root = 0
                else:
                    next_root = 1

            root = next_root
        
        return root


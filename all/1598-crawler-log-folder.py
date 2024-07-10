'''
2024/07/10 daily challenge

counter approach
'''


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        lv = 0  # the level of current path (main=0)
        
        for op in logs:
            if op == '../':
                if lv:
                    lv -= 1
            elif op != './':
                lv += 1

        return lv


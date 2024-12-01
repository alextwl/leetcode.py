'''
2024/12/01 daily challenge

set approach
'''


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        
        for v in arr:
            if v << 1 in seen:
                return True
            if v & 1 == 0 and v >> 1 in seen:
                return True
            seen.add(v)

        return False


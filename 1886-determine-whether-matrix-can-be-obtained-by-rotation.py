'''
learnt from
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/discuss/1266035/Python-Very-detailed-explanation-of-one-liner-solution-(for-python-beginners)
'''

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            # compare if initial input was equivalent to target or not.
            # 0 degree rotation == 360 degree rotation
            return True
        # rotate 3 times and compare with target
        for _ in range(0,3):
            # zip(*mat[::-1]) -> regroup each column of rows -> 90-degree rotated matrix
            mat = [list(x) for x in zip(*mat[::-1])]
            if mat == target:
                return True
        
        return False

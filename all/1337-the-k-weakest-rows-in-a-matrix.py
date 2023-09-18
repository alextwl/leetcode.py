'''
2023/09/18 daily challenge
'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_soldiers = []
        
        # count soldiers for each row
        for idx, row in enumerate(mat):
            soldier = 0
            for cell in row:
                if not cell:
                    break
                soldier += 1
            row_soldiers.append((soldier, idx))
        
        # sort by soldier and its row index.
        row_soldiers.sort()
        
        return [idx for _, idx in row_soldiers[:k]]


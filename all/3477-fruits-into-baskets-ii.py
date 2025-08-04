'''
simulation approach
'''


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for v in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= v:
                    baskets[i] = 0  # used
                    break
            else:
                unplaced += 1
        return unplaced


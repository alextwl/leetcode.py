'''
2024/07/01 daily challenge

counter approach
'''


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = 0
        for v in arr:
            if v & 1:
                odds += 1
                if odds >= 3:
                    return True
            else:
                odds = 0

        return False


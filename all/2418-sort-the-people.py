'''
2024/07/22 daily challenge
'''


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [na for _, na in sorted(zip(heights, names), reverse=True)]


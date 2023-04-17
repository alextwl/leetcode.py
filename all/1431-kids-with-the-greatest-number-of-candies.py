'''
2023/04/17 daily challenge
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        threshold = max(candies) - extraCandies
        return [kidCandies >= threshold for kidCandies in candies]


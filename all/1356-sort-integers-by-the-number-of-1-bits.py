'''
2023/10/30 daily challenge

sort by 2 keys
'''

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bit_arr = [(v.bit_count(), v) for v in arr]
        bit_arr.sort()
        return [v for _, v in bit_arr]


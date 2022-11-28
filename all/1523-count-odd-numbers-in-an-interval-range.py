'''
programming skills lv1 day 1

bitwise approach

count(odd, odd) = 1 + diff//2
count(odd, even) = 1 + diff//2
count(even, odd) = 1 + diff//2
count(even, even) = diff//2

fn() = (low or high) & 1 + diff//2 
'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((low | high) & 1) + ((high-low)>>1)


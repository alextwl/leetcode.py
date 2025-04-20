'''
2025/04/20 daily challenge

math approach
'''


import collections
import math


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ctr = collections.Counter(answers)

        rabbits = 0
        for key, cnt in ctr.items():
            # if some rabbits said there're **other** k rabbits having the
            # same color, then there're (k+1) rabbits having the same color.
            total_of_a_color = key + 1
            quo = math.ceil(cnt / total_of_a_color)
            rabbits += quo * total_of_a_color

        return rabbits


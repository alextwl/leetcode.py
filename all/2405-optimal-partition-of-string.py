'''
2023/04/04 daily challenge

greedy + bitmask approach
'''

class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1  # at least 1 partition initially

        a = ord('a')
        letters = 0  # letter bitmap
        for c in s:
            mask = 1<<(ord(c) - a)
            if letters & mask:
                # add one more partition
                partitions += 1
                letters = mask
            else:
                letters |= mask
        
        return partitions


'''
greedy + hash approach
'''

import string


class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1  # at least 1 partition initially

        letter_pos = {c: -1 for c in string.ascii_lowercase}  # each letter's last position
        begin = 0  # current partition's beginning position
        for i, c in enumerate(s):
            if letter_pos[c] >= begin:
                begin = i
                partitions += 1
            letter_pos[c] = i

        return partitions


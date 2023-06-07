'''
bit-to-bit comparsion ver
'''

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        while(start or goal):
            if (start & 1) != (goal & 1):
                flips += 1
            start >>= 1
            goal >>= 1

        return flips


'''
XOR oneliner ver
'''

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal)[2:].count('1')


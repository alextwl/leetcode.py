'''
2024/07/08 daily challenge

simulation approach
'''


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1, n+1)]

        j = 0
        while n > 1:
            # count the next k ppl including the fd we started at.
            j = (j+k-1) % n
            circle = circle[:j] + circle[j+1:]
            n -= 1

        return circle[0]


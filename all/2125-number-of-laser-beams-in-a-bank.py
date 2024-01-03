'''
2024/01/03 daily challenge

greedy method approach
'''


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        prev = 0

        for row in bank:
            if curr := row.count('1'):
                    beams += prev * curr
                    prev = curr

        return beams


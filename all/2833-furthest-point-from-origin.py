'''
try to make moves[i] == '_' to the same direction.
'''


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('R') - moves.count('L')) + moves.count('_')


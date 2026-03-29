'''
sorting approach

build ranks[i][j] for i-th team's j-th vote count,
sort by ranks[i] in descending order,
and then i char in alphabetical order.
'''


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = len(votes[0])
        keys = list(votes[0])
        ranks = {c: [0] * teams for c in keys}

        for voting in votes:
            for i, c in enumerate(voting):
                # convert to negative votes
                # in order to sort votes in descending order.
                ranks[c][i] -= 1

        keys.sort(key=lambda c: (ranks[c], c))
        return ''.join(keys)


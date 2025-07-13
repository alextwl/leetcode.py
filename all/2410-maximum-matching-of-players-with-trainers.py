'''
2025/07/13 daily challenge

sorting + greedy method approach

iterate players & trainers from the most ability & training capacity matches.
'''


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        matches = 0
        t_it = iter(trainers)
        curr_trainer = next(t_it)
        for ability in players:
            if ability <= curr_trainer:
                matches += 1
                try:
                    curr_trainer = next(t_it)
                except StopIteration:
                    break

        return matches


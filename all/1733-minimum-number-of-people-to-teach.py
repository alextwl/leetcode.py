'''
2025/09/10 daily challenge

brute-force + set approach
'''


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # convert languages to a list of sets
        langsets = [None]
        for langlist in languages:
            langsets.append(set(langlist))

        disjoints = set()
        for u, v in friendships:
            if not langsets[u] & langsets[v]:
                disjoints.add(u)
                disjoints.add(v)

        min_teaches = len(disjoints)
        # brute-force
        for i in range(1, n + 1):
            count = 0
            # teach i-th lang
            for u in disjoints:
                if i not in langsets[u]:
                    count += 1
            min_teaches = min(min_teaches, count)

        return min_teaches


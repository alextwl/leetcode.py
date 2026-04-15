'''
2026/04/15 daily challenge

linear search approach

note the target might be duplicated, so we need to search all words.
'''


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = n
        for i, w in enumerate(words):
            if w == target:
                # (1) difference between target & startIndex in non-circular order.
                # (2) target comes first, startIndex is after the array's end.
                # (3) startIndex comes first, target is after the array's end.
                min_dist = min(min_dist, abs(i - startIndex), n + startIndex - i, n - startIndex + i)
        return min_dist if min_dist < n else -1


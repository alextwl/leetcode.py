'''
2025/02/05 daily challenge

counter approach
'''


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff_count = 0
        diffs = [0] * 26
        for a, b in zip(s1, s2):
            if a != b:
                diffs[ord(a) - ord('a')] += 1
                diffs[ord(b) - ord('a')] -= 1
                diff_count += 1
                if diff_count > 2:
                    return False
        return not any(diffs)


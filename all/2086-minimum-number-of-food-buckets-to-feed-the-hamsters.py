'''
dynamic programming approach

strategy:
(1) if left bucket already filled, feed it.
(2) seek right empty bucket.
(3) seek left empty bucket.
'''


class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        buckets = [0] * n
        for i, c in enumerate(hamsters):
            if c == 'H':
                left, right = i - 1, i + 1
                if left >= 0 and buckets[left]:
                    # food already placed at left bucket
                    pass
                elif right < n and hamsters[right] == '.':
                    # place food at right bucket
                    buckets[right] = 1
                elif left >= 0 and hamsters[left] == '.':
                    # place food at left bucket
                    buckets[left] = 1
                else:
                    return -1
        return sum(buckets)


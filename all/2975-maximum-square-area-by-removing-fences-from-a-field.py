'''
2026/01/16 daily challenge

exhaustive method approach
'''


import itertools


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def get_gaps(fences, bound):
            # input fences should be already sorted
            gaps = [b - a for a, b in itertools.pairwise(fences)]
            gaps.insert(0, fences[0] - 1)
            gaps.append(bound - fences[-1])
            all_gaps = []
            # prefix sum of gap width
            psum = list(itertools.accumulate(gaps))  # [1,2,3,...] -> [1,3,6,...]
            psum.insert(0, 0)
            # brute-force all possible lengthes of gaps
            for r in range(1, len(psum)):
                for left in range(0, len(psum) - r):
                    all_gaps.append(psum[left + r] - psum[left])
            return set(all_gaps)

        gset0 = get_gaps(sorted(hFences), m)
        gset1 = get_gaps(sorted(vFences), n)

        root = max(gset0 & gset1, default=0)
        if not root:
            return -1
        return (root * root) % 1_000_000_007


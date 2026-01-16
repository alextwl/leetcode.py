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


'''
enumeration approach

learnt from official editorial:
https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/editorial/#approach-enumeration

no need to get length between fences and build prefix sum.
just get the difference of fences with nested loops and we can have
all possible lengthes of gaps.
'''


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def get_gaps(fences, bound):
            fences.insert(0, 1)
            fences.append(bound)
            return {fences[j] - fences[i] for i in range(len(fences)) for j in range(i + 1, len(fences))}

        gset0 = get_gaps(sorted(hFences), m)
        gset1 = get_gaps(sorted(vFences), n)

        root = max(gset0 & gset1, default=0)
        if not root:
            return -1
        return (root * root) % 1_000_000_007


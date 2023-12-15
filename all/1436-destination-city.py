'''
2023/12/15 daily challenge

set approach
'''


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dst = set(), set()
        for a, b in paths:
            src.add(a)
            dst.add(b)
        # the problem guarantees there's exactly one destination city.
        return (dst - src).pop()


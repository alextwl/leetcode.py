'''
2025/04/09 daily challenge

set approach

each distinct integer needs an operation performed.
'''


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        for v in nums:
            if v < k:
                return -1
            seen.add(v)
        return len(seen - {k})  # no need op for k itself


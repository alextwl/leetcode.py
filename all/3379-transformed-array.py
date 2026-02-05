'''
2026/02/05 daily challenge

enumerate circular array by modulo of index.
'''


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i + v) % len(nums)] for i, v in enumerate(nums)]


'''
2026/10/12 daily challenge

counter + greedy method approach
'''


MASKS = list(map((1).__lshift__, range(30)))


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bit_count = [0] * 30  # because (10**9).bit_length() == 30

        for v in nums:
            for i, mask in enumerate(MASKS):
                if v & mask:
                    bit_count[i] += 1

        ans = 0
        for _ in range(k):
            curr = 0
            # make each value as big as possible by bitwise OR-ing from MSB to LSB
            for i in range(29, -1, -1):
                if bit_count[i]:
                    curr = curr | MASKS[i]
                    bit_count[i] -= 1
            ans = (ans + curr * curr) % 1_000_000_007

        return ans


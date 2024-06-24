'''
2024/06/24 daily challenge

sliding window + XOR property approach
'''


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bit_flipped = [False] * n

        flips_in_window = 0
        flip_count = 0

        for i, b in enumerate(nums):
            if i >= k and bit_flipped[i - k]:
                # flipped nums[i-k] is out of the current window,
                # so we decrease the count of flips
                flips_in_window -= 1

            # conditions to flip the bit in the window:
            #
            # (1) odd times of bit flipped + original nums[i]==1:
            #     that means nums[i] was flipped to 0
            #     and we need to flip it back to 1.
            #
            # (2) even times of bit flipped + original nums[i]==0:
            #     that means nums[i] might (not) be flipped in even times and
            #     nums[i] remains 0 due to the parity invariance of XOR property,
            #     and we need to flip it to 1.
            if (flips_in_window & 1) == b:
                if i + k > n:
                    # k-flip window overflows, impossible to get all 1s array
                    return -1

                flips_in_window += 1
                bit_flipped[i] = True
                flip_count += 1

        return flip_count


'''
2024/05/30 daily challenge

prefix sum approach (one pass ver)

learnt from official solution 4:
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/solution/

hint: it utilizes the technique of two counters of prefix sums
to calculate the occurance of XOR values in middle subsequences.
'''

import collections


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        prefix = 0  # prefix XOR value

        xor_count = collections.defaultdict(int)
        xor_count[0] = 1

        seen_count = collections.defaultdict(int)

        for i, v in enumerate(arr):
            prefix ^= v

            ans += xor_count[prefix] * i - seen_count[prefix]

            xor_count[prefix] += 1
            seen_count[prefix] += i + 1

        return ans


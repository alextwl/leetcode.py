'''
2025/08/11 daily challenge

bitwise + prefix sum approach
'''


MOD = 1_000_000_007


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # the array can be formed by the binary representation of n directly.
        # seperate each set bit of n from LSB and generate prefix products.
        prod_prefix = []
        curr_prefix = 1
        i = 0
        while n:
            if n & 1:
                curr_prefix *= 1 << i
                prod_prefix.append(curr_prefix)
            n >>= 1
            i += 1

        ans = []
        for left, right in queries:
            if left > 0:
                ans.append((prod_prefix[right] // prod_prefix[left - 1]) % MOD)
            else:
                ans.append(prod_prefix[right] % MOD)
        return ans


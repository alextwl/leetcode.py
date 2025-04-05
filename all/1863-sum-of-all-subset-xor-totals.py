'''
2024/05/20 daily challenge
2025/04/05 daily challenge

backtracing approach
'''


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def recurse_subset(i, xor_sum):
            if i == n:
                return xor_sum

            xor_i = recurse_subset(i + 1, xor_sum ^ nums[i])
            non_xor_i = recurse_subset(i + 1, xor_sum)

            # no need to trace visited nodes,
            # we can just accumulate each value of subset XOR.
            return xor_i + non_xor_i

        return recurse_subset(0, 0)


'''
bitwise OR & shift approach inspired from patterns

learnt from official solution 3:
https://leetcode.com/problems/sum-of-all-subset-xor-totals/solution/
'''


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for v in nums:
            ans |= v
        return ans << (n - 1)


'''
brute force approach

the input range is small, we can generate all possible subsets
and summarize its XOR values.
'''


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        prev_xors = [0]  # existed subsets
        for v in nums:
            curr_xors = []
            for x in prev_xors:
                curr_xors.append(x ^ v)
            prev_xors.extend(curr_xors)
        return sum(prev_xors)


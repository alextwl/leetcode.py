'''
2024/12/28 daily challenge

sliding window approach
'''


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sub_sums = []
        curr_sum = 0
        it = enumerate(nums, start=-k)
        for _ in range(k):
            curr_sum += next(it)[1]
        sub_sums.append(curr_sum)

        for prev_i, curr_val in it:
            print(prev_i)
            curr_sum += curr_val - nums[prev_i]
            sub_sums.append(curr_sum)

        max_sum = -1  # single subarray's max sum
        max_i = -1
        two_sums = []  # [sum(sub1 + sub2), sub1's first index]

        # pair middle subarray with previous maximum subarray
        for i, (a, b) in enumerate(zip(sub_sums, sub_sums[k:])):
            # j = i + k
            if a > max_sum:
                max_sum = a
                max_i = i
            two_sums.append((max_sum + b, max_i))

        # pair third subarray with previous 2sum pairs
        max_sum = -1  # two subarray's max sum
        max_j = -1
        overall_max = -1
        ans = None
        for j, (ab, c) in enumerate(zip(two_sums, sub_sums[k*2:]), start=k):
            if ab[0] > max_sum:
                max_sum = ab[0]
                max_j = j

            if (abc := max_sum + c) > overall_max:
                ans = [two_sums[max_j - k][1], max_j, j + k]
                overall_max = abc

        return ans


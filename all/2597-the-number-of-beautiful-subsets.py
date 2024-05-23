'''
2024/05/23 daily challenge

backtracing with bitset approach (slow, runtime ~10secs)
'''


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def count_subsets(i, bitset):
            if i == n:
                # a non-empty bitset is a valid beautiful subset
                return 1 if bitset else 0

            is_valid = True
            for j in range(i):
                if ((1 << j) & bitset) == 0 or abs(nums[j] - nums[i]) != k:
                    # nums[i] & nums[j] can be included together in the current subset
                    continue
                else:
                    is_valid = False
                    break

            # count of valid subsets without nums[i]
            count = count_subsets(i + 1, bitset)

            if is_valid:
                count += count_subsets(i + 1, bitset + (1 << i))

            return count

        return count_subsets(0, 0)


'''
2024/06/22 daily challenge

sliding window approach

counting at most k is much easier than counting exact k.

exact k = at most k - at most (k-1)
'''


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most_k(k):
            odds = 0
            subarrays = 0
            left = 0
            for right, v in enumerate(nums):
                if v & 1:
                    odds += 1
                while odds > k:
                    if nums[left] & 1:
                        odds -= 1
                    left += 1
                subarrays += right - left + 1
            return subarrays
        return at_most_k(k) - at_most_k(k - 1)


'''
yet another sliding window approach

when the window has k+1 odds, count nice subarrays
with measuring the length of non-odd prefix & suffix length of the window.
'''


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nice = 0
        odds = 0
        left_odd = -1

        for i, v in enumerate(nums):
            if v & 1:
                odds += 1

            if odds > k:
                # time to count nice subarrays
                # part 1: count left non-odd prefix length
                prefix_len = 0
                for j in range(left_odd + 1, len(nums)):
                    if nums[j] & 1:
                        break
                    prefix_len += 1
                left_odd = j  # update the position of leftmost odd in the window

                # part 2: count right non-odd suffix length
                suffix_len = 0
                for j in range(i - 1, -1, -1):
                    if nums[j] & 1:
                        break
                    suffix_len += 1

                # part 3: accumulate nice subarrays
                nice += (prefix_len + 1) * (suffix_len + 1)

                # shrink window: maintain odds == k
                odds -= 1

        # count last batch of nice subarrays
        if odds == k:
            # part 1
            prefix_len = 0
            for j in range(left_odd + 1, len(nums)):
                if nums[j] & 1:
                    break
                prefix_len += 1
            # part 2
            suffix_len = 0
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] & 1:
                    break
                suffix_len += 1
            # part 3
            nice += (prefix_len + 1) * (suffix_len + 1)

        return nice


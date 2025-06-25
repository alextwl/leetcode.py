'''
2025/06/25 daily challenge

binary search approach

split products by sign and search different combinations of products
'''


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # split arrays by sign
        neg1 = [-v for v in reversed(nums1) if v < 0]  # reverse both sign & order for convenience
        pos1 = [v for v in nums1 if v >= 0]
        neg2 = [-v for v in reversed(nums2) if v < 0]
        pos2 = [v for v in nums2 if v >= 0]

        # total count of negative products
        neg_counts = len(neg1) * len(pos2) + len(neg2) * len(pos1)

        # determine the k-th product is negative or not
        if k > neg_counts:
            # non-negative product
            sign = 1
            k -= neg_counts
        else:
            # negative product
            sign = -1
            k = neg_counts - k + 1  # reverse order
            neg2, pos2 = pos2, neg2

        def count(arr1, arr2, target):
            # linear search the number of order of target product
            ret = 0
            j = len(arr2) - 1
            for i, v1 in enumerate(arr1):
                while j >= 0 and v1 * arr2[j] > target:
                    j -= 1
                ret += j + 1
            return ret

        # binary search the product
        left, right = 0, 10_000_000_000  # because the max product is 10**5 * 10**5

        while left < right:
            mid = (left + right) // 2
            # for negative product it's actually count(neg1, pos2, mid) + count(pos1, neg2, mid)
            if count(neg1, neg2, mid) + count(pos1, pos2, mid) >= k:
                right = mid
            else:
                left = mid + 1
        return sign * left


'''
2023/11/15 daily challenge
2026/06/28 daily challenge

greedy method + sorting approach
'''


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        max_val = 0

        for v in arr:
            max_val = min(max_val+1, v)

        return max_val


'''
counting sort approach

time=O(n)
'''


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        counts = [0] * (n + 1)
        ans = 1

        # trim heights beyond n
        # because it's impossible to have a height > n
        # within abs(arr[i] - arr[i - 1]) <= 1 condition.
        for v in arr:
            counts[min(v, n)] += 1

        for v, cnt in enumerate(counts[2:], start=2):
            ans = min(ans + cnt, v)

        return ans


'''
2026/02/10 daily challenge

brute-force approach

simply use brute force with dict.
prefix counter subtraction is much slower and TLE.
'''


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            odds = {}
            evens = {}
            for j in range(i, n):
                v = nums[j]
                if v & 1:
                    odds[v] = odds.get(v, 0) + 1
                else:
                    evens[v] = evens.get(v, 0) + 1
                if len(odds) == len(evens):
                    ans = max(ans, j - i + 1)

        return ans


'''
optimized brute force with set
'''


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            # no need to count amount of each distinct number,
            # we only need the difference.
            seen = set()
            delta = 0  # difference between evens & odds

            if ans > (n - i):
                # shortcut: current maximum is already larger than nums[i:]
                break

            for j in range(i, n):
                v = nums[j]
                if v not in seen:
                    # shortcut: only count unseen numbers
                    if v & 1:
                        delta -= 1
                    else:
                        delta += 1
                    seen.add(v)

                if delta == 0:
                    ans = max(ans, j - i + 1)

        return ans


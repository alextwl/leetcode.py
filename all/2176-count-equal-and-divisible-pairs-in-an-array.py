'''
2025/04/17 daily challenge

exhaustive method approach
'''


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        indices = dict()

        # collect indices by value
        for i, v in enumerate(nums):
            if v not in indices:
                indices[v] = list()
            indices[v].append(i)

        ans = 0
        # iterate each distinct value which appears in multiple indices.
        for v, idx_list in indices.items():
            if len(idx_list) < 2:
                continue
            for a, i in enumerate(idx_list):
                if i % k == 0:
                    # shortcut: if i is divisible by k, then (i * j) is also divisible.
                    ans += len(idx_list) - 1 - a
                else:
                    for b in range(a + 1, len(idx_list)):
                        j = idx_list[b]
                        if (i * j) % k == 0:
                            ans += 1
        return ans


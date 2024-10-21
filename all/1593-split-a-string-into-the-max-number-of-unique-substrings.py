'''
2024/10/21 daily challenge

depth first search approach (backtracking)
'''


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()

        def dfs(idx):
            if idx == n:
                return 0

            max_split = 0

            for j in range(idx + 1, n + 1):
                # try each substring starting from s[idx]
                sub = s[idx:j]
                if sub not in seen:
                    seen.add(sub)
                    max_split = max(max_split, dfs(j) + 1)
                    seen.remove(sub)
            return max_split

        return dfs(0)


'''
backtracking + pruning

learnt from official solution 2:
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/solution/
'''


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()
        max_split = 0  # update only when the search reaches the end of s.

        def dfs(idx, splited_num):
            nonlocal max_split

            if splited_num + (n - idx) <= max_split:
                # no need recurring further because remaining length of s[idx:]
                # cannot contribute enough split parts more than max_split.
                return

            if idx == n:
                # entire string searched. update the maximum
                max_split = max(max_split, splited_num)
                return

            splited_num += 1
            for j in range(idx + 1, n + 1):
                sub = s[idx:j]
                if sub not in seen:
                    seen.add(sub)
                    dfs(j, splited_num)
                    seen.remove(sub)
            return

        dfs(0, 0)

        return max_split


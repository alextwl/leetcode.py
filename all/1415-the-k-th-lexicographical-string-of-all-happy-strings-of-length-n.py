'''
2025/02/19 daily challenge

backtracking + exhaustive approach

generate all possible happy strings, sort,
and return the k-th lexicographical one.
'''


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happystr = []

        def dfs(arr):
            if len(arr) == n:
                nonlocal happystr
                happystr.append(''.join(map(lambda x: chr(ord('a') + x), arr)))
                return

            for x in range(3):
                if arr and x == arr[-1]:
                    continue
                arr.append(x)
                dfs(arr)
                arr.pop()
            return

        dfs([])

        if len(happystr) < k:
            return ""
        happystr.sort()

        return happystr[k - 1]


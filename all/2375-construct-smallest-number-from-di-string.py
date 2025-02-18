'''
2025/02/18 daily challenge

backtracking + exhaustive approach

try to generate all valid string by backtracking.
'''


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern) + 1
        smallest = "9" * n

        arr = []
        used = set()

        def dfs(i):
            if len(arr) == n:
                nonlocal smallest
                smallest = min(smallest, ''.join(map(str, arr)))
                return
            if pattern[i] == 'I':
                # a < b
                for k in range(arr[-1] + 1, n + 1):
                    if k not in used:
                        used.add(k)
                        arr.append(k)
                        dfs(i + 1)
                        arr.pop()
                        used.remove(k)
            else:
                # a > b
                for k in range(arr[-1] - 1, 0, -1):
                    if k not in used:
                        used.add(k)
                        arr.append(k)
                        dfs(i + 1)
                        arr.pop()
                        used.remove(k)
            return

        for x in range(1, n + 1):
            used.add(x)
            arr.append(x)
            dfs(0)
            arr.pop()
            used.remove(x)

        return smallest


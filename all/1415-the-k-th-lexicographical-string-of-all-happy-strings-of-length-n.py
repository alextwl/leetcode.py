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


'''
combinatorics approach

learnt from official editorial 4:
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/editorial/#approach-4-combinatorics
'''


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # total strings = 3 * (2 ** (n - 1))
        if k > 3 * (1 << (n - 1)):
            return ""
        
        arr = ["a"] * n

        next_smallest = {'a': 'b', 'b': 'a', 'c': 'a'}
        next_greatest = {'a': 'c', 'b': 'c', 'c': 'b'}

        # split valid strings into 3 groups and find start indices of groups
        # a: 1 ~ 2**(n-1)
        start_a = 1
        # b: 2**(n-1)+1 ~ 2*2**(n-1)
        start_b = (1 << (n - 1)) + start_a
        # c: 2*2**(n-1)+1 ~ 3*2**(n-1)
        start_c = (1 << (n - 1)) + start_b

        # determine the first char by group
        if k < start_b:
            # the first char is 'a'.
            k -= start_a
        elif k < start_c:
            # the first char is 'b'.
            arr[0] = "b"
            k -= start_b
        else:
            # the first char is 'c'.
            arr[0] = "c"
            k -= start_c
        
        for i in range(1, n):
            # the size of group at i-th char is 2**(n-i) and
            # can be divided into two parts with size 2**(n-i-1).
            #
            # the next char is always one of two chars except the previous one,
            # compare remaining k with middle point index to determine the next char.
            mid = 1 << (n - i - 1)
            if k < mid:
                arr[i] = next_smallest[arr[i - 1]]
            else:
                arr[i] = next_greatest[arr[i - 1]]
                k -= mid

        return ''.join(arr)


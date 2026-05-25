'''
2026/05/25 daily challenge

difference array approach
'''


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        n = len(s)
        diff = [0] * (n + maxJump + 1)
        # base case: the nearest where 0 can jump to.
        diff[minJump] = 1
        # base case: the position next to the farthest where 0 can jump to.
        diff[maxJump + 1] = -1

        it = enumerate(s)
        next(it)
        for i, c in it:
            diff[i] += diff[i - 1]
            if s[i] == '1':
                # skip obstacle
                continue
            if diff[i] == 0:
                # i is unreachable
                continue
            diff[i + minJump] += 1
            diff[i + maxJump + 1] -= 1

        return diff[n - 1] > 0


'''
breadth first search approach (TLE)
'''


import collections


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        n = len(s)
        target = n - 1
        seen = {i for i, c in enumerate(s) if c == '1'}
        seen.add(0)
        q = collections.deque([0])
        while q:
            i = q.popleft()
            for j in range(i + minJump, min(i + maxJump, target) + 1):
                if j == target:
                    return True
                if j not in seen:
                    q.append(j)
                    seen.add(j)
        return False


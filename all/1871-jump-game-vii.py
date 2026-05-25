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
graph traversal + visited set approach
'''


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # shortcuts for invalid cases
        # we must verify these corner cases first, or it'd be TLE.
        if s[-1] == '1':
            return False
        if '1' * maxJump in s:
            return False

        n = len(s)
        target = n - 1

        if minJump == maxJump:
            # test if target is reachable through fixed-length jumps
            return target % minJump == 0 and '1' not in s[::minJump]

        seen = {0}
        stack = [0]
        while stack:
            i = stack.pop()
            for j in range(i + minJump, min(i + maxJump, target) + 1):
                if j == target:
                    return True
                if s[j] == '0' and j not in seen:
                    stack.append(j)
                    seen.add(j)
        return False


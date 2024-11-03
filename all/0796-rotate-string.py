'''
2024/11/03 daily challenge

brute force approach
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i, c in enumerate(s):
            if c == goal[0] and (s[i:] + s[:i]) == goal:
                return True
        return False


'''
finding goal in the doubled string approach
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s * 2)


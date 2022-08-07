class Solution:
    def maxDepth(self, s: str) -> int:
        mdepth = 0
        depth = 0
        for c in s:
            if c == "(":
                depth += 1
                mdepth = max(mdepth, depth)
            if c == ")":
                depth -= 1
        return mdepth

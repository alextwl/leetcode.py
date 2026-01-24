'''
backtracking approach
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def gen(prefix, opened, closed):
            if opened == 0 and closed == n:
                ans.append(''.join(prefix))
                return
            if opened > 0:
                prefix.append(')')
                gen(prefix, opened - 1, closed + 1)
                prefix.pop()
            if opened + closed < n:
                prefix.append('(')
                gen(prefix, opened + 1, closed)
                prefix.pop()

        gen([], 0, 0)
        return ans


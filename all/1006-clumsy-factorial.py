'''
simulation approach
'''


class Solution:
    def clumsy(self, n: int) -> int:
        # assume ans = ans + opnd
        ans, opnd = 0, n

        it = iter(range(n - 1, 0, -1))
        try:
            # 1st batch
            opnd = opnd * next(it)
            opnd = opnd // next(it)
            ans, opnd = ans + opnd, next(it)
            ans, opnd = ans + opnd, -next(it)
            # 2nd and later batches
            for v in it:
                # '*'
                opnd = opnd * v
                # '/'
                # note 30//4 == 7 and (-30)//4 == -8,
                # we need -(30 // 4) == -7.
                opnd = -((-opnd) // next(it))
                # '+'
                ans, opnd = ans + opnd, next(it)
                # '-'
                ans, opnd = ans + opnd, -next(it)
        except StopIteration:
            pass
        return ans + opnd


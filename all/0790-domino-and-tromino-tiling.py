'''
2022/12/24 daily challenge

dynamic programming approach

learnt from
https://leetcode.com/problems/domino-and-tromino-tiling/solutions/116506/python-recursive-dp-solution-with-cache-w-explanation/
'''

MODULO = (10**9) + 7


class Solution:
    def numTilings(self, n: int) -> int:
        dp_D = {0: 0, 1: 1, 2: 2}  # board filled without empty cell
        dp_T = {0: 0, 1: 0, 2: 1}  # board filled with 1 empty cell in the end of column

        for i in range(3, n+1):
            '''
            grown board fully filled by the following ways

            (1)
            ------------+---+
                        | o |
             dp_D[i-1]  +---+
                        | o |
            ------------+---+

            (2)
            ------------+---+---+
                        | o | o |
             dp_D[i-2]  +---+---+
                        | x | x |
            ------------+---+---+

            (3)
            ------------+---+---+      ------------+---+---+
                        | o | o |                      | o |
             dp_T[i-1]  +---+---+  or   dp_T[i-1]  +---+---+
                            | o |                  | o | o |
            ------------+---+---+      ------------+---+---+
            '''
            dp_D[i] = (dp_D[i-1] + dp_D[i-2] + dp_T[i-1]*2) % MODULO

            '''
            grown board partially filled with 1 empty cell by the following ways

            (1) dp_D[i-2] + a tromino
            ------------+---+---+
                        | o | o |
             dp_D[i-2]  +---+---+
                        | o |
            ------------+---+

            (2) dp_T[i-1] + a domino
            ------------+---+---+
                        | o | o |
             dp_T[i-1]  +---+---+
                            |
            ------------+---+

            note the equation weren't doubled for cases of empty cell in bottom-right or top-right corners
            because it's eventually doubled when retrieved by calculating dp_D[i].
            '''
            dp_T[i] = (dp_T[i-1] + dp_D[i-2]) % MODULO
        
        # the 2*n board must be fully filled, so we get the answer from the last dp_D.
        return dp_D[n]


'''
2023/05/04 daily challenge

queue approach
'''

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qr, qd = deque(), deque()

        for i, s in enumerate(senate):
            if s == 'R':
                qr.append(i)
            else:
                qd.append(i)

        while(qr and qd):
            r = qr.popleft()
            d = qd.popleft()

            '''
            note the procedure is **multiple rounds**,
            the senate who exercises its right does **not** mean losing its seat in the next round,
            so we append its index+n to indicate the senate may enter the next round
            in order to compare to the opposites (which is also index+n) in the next round with the same base.

            but if any opposite survived in this round, the previous senate may be also banned
            because its new index is always larger than current round's senate.
            '''
            if r < d:
                '''
                r bans d, the senate r survives and enters the next round
                (or to be banned by the another d senate in this round.)
                '''
                qr.append(n+r)
            else:
                '''
                d bans r, the senate r survives and enters the next round
                (or to be banned by the another r senate in this round.)
                '''
                qd.append(n+d)

        return "Radiant" if qr else "Dire"


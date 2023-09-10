'''
2023/09/10 daily challenge

permutation + combination approach

for n=1, there's only single slot to be filled by (P1, D1), so the result(1) = 1.

for n=2, there're the following slots can be filled by (P2, D2):

    [slot0, P1, slot1, P2, slot2], total 3 available slots.
    
    so we can know slots(n) = (n-1)*2 + 1,
    and we can get the following results:
    
    where P2 fixed in slot 0:
    [P2, D2, P1, D2], [P2, P1, D2, D2], [P2, P1, D1, D2],
    where P2 fixed in slot 1:
    [P1, P2, D2, D1], [P1, P2, D1, D2],
    where P2 fixed in slot 2:
    [P1, D1, P2, D2].
    
    result(2) = 6
                          slots(n) * (slots(n) + 1)
    so we get result(n) = -------------------------
                                      2

    countOrders(n) = result(1) * ... * result(n-1) * result(n)

for n=3, there're slots(3) = 5, result(3) = 5 * (5+1) / 2 = 15.

    countOrders(3) = 1 * 6 * 15 = 90.
'''


class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        
        for i in range(2, n+1):
            slots = (i - 1) * 2 + 1
            result = slots * (slots + 1) // 2
            ans *= result
            ans %= 1_000_000_007

        return ans


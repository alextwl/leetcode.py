'''
2023/02/15 daily challenge
'''

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # convert k to array-form
        klist = []
        quo = k
        while(quo > 9):
            quo, rem = divmod(quo, 10)
            klist.append(rem)
        klist.append(quo)

        # num + klist
        ans = []
        num.reverse()
        carry = 0
        for i in range(max(len(num), len(klist))):
            a = num[i] if i < len(num) else 0
            b = klist[i] if i < len(klist) else 0
            s = a+b+carry
            if s >= 10:
                carry = 1
                s -= 10
            else:
                carry = 0
            ans.append(s)
        if carry:
            ans.append(1)
        ans.reverse()

        return ans


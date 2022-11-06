class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzcnt = 0
        buzzcnt = 0
        ret = list()
        for i in range(1, n+1):
            fizzcnt += 1
            buzzcnt += 1
            isFizz = False
            isBuzz = False
            if (fizzcnt == 3):
                fizzcnt = 0
                isFizz = True
            if (buzzcnt == 5):
                buzzcnt = 0
                isBuzz = True
            if (isFizz and isBuzz):
                ans = "FizzBuzz"
            elif isFizz:
                ans = "Fizz"
            elif isBuzz:
                ans = "Buzz"
            else:
                ans = str(i)
            ret.append(ans)
        return ret

'''
2023/12/07 daily challenge

find the position of the rightmost odd digit

the **longest** substring ending with an odd digit
forms the largest odd number in string.
'''


class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = set("13579")

        last_odd = None
        for i, c in enumerate(reversed(num)):
            if c in odds:
                last_odd = i
                break
        else:
            # no odd found
            return ""

        return num[:len(num) - last_odd]


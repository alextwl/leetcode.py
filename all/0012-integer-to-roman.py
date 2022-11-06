class Solution:
    def intToRoman(self, num: int) -> str:
        rev = str(num)[::-1]
        nlen = len(rev)
        roman = ""
        if nlen >= 4:
            roman += "M" * int(rev[3])
        if nlen >= 3:
            c = int(rev[2])
            if c == 9:
                roman += "CM"
            elif c == 4:
                roman += "CD"
            elif c >= 5:
                roman += "D" + "C" * (c-5)
            else:
                roman += "C" * c
        if nlen >= 2:
            x = int(rev[1])
            if x == 9:
                roman += "XC"
            elif x == 4:
                roman += "XL"
            elif x >= 5:
                roman += "L" + "X" * (x-5)
            else:
                roman += "X" * x
        # first dight
        i = int(rev[0])
        if i == 9:
            roman += "IX"
        elif i == 4:
            roman += "IV"
        elif i >= 5:
            roman += "V" + "I" * (i-5)
        else:
            roman += "I" * i

        return roman

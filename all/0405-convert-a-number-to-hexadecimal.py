'''
remainder approach
'''


MAX32 = 0xFFFFFFFF
CHARMAP = "0123456789abcdef"


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            return self.toHex(MAX32 + num + 1)  # 2's complement

        arr = []
        while num:
            num, rem = divmod(num, 16)
            arr.append(CHARMAP[rem])
        return ''.join(reversed(arr))


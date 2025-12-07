'''
assign 'a' to each char and try to enlarge from rightmost char.
'''


ORD_A = ord('a')


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        arr = [0] * n
        k -= n
        for i in range(n):
            adds = min(k, 25)
            arr[i] += adds
            k -= adds
            if k == 0:
                break
        return ''.join(chr(ORD_A + v) for v in reversed(arr))


'''
find lengthes of heading 'a' + trailing 'z'
'''


ORD_A = ord('a')


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # subtract 'a' bases
        rem = k - n
        # find how many trailing 'z' we could generate
        z, rem = divmod(rem, 25)  # 26 - 1
        if rem:
            # heading 'a' + one 'b'-to-'y' char + trailing 'z'
            return 'a' * (n - z - 1) + chr(ORD_A + rem) + 'z' * z
        # heading 'a' + trailing 'z'
        return 'a' * (n - z) + 'z' * z


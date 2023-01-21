'''
2023/01/21 daily challenge

backtracking approach

it's easier to restore the address by proceeding the digit reversely.
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        s = s[::-1]  # reverse the string first.
        valid_addrs = set()

        def addDigit(i: int, addr: List[str], j: int):
            '''
            :param i: the index of s[i] to be proceeded
            :param addr: an octet-per-element list of restoring address in reversed order
            :param j: the index of addr[j] to be proceeded
            '''
            if i >= len(s):
                if j > 3:
                    # check addr validity only when octets are all formed
                    for octet_str in addr:
                        if len(octet_str) > 1 and octet_str[0] == '0':
                            # invalid when octet has leading zeroes ('0*' or '0**'.)
                            return
                    # ship restored address
                    valid_addrs.add('.'.join(addr[::-1]))
                return
            if j > 3:
                # invalid address: insufficient space to add all chars from s.
                return

            # check if we can add s[i] to addr[j]
            if not addr[j]:
                # the octet is empty, feel free to add any digit
                addr[j] = s[i]
                addDigit(i+1, addr.copy(), j)  # try to add next char to the **same** octet
                addDigit(i+1, addr.copy(), j+1)  # try to add next char to the next octet
            else:
                # verify if s[i] can be added to the current octet
                if len(addr[j]) < 2:
                    # octet < 10, feel free to add next char
                    addr[j] = s[i] + addr[j]
                    addDigit(i+1, addr.copy(), j)  # try to add next char to the **same** octet
                    addDigit(i+1, addr.copy(), j+1)  # try to add next char to the next octet
                elif len(addr[j]) == 2:
                    if s[i] == '1':
                        # octet < 100, can form 100~199
                        addr[j] = '1' + addr[j]
                        addDigit(i+1, addr.copy(), j+1)  # try to add next char to the next octet
                    elif s[i] == '2' and int(addr[j]) <= 55:
                        # octet <= 55, can form 200~255
                        addr[j] = '2' + addr[j]
                        addDigit(i+1, addr.copy(), j+1)  # try to add next char to the next octet
            return

        # start from s[0] & addr[0]
        addDigit(0, ['', '', '', ''], 0)

        return list(valid_addrs)


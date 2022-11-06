class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ''' quick ans
        return bin(int(a, base=2) + int(b, base=2))[2:]
        '''
        
        # convert str to base2 int manually
        
        abin = 0
        for c in a:
            abin = abin << 1
            if c == '1':
                abin += 1
        bbin = 0
        for c in b:
            bbin = bbin << 1
            if c == '1':
                bbin += 1
        return bin(abin+bbin)[2:]

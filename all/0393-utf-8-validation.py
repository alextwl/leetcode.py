'''
2022/09/13 daily challenge
'''

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        pos = 0
        
        while(pos < len(data)):
            # 1 byte char
            if (data[pos] >> 7) == 0:
                pos += 1
                continue
            
            # 2-4 bytes char
            if (data[pos] >> 5) == 0b110:
                follows = 1
            elif (data[pos] >> 4) == 0b1110:
                follows = 2
            elif (data[pos] >> 3) == 0b11110:
                follows = 3
            else:
                # invalid leading octet
                return False
            
            for _ in range(0, follows):
                pos += 1
                try:
                    if (data[pos] >> 6) != 0b10:
                        # invaild followed octet
                        return False
                except IndexError:
                    # insufficient octets of multibyte char
                    return False
            # validation passed, check next unicode char
            pos += 1
        
        return True

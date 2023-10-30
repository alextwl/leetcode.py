'''
2023/10/30 daily challenge

sort by 2 keys
'''

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bit_arr = [(v.bit_count(), v) for v in arr]
        bit_arr.sort()
        return [v for _, v in bit_arr]


'''
sort by 2 keys (use hamming weight instead of builtin bit count)
'''

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def hamming_weight(val):
            weight = 0
            mask = 1
            
            while(val):
                if val & mask:
                    # bit matches, flip the matched bit to zero by XOR
                    val ^= mask
                    weight += 1
                mask <<= 1
            
            return weight
        
        arr.sort(key=lambda v: (hamming_weight(v), v))
        return arr


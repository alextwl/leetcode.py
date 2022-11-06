'''
XOR cancel approach

try to recover elements by canceling first and recovered numbers.
'''

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        
        for enc in encoded:
            '''
            encoded[i] = arr[i] XOR arr[i+1]
            encoded[i] XOR arr[i] = arr[i] XOR arr[i+1] XOR arr[i] = arr[i+1]
            
            arr[i+1] can be recovered when encoded[i] & arr[i] given.
            '''
            arr.append(enc ^ arr[-1])
        
        return arr

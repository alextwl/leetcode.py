'''
2023/07/03 daily challenge
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        swapped = False
        pending = None
        
        if len(s) != len(goal):
            # strings with different length cannot be buddy
            return False
        
        for a, b in zip(s, goal):
            if a != b:
                if swapped:
                    # another pair of difference occured
                    return False
                if pending:
                    if pending == (b, a):
                        # accept the swap
                        swapped = True
                    else:
                        # pair to be swapped mismatch
                        return False
                else:
                    # memorize the diffence
                    pending = (a, b)
        
        # the entire string scanned, verify if there're other situations
        if swapped:
            # the buddy strings confirmed
            return True
        elif pending:
            # not swapped but there's one difference
            return False
        
        # s == goal, try to find two same char to satisfy buddy condition
        chars = set()
        for c in s:
            if c in chars:
                # swapping the same character in different locations is possible.
                return True
            chars.add(c)
        
        return False


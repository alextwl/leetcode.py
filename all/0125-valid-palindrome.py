class Solution:
    def isPalindrome(self, x: str) -> bool:
        low = 0
        high = len(x) - 1
        
        while (low < high):
            # skip non-alphanumerics
            while (low < high and not x[low].isalnum()):
                low += 1
            while (high > low and not x[high].isalnum()):
                high -= 1
            if (x[low].lower() != x[high].lower()):
                return False
            low += 1
            high -= 1

        return True

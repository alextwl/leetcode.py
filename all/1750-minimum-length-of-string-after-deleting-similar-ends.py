'''
2024/03/05 daily challenge

two pointer approach
'''


class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        while(left < right):
            if s[left] != s[right]:
                break
            
            target = s[left]
            
            for i in range(left, right):
                if s[i] != target:
                    break
            else:
                # all chars deleted
                return 0
            
            left = i
            
            for j in range(right, left-1, -1):
                if s[j] != target:
                    break
            
            right = j
        
        return right - left + 1


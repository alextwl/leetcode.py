'''
2022/11/04 daily challenge

pointer approach

scan vowels from left and right of input string.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aieouAIEOU")  # target chars
        s = list(s)  # convert string to list for further swap operations.
        left = 0
        slen = right = len(s) - 1
        
        while (left < right):
            # filter non-vowel from left
            while (left < slen and s[left] not in vowels):
                left += 1
            # vowel found or went over the end of s 
            while (right >= 0 and s[right] not in vowels):
                right -= 1
            # vowel found or went over the beginning of s
            
            if (left < right):
                # swap vowels only if left & right pointers didn't pass by each other.
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)

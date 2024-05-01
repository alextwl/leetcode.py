'''
2024/05/01 daily challenge

reverse portion of the word by range.
'''


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, v in enumerate(word):
            if v == ch:
                ans = word[:i+1][::-1] + word[i+1:]
                break
        else:
            ans = word

        return ans


'''
stack approach
'''


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        for i, v in enumerate(word):
            stack.append(v)
            if v == ch:
                stack.reverse()
                ans = ''.join(stack) + word[i+1:]
                break
        else:
            ans = word

        return ans


'''
two pointer approach
'''


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = list(word)
        
        left = 0
        for right in range(len(arr)):
            if arr[right] == ch:
                while left < right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
                return ''.join(arr)

        return word


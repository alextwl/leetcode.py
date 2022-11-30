'''
Newton's method approach
https://en.wikipedia.org/wiki/Newton%27s_method

Runtime: 16 ms, faster than 99.98% of Python3 online submissions
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = (num+1)//2
        while(root**2 > num):
            root = (root + num/root)//2
        return root**2 == num


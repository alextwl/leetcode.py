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


'''
binary search lv1 day 3
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        
        while(left <= right):
            mid = left + (right-left)//2
            if (sq:=mid**2) == num:
                return True
            elif sq > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False


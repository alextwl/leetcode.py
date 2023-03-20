'''
2023/03/20 daily challenge

greedy approach
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        repeat_zeroes = 0

        # special case: the first bed is available for plant
        # flowerbed=[0,0,1,0,1], n=1
        if flowerbed[0] == 0:
            repeat_zeroes = 1

        for flower in flowerbed:
            if flower:
                # there's a flower
                repeat_zeroes = 0
            elif repeat_zeroes == 2:
                # new flower can be planted in the previous bed.
                n -= 1
                repeat_zeroes = 1
                if not n:
                    # all new flowers have been planted.
                    return True
            else:
                # count vacant bed
                repeat_zeroes += 1
        
        # test if we can plant in the last bed
        if repeat_zeroes == 2:
            n -= 1
        
        return n <= 0


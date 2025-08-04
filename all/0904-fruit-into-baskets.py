'''
2023/02/07 daily challenge
2025/08/04 daily challenge

sliding window approach
'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = dict()  # basket[fruitType] = amount of fruit
        start = 0

        for pos, fruitType in enumerate(fruits):
            basket[fruitType] = basket.get(fruitType, 0) + 1

            '''
            we do not remove all extra fruits here but only 1 fruit,
            and the window [start, pos] is not necessarily the exact answer
            of the maximum window of fruits.

            when the basket is full in the first time,
            we remove a fruit and the window size will be maximized.

            that is: len([0, pos-1]) == len([1, pos])

            we don't need to recalculate the max window size or shrink it
            when a type of frult in the basket is replaced,
            as long as the amount of current types of fruits keeps growing,
            the window size always grows up or remains.
            '''
            if len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
        
        return len(fruits) - start


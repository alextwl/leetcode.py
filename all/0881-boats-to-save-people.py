'''
2023/04/03 daily challenge

greedy + two pointer approach
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the weights of people first, order by descending weight
        people.sort(reverse=True)
        left, right = 0, len(people)-1

        # greedy method: pick heavyweight ppl first, and pair it with lightweight one
        boats = 0
        while(left <= right):
            # try to pair it to the another lightweight passenger
            if left < right and people[left] + people[right] <= limit:
                # found
                right -= 1
            # always add a new boat
            boats += 1
            # next fat one
            left += 1

        return boats


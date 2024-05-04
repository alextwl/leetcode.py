'''
2023/04/03 daily challenge
2024/05/04 daily challenge

greedy + two pointer approach
'''


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the weights of people
        people.sort()
        left, right = 0, len(people)-1

        # greedy method: pick heavyweight ppl first,
        # and try to pair it with a lightweight one
        boats = 0
        while(left < right):
            # try to pair it to the another lightweight passenger
            if people[left] + people[right] <= limit:
                # found
                left += 1
            # each pair always has a fat one
            right -= 1
            # always add a new boat
            boats += 1

        # count the orphan
        if left == right:
            boats += 1

        return boats


'''
2022/12/20 daily challenge

breadth first search approach
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        keys = {0}  # room 0 is unlocked initially
        stack = [0]  # let room 0 as root, its stored keys are leaves.

        while(stack):
            room = stack.pop()
            new_keys = rooms[room]
            # queue new keys only
            stack.extend(set(new_keys) - keys)
            # take these keys
            keys.update(new_keys)
            # if all keys were collected, we can return the result early.
            if len(keys) == n:
                return True
        
        # insufficient keys
        return False


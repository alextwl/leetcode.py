'''
leetcode 75 lv2 day 18

stack approach
'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for rock in asteroids:
            if stack:
                if rock > 0:
                    # the asteroid goes right, always append it to stack
                    stack.append(rock)
                else:
                    # the asteroid goes left, check collisions
                    while(stack):
                        last_rock = stack.pop()
                        if last_rock > 0 and rock < 0:
                            if abs(last_rock) > abs(rock):
                                # the incoming rock exploded
                                rock = last_rock
                            elif abs(last_rock) == abs(rock):
                                # both rocks exploded
                                break
                            # else: the last rock exploded
                        else:
                            # append the winner or it has the same direction as last rock.
                            stack.append(last_rock)
                            stack.append(rock)
                            break
                    else:
                        stack.append(rock)
            else:
                stack.append(rock)

        return stack


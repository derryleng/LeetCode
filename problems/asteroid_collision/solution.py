# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        for asteroid in asteroids:
            stack.append(asteroid)
            while (len(stack) > 1):
                y = stack.pop()
                x = stack.pop()
                if x < 0 and y > 0 or x * y > 0:
                    stack += [x, y]
                    break
                if abs(x) > abs(y):
                    stack += [x]
                    break
                elif abs(x) < abs(y):
                    stack += [y]
                elif abs(x) == abs(y):
                    break
        return stack
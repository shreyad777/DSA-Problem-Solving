class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            alive = True
            while (
                alive
                and asteroid < 0
                and stack
                and stack[-1] > 0
            ):
                if stack[-1] < -asteroid:
                    stack.pop()
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(asteroid)
        return stack
asteroids = list(
    map(int, input("Enter asteroids: ").split())
)
solution = Solution()
print(
    "Remaining Asteroids:",
    solution.asteroidCollision(asteroids)
)